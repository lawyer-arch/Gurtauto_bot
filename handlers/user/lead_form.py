import re
import logging
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from states.states import ApplicationFormStates
from database.session import async_session
from database.repository.user_repo import UserRepository
from database.repository.lead_repo import LeadRepository
from services.lead_service import LeadService
from services.notify_service import NotifyService

router = Router()


# Вспомогательная функция для извлечения URL изображения
def extract_image_url(text: str):
    match = re.search(r'(https?://\S+\.(?:jpg|jpeg|png|gif|webp))', text)
    return match.group(1) if match else None


@router.callback_query(F.data == "free_form")
async def start_free_form(callback: CallbackQuery, state: FSMContext):
    massage = (
        "<b>Опишите авто как можно подробнее.</b>\n"
        "Укажите: Марку, модель, цвет,"
        "объем двигетеля, привод, трансмиссия,"
        "топливо, пробег желаемый, год выпуска. "
        "Желаемый бюджет."
    )
    await callback.message.answer(massage)
    await state.set_state(ApplicationFormStates.WAITING_FOR_DESCRIPTION)
    await callback.answer()


@router.message(ApplicationFormStates.WAITING_FOR_DESCRIPTION)
async def desc_url(message: Message, state: FSMContext):
    if not message.text:
        await message.answer("❗ Пожалуйста, отправьте текст")
        return
    await state.update_data(car_description=message.text)
    await message.answer("По желанию прикрепите по выбору фото, ссылку на Авито, Дром.")
    await state.set_state(ApplicationFormStates.WAITING_FOR_URL_PICTURE)


@router.message(ApplicationFormStates. WAITING_FOR_URL_PICTURE)
async def desc(message: Message, state: FSMContext):
    if not message.text:
        await message.answer("❗ Пожалуйста, отправьте текст")
        return
    await state.update_data(car_description=message.text)
    await message.answer("Введите телефон:")
    await state.set_state(ApplicationFormStates.WAITING_FOR_CONTACTS)


@router.message(ApplicationFormStates.WAITING_FOR_CONTACTS)
async def phone_handler(message: Message, state: FSMContext):

    if not message.text:
        await message.answer("❗ Введите телефон")
        return

    # Нормализация
    phone = re.sub(r"[^\d]", "", message.text)
    phone = "+" + phone

    # Валидация
    if not re.match(r"^\+\d{10,15}$", phone):
        await message.answer("❗ Некорректный телефон. Введите ещё раз (пример: +79991234567)")
        return

    data = await state.get_data()

    # ВАЖНАЯ ПРОВЕРКА FSM
    car_description = data.get("car_description")

    if not car_description:
        await message.answer("❗ Ошибка. Начните заново.")
        await state.clear()
        return

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
                "car_description": car_description,
                "phone": phone,
                "car_id": None
            })
        except Exception as e:
            logging.error(f"DB error: {e}")
            await message.answer("❗ Ошибка сохранения заявки. Попробуйте позже.")
            return 

    notify = NotifyService(message.bot)

    try:
        await notify.send_new_lead(
            message.from_user.full_name,
            phone,
            car_description
        )
    except Exception as e:
        logging.error(f"Notify error: {e}")

    await message.answer("✅ Заявка отправлена")
    await state.clear()