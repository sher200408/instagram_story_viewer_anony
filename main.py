
from aiogram import Dispatcher, types

from aiogram.types import Message

from routes.routes import router


TOEKN = geten("BOT_TOKEN")


dp = Dispatcher()

dp.include_router(router)


async def main():
    
    print("bot started")
    
    bot = Bot(token=TOEKN)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    
    asyncio.run(main())
    