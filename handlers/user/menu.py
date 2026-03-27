from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from keyboards.catalog_keyboards import (
    button_generator_application,
    button_generator_comments
)
import textwrap

router = Router()

MAX_CAPTION = 1024
MAX_MESSAGE = 4000

# Обработчик кнопки "Оставить заявку на подбор авто"
@router.message(F.text == "📢 Оставить заявку на подбор авто")
async def leave_application(message: Message):
    # Отправляем сообщение с клавиатурой 
    await message.answer(
        "<b>🖊️ Ответьте на несколько вопросов</b>\n"
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
    
    
@router.message(F.text == "📄 О нас")
async def show_about_us(message: Message):
    img_path = "image/1000047083.jpg"  # исходное фото
   
    photo = FSInputFile(img_path)
    
    # Короткий текст для подписи (caption)
    short_caption = (
        "<b>Приветствуем вас в GURTAUTO!</b>\n"
        "Мы доставляем автомобили из Китая, Японии, Кореи и Киргизии."
    )
    # Отправляем фото с подписью
    await message.answer_photo(photo=photo, caption=short_caption)
    
    # Полный текст для отдельного сообщения
    full_text = (
        "<i>Если вы планируете приобрести автомобиль в ближайшее время, </i>"
        "<i>просто отправьте нам запрос с помощью бота: @GurtautoBot</i>\n\n"
        "<i>Мы оперативно рассчитаем стоимость с учетом доставки </i>"
        "<i>в ваш город и предложим лучшие условия.</i>\n"
        "<b>Для новых клиентов у нас действует скидка 15% </b>"
        "<b>на нашу комиссию в честь первого сотрудничества!</b>\n\n"
        "<i>Кроме того, участвуйте в нашей акции: </i>"
        "<b>и получите 10 000 рублей за рекомендацию нашей компании</b>\n\n"
        "<b>НАША КОНТАКТЫ И ОТЗЫВЫ ТУТ:👇</b>\n"
        "VK: vk.com/gurt_auto\n"
        "TG: t.me/gurt_auto\n"
        "https://2gis.ru/krasnodar/geo/70000001104157255\n"
        "МАХ: https://max.ru/id7000020472_biz\n\n"
        "<b>ЗАПРОСЫ ДЛЯ РАСЧЁТА СТОИМОСТИ НУЖНОГО ВАМ АВТО НАПРАВЛЯЙТЕ СЮДА:👇</b>\n"
        "➡️ Телеграм бот: @GurtautoBot\n"
        "➡️ СЮДА В https://vk.ru/gurt_auto СООБЩЕСТВО-КНОПКА НАПИСАТЬ СООБЩЕСТВУ\n"
        "➡️ TG: t.me/gurt_auto, ВНИЗУ ИКОНКА СООБЩЕНИЙ\n"
        "➡️ МАХ: https://max.ru/id7000020472_biz\n"
        "➡️ WhatsApp: wa.me/+79016131647\n"
        "➡️ В СЛУЧАЕ ОТСУТСТВИЯ СВЯЗИ ПРОСТО ЗВОНИТЕ\n"
        "⚠️ПО ☎️ 89016131647\n\n"
        "<b>Ждем ваших запросов и готовы помочь с выбором автомобиля вашей мечты!</b>"
    )
    
    # Разбиваем длинный текст на части и отправляем
    messages = textwrap.wrap(full_text, width=MAX_MESSAGE, replace_whitespace=False)
    for part in messages:
        await message.answer(part, parse_mode="HTML")