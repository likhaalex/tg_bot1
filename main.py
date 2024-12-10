import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from background import keep_alive


TOKEN = '7818186037:AAFROJjR-vT1iKTUDaD26ZDw5DfreWFlImQ'

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Я твой Telegram-бот. Напиши мне что-нибудь, и я отвечу!")

@dp.message()
async def echo_message(message: types.Message):
    await message.answer(f"Ты написал: {message.text}", parse_mode="HTML")

# Запуск бота
async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == '__main__':
    keep_alive()
    asyncio.run(main())
