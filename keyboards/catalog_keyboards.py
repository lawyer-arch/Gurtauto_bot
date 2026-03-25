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


def button_generator_drive():
    
    """Генерирует кнопки выбора привода передний, полный, задний"""
    
    buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="4WD",
                    callback_data="drive_4wd"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Передний привод",
                    callback_data="drive_front"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Задний привод",
                    callback_data="drive_rear"
                )
            ]
        ]
    ) 
    
    return buttons 


def button_generator_fuel():
    
    """Генерирует кнопки выбора топлива бензин, дизель, гибрид, элетрический"""
    
    buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Бензин",
                    callback_data="fuel_petrol"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Дизель",
                    callback_data="fuel_diesel"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Гибрид",
                    callback_data="fuel_hybrid"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Электрический",
                    callback_data="fuel_electric"
                )
            ]
        ]
    ) 
    
    return buttons


def button_generator_year():
    
    """Генерирует кнопки выбора года"""
    
    buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="До 3-х лет",
                    callback_data="year_3"
                )
            ],
            [
                InlineKeyboardButton(
                    text="3-5 лет",
                    callback_data="year_3_5"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Старше 5 лет",
                    callback_data="year_more_than_5"
                )
            ]
        ]
    ) 
    
    return buttons


def button_generator_repairs():
    
    """Генерирует кнопки выбора допустимости повреждений авто"""
    
    buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Допустимо",
                    callback_data="repairs_yes"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Не допустимо",
                    callback_data="repairs_no"
                )
            ]
        ]
    ) 
    
    return buttons
