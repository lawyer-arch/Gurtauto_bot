
from aiogram import Bot
from config import settings


class NotifyService:

    def __init__(self, bot: Bot):
        self.bot = bot

    async def send_new_lead(self, user_name, phone, car_description):

        text = (
            "🔥 <b>Новая заявка!</b>\n\n"
            f"👤 {user_name}\n"
            f"📞 {phone}\n\n"
            f"{car_description}"
        )

        await self.bot.send_message(
            chat_id=settings.ADMIN_ID,
            text=text,
            parse_mode="HTML"
        )