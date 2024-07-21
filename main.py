from aiogram import Bot, Dispatcher
import asyncio
from bot import bot_router
from admin import admin_router
from database import Base, engine
# TODO токен
bot = Bot(token="7315969917:AAG2Um1dFz6m7v6KZr4Arg5VxhfWN7pNU78")
dp = Dispatcher()
Base.metadata.create_all(bind=engine)

async def main():
    dp.include_router(admin_router)
    dp.include_router(bot_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())