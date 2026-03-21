import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from config import settings
from handlers.user import start, menu, lead_form
# from handlers.admin import admin_menu, cars, leads


async def main():
    # Контекстный менеджер гарантирует корректное закрытие сессии
    logging.basicConfig(level=logging.INFO)
    async with Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode="HTML")
    ) as bot:

        dp = Dispatcher()  # v3: не передаём bot

        # USER ROUTERS 
        dp.include_router(start.router)
        dp.include_router(menu.router)
        dp.include_router(lead_form.router)
        
        # ADMIN ROUTERS
        # dp.include_router(admin_menu.router)
        # dp.include_router(cars.router)
        # dp.include_router(leads.router)

        # Удаляем вебхук с увеличенным таймаутом
        # await bot.delete_webhook(drop_pending_updates=True, request_timeout=20)

        # Запуск поллинга
        try:
            await dp.start_polling(bot)
        except asyncio.CancelledError:
            print("Polling cancelled, exiting...")


if __name__ == "__main__":
    asyncio.run(main())