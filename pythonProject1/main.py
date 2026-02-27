from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart
import asyncio

TOKEN = "6784902637:AAH7x-37W9ZViPwvR9Dwj1NFAIpMaGER8jA"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="⚽ Открыть Dribbling",
            web_app=WebAppInfo(url="https://z-cyan.vercel.app/")
        )]
    ])

    await message.answer("Добро пожаловать в Dribbling!", reply_markup=keyboard)

@dp.message(F.web_app_data)
async def webapp_data(message: Message):
    await message.answer(f"Получены данные: {message.web_app_data.data}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())