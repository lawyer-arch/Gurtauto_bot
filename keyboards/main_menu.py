from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def generate_main_menu():
    """Генерирует главное меню""" 
    
    buttons = [
        
        [KeyboardButton(text="📢 Оставить заявку на подбор авто")],
        [ 
            KeyboardButton(text="✨ Отзывы"),
            KeyboardButton(text="☎️ Контакты")
        ],
        [KeyboardButton(text="📄 О нас")]
    ] 
    
    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=False
    )
    
    return keyboard