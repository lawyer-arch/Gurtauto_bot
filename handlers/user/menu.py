from aiogram import Router, F
from aiogram.types import Message
from keyboards.catalog_keyboards import (
    button_generator_application,
    button_generator_comments
)

router = Router()

# Обработчик кнопки "Оставить заявку на подбор авто"
@router.message(F.text == "📢 Оставить заявку на подбор авто")
async def leave_application(message: Message):
    # Отправляем сообщение с клавиатурой 
    await message.answer(
        "<b>🖊️ Ответте на несколько вопросов</b>\n"
        "<b>и по желанию можете приложить фото,</b>\n"
        "<b>ссылку на Авито или Дром.</b>",
        reply_markup=button_generator_application()
    )


@router.message(F.text == "✨ Отзывы")
async def see_reviews(message: Message):
    # Отправляем сообщение с клавиатурой
    await message.answer(
        "<b>В указанных каналах Вы можете подробно </b>"
        "<b>ознакомится с отзывами сотен клиентов </b>"
        "<b>и более подробно узнать о GURTAUTO.</b>",
        reply_markup=button_generator_comments()
    ) 


@router.message(F.text == "☎️ Контакты")
async def show_contacts(message: Message):
    await message.answer(
        "<b>Как нас найти:</b>\n"
        "<b>Max: +79016131647</b>\n"
        "<b> WhatsApp: +79016131647</b>\n"
        "<b> В СЛУЧАЕ ОТСУТСТВИЯ СВЯЗИ ПРОСТО ЗВОНИТЕ</b>\n"
        "⚠️ПО ☎️ +79016131647"
    )