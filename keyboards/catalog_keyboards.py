from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
    ) 

"""Модуль содержит кнопки интерактива отображаемых для пользователя""" 


def button_generator_application():
    """Генерирует кнопки заявки"""
    
    buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📝 Заполнить форму",
                    callback_data="free_form"
                )
            ],
        ]
    ) 
    
    return buttons 


def button_generator_comments():
    """Генерирует кнопки выбора источника отзывов VK, TG, 2GIS""" 
    
    buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="Вконтакте",
                url="vk.com/gurt_auto"
            ),],
            [InlineKeyboardButton(
                text="Telegram",
                url="https://t.me/gurt_auto"
            ), ],
            [InlineKeyboardButton(
                text="2GIS",
                url="https://2gis.ru/krasnodar/geo/70000001104157255"
            )]
        ]
    )
    
    return buttons
