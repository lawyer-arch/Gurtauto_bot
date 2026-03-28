import re
import logging
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ContentType, PhotoSize
from aiogram.fsm.context import FSMContext

from states.states import ApplicationFormStates
from database.session import async_session
from database.repository.user_repo import UserRepository
from database.repository.lead_repo import LeadRepository
from services.lead_service import LeadService
from services.notify_service import NotifyService
from keyboards.catalog_keyboards import (
    button_generator_drive,
    button_generator_fuel,
    button_generator_year,
    button_generator_repairs,
    button_generator_further
)

router = Router()


# Вспомогательная функция для извлечения URL изображения
def extract_image_url(text: str):
    match = re.search(r'(https?://\S+\.(?:jpg|jpeg|png|gif|webp))', text)
    return match.group(1) if match else None


""" Выбираем марку, модель, цвет кузова"""
@router.callback_query(F.data == "free_form")
async def start_free_form(callback: CallbackQuery, state: FSMContext):
    get_message = (
        "Укажите марку, модель, цвет кузова желаемого автомобиля.\n"
        "Обязательно в указанном порядке."
    )
    
    await callback.message.answer(get_message)
    await state.set_state(ApplicationFormStates.marka_model)
    await callback.answer()


"""Выбираем объем двигателя"""
@router.message(ApplicationFormStates.marka_model)
async def handler_marka_model(message: Message, state: FSMContext):
    parts = message.text.split()
    if len(parts) < 2:
        await message.answer("❗ Укажите минимум: марка и модель (например: BMW X5)")
        return
    
    marka = parts[0] if len(parts) > 0 else None
    model = parts[1] if len(parts) > 1 else None
    color = " ".join(parts[2:]) if len(parts) > 2 else None
    get_message = (
        "Укажите объем двигателя."
    )
    await state.update_data(
        marka=marka,
        model=model,
        color=color
    )
    await state.set_state(ApplicationFormStates.engine)
    await message.answer(get_message)
    
    
"""Выбираем тип привода"""
@router.message(ApplicationFormStates.engine)
async def select_drive_type(message: Message, state: FSMContext):
    """
    Обработчик выбора типа двигателя.
    Сохраняет выбранный тип двигателя и предлагает выбрать тип привода.
    """
    
    # Сохраняем выбранный тип двигателя в FSMContext
    await state.update_data(engine=message.text)
    
    # Переходим к следующему шагу FSM
    await state.set_state(ApplicationFormStates.drive)
    
    # Предложение пользователю выбрать тип привода
    prompt = "Укажите тип привода."
    
    # Отправляем сообщение с клавиатурой выбора привода
    await message.answer(
        text=prompt,
        reply_markup=button_generator_drive()
    )


"""Выбираем тип топлива"""
@router.callback_query(
    F.data.startswith("drive_"),
    ApplicationFormStates.drive
)
async def select_fuel_type(callback: CallbackQuery, state: FSMContext):
    """
    Обработчик выбора типа привода.
    Сохраняет выбранный тип привода и предлагает выбрать тип топлива.
    """
    
    # Получаем выбранный тип привода из callback_data
    selected_drive = callback.data.split("_")[1]
    
    # Сохраняем выбранный тип привода в FSMContext
    await state.update_data(drive=selected_drive)
    
    # Переходим к следующему шагу FSM
    await state.set_state(ApplicationFormStates.fuel)
    
    # Предложение пользователю выбрать тип топлива
    prompt = "Выберите тип топлива"
    
    # Отправляем сообщение с клавиатурой выбора топлива
    await callback.message.answer(
        text=prompt,
        reply_markup=button_generator_fuel()
    )
    await callback.answer()


"""Выбираем пробег"""
@router.callback_query(
    F.data.startswith("fuel_"),
    ApplicationFormStates.fuel
)
async def handler_mileage(callback: CallbackQuery, state: FSMContext):
    # Получаем выбранное значение топлива из callback_data
    selected_fuel = callback.data.split("_")[1]
    get_message = "Укажите желаемый пробег"
    # Запоминаем выбранное значение в состоянии
    await state.update_data(fuel=selected_fuel)
    # Переводим машину состояний дальше
    await state.set_state(ApplicationFormStates.mileage)
    await callback.message.answer(get_message)
    await callback.answer()
    
    
"""Выбераем возраст авто"""
@router.message(ApplicationFormStates.mileage)
async def handler_year(message: Message, state: FSMContext):
    get_message = "Выберите желаемый диапазон возраста автомобиля"
    await state.update_data(mileage=message.text)
    await state.set_state(ApplicationFormStates.year)
    await message.answer(
        text=get_message,
        reply_markup=button_generator_year()
    )
    

"""Выбираем бюджет"""
@router.callback_query(
    F.data.startswith("year_"),
    ApplicationFormStates.year
)
async def handler_budget(callback: CallbackQuery, state: FSMContext):
    # Получаем выбранное значение топлива из callback_data
    selected_year = callback.data.split("_")[1]
    get_message = "Укажите желаемый бюджет"
    # Запоминаем выбранное значение в состоянии
    await state.update_data(year=selected_year)
    # Переводим машину состояний дальше
    await state.set_state(ApplicationFormStates.budget)
    await callback.message.answer(get_message)
    await callback.answer()
    

"""Выбираем допустимы или нет повреждения"""
@router.message(ApplicationFormStates.budget)
async def handler_repairs(message: Message, state: FSMContext):
    selected_budget = message.text
    get_message = "Выбирите допустимость повреждений"
    await state.update_data(budget=selected_budget)
    await state.set_state(ApplicationFormStates.repairs)
    await message.answer(
            text=get_message,
            reply_markup=button_generator_repairs()
        )


"""Предлагаем оставить ссылку на сайт или фото"""
@router.callback_query(
    F.data.startswith("repairs_"),
    ApplicationFormStates.repairs
)
async def handler_url(callback: CallbackQuery, state: FSMContext):
    # Получаем выбранное значение топлива из callback_data
    selected_repairs = callback.data.split("_")[1]
    get_message = (
        "По желанию оставьте ссылку на выбранный автомобиль Авито, Дром и т.д.\n"
        "либо фото или любое изображение авто.\n\n"
        "Или нажмите «Пропустить», если не хотите прикреплять."
    )
    # Запоминаем выбранное значение в состоянии
    await state.update_data(repairs=selected_repairs)
    # Переводим машину состояний дальше
    await state.set_state(ApplicationFormStates.url_or_image)
    await callback.message.answer(
        get_message,
        reply_markup=button_generator_further()
    )
    await callback.answer()
    

"""Ловит кнопку далее"""
@router.callback_query(F.data == "further", ApplicationFormStates.url_or_image)
async def skip_url_or_image(callback: CallbackQuery, state: FSMContext):
    # Сохраняем None для обоих полей — пользователь ничего не прикрепил
    await state.update_data(url=None, image_data=None)
    await state.set_state(ApplicationFormStates.phone)
    await callback.answer()


"""Предлагаем оставить телефон"""
@router.message(ApplicationFormStates.url_or_image,
              F.content_type.in_({ContentType.TEXT, ContentType.PHOTO}))
async def hanler_url_or_image(message: Message, state: FSMContext):
    try:
        if message.content_type == ContentType.TEXT:
            text = message.text.strip()
            # Проверяем, является ли текст ссылкой
            if re.match(r'https?://\S+', text):
                await state.update_data(url=text, image_data=None)
            else:
                # Если текст не ссылка — считаем, что пользователь ошибся
                await message.answer(
                    "Это не похоже на ссылку. Отправьте фото или нажмите «Пропустить»."
                )
                return

        elif message.content_type == ContentType.PHOTO:
            photo: PhotoSize = max(message.photo, key=lambda x: x.width * x.height)
            photo_file = await message.bot.get_file(photo.file_id)
            photo_bytes = await message.bot.download_file(photo_file.file_path)
            await state.update_data(image_data=photo_bytes.getvalue(), url=None)

        # Переходим к следующему шагу только если данные корректны
        await message.answer("Оставьте контактный номер телефона")
        await state.set_state(ApplicationFormStates.phone)

    except Exception as e:
        logging.error(f"Error processing url/photo: {e}")
        await message.answer(
            "Произошла ошибка. Отправьте фото или ссылку, либо нажмите «Пропустить»."
        )

    
@router.message(ApplicationFormStates.phone)
async def phone_handler(message: Message, state: FSMContext):

    if not message.text:
        await message.answer("❗ Введите телефон")
        return

    # Нормализация
    phone = re.sub(r"[^\d]", "", message.text)
    phone = "+" + phone

    # Валидация
    if not re.match(r"^(\+?\d{1,4})?\d{6,15}$", phone):
        await message.answer("❗ Некорректный телефон. Введите ещё раз (пример: +79991234567)")
        return

    data = await state.get_data()

    async with async_session() as session:

        user_repo = UserRepository(session)
        user = await user_repo.get_or_create(
            message.from_user.id,
            message.from_user.username or "",
            message.from_user.full_name or message.from_user.first_name or ""
        )

        lead_repo = LeadRepository(session)
        service = LeadService(lead_repo)
        
        try:
            await service.create_lead({
                "user_id": user.id,
                "phone": phone,
                "marka": data.get("marka"),
                "model": data.get("model"),
                "color": data.get("color", "не указано"),
                "engine": data.get("engine", "не указано"),
                "drive": data.get("drive", "не указано"),
                "fuel": data.get("fuel", "не указано"),
                "mileage": data.get("mileage", "не указано"),
                "year": data.get("year", "не указано"),
                "budget": data.get("budget", "не указано"),
                "repairs": data.get("repairs", "не указано"),
                "url": data.get("url"),
                "image_data": data.get("image_data")
            })
            await session.commit()
        except Exception as e:
            logging.error(f"DB error: {e}", exc_info=True)
            await message.answer("❗ Ошибка сохранения заявки. Попробуйте позже.")
            return 

    notify = NotifyService(message.bot)

    try:
        await notify.send_new_lead(
            message.from_user.full_name,
            phone,
            data
        )
    except Exception as e:
        logging.error(f"Notify error: {e}")

    await message.answer("✅ Заявка отправлена")
    await state.clear()