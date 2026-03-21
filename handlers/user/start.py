from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.main_menu import generate_main_menu


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    
    await message.answer(
        "<b>🚗 Добро пожаловать!</b>\n"
        "<b>GURTAUTO поможет воплотить мечту в реальность.</b>",
        reply_markup=generate_main_menu()
    )