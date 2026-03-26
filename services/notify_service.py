
from aiogram import Bot
from config import settings
from aiogram.types import BufferedInputFile


class NotifyService:

    def __init__(self, bot: Bot):
        self.bot = bot

    async def send_new_lead(self, user_name, phone, data: dict):
        
        # 1. Основное сообщение
        text = (
            "🔥 <b>Новая заявка!</b>\n\n"
            f"👤 {user_name}\n"
            f"📞 {phone}\n\n"
            f"{data.get('marka')} {data.get('model')} ({data.get('color')})\n"
            f"Двигатель: {data.get('engine')}\n"
            f"Привод: {data.get('drive')}\n"
            f"Топливо: {data.get('fuel')}\n"
            f"Пробег: {data.get("mileage")}\n"
            f"Возраст: {data.get("year")}\n"
            f"Состояние: {data.get("repairs")}\n"
            f"Бюджет: {data.get('budget')}"
        )

        await self.bot.send_message(
            chat_id=settings.ADMIN_ID,
            text=text
        )

        # 2. URL (если есть)
        if data.get("url"):
            await self.bot.send_message(
                chat_id=settings.ADMIN_ID,
                text=f"🔗 Ссылка:\n{data.get('url')}"
            )

        # 3. Фото (если есть)
        if data.get("image_data"):
            photo = BufferedInputFile(
                data.get("image_data"),
                filename="car.jpg"
            )

            await self.bot.send_photo(
                chat_id=settings.ADMIN_ID,
                photo=photo,
                caption="📸 Фото от клиента"
            )