import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from app.handlers import start, topic, hashtags


async def main():
    # просто стандартный бот, без кастомного AiohttpSession
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(topic.router)
    dp.include_router(hashtags.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
