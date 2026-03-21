from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from states.states import ApplicationFormStates
from aiogram.fsm.context import FSMContext


router = Router()


# Начало опроса
@router.message(Command("form"))
async def form_start(message: Message, state: FSMContext):
    await state.set_state(ApplicationFormStates.marka)
    await message.answer("Какой марки автомобиль ищете?")


# Сбор марки автомобиля
@router.message(ApplicationFormStates.marka)
async def collect_brand(message: Message, state: FSMContext):
    await state.update_data(marka=message.text)
    await state.set_state(ApplicationFormStates.model)
    await message.answer("Модель автомобиля?")


# Сбор модели автомобиля
@router.message(ApplicationFormStates.model)
async def collect_model(message: Message, state: FSMContext):
    await state.update_data(model=message.text)
    await state.set_state(ApplicationFormStates.year)
    await message.answer("Год выпуска?")


# Сбор года выпуска
@router.message(ApplicationFormStates.year)
async def collect_year(message: Message, state: FSMContext):
    await state.update_data(year=message.text)
    await state.set_state(ApplicationFormStates.budget)
    await message.answer("Какой бюджет рассматриваете?")


# Сбор бюджета
@router.message(ApplicationFormStates.budget)
async def collect_budget(message: Message, state: FSMContext):
    await state.update_data(budget=message.text)
    await state.set_state(ApplicationFormStates.contact)
    await message.answer("Укажите контактные данные для связи:")


# Завершение опроса и сохранение данных
@router.message(ApplicationFormStates.contact)
async def finish_form(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()  # Очистка состояния

    # Формирование итогового сообщения
    result_message = f"Ваши ответы:\n" \
                    f"Марка: {data['marka']}\n" \
                    f"Модель: {data['model']}\n" \
                    f"Год выпуска: {data['year']}\n" \
                    f"Бюджет: {data['budget']}\n" \
                    f"Контакт: {message.text}"

    await message.answer(result_message)