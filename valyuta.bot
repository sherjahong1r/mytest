"""
Created on Sun Nov 23 03:43:30 2025
usd, eur, gbp kursini hisoblaydigan bot
@author: Owner
"""


import asyncio
import requests
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

API_KEY = "d70f028eb221e71ddd27674e"  # ExchangeRate API key
BOT_TOKEN = "8251596631:AAGSDDUXdLC7EklLcY4XdyGzQ0K4UqPb6D8"  # Telegram bot token

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


#   /kurs komandasi

@dp.message(Command("kurs"))
async def kurs_handler(message: Message):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/UZS"

    try:
        data = requests.get(url).json()
        usd = data["conversion_rates"]["USD"]
        eur = data["conversion_rates"]["EUR"]
        gbp = data["conversion_rates"]["GBP"]

        text = (
            f"*Bugungi valyuta kurslari:*\n\n"
            f"1 🇺🇸 USD = {1/usd:.2f} so‘m\n"
            f"1 🇪🇺 EUR = {1/eur:.2f} so‘m\n"
            f"1 🇬🇧 GBP = {1/gbp:.2f} so‘m"
        )

        await message.answer(text, parse_mode="Markdown")
    except Exception:
        await message.answer("❌ Kurslarni olishda xatolik yuz berdi.")



#  Oddiy son yuborilganda

@dp.message()
async def convert_handler(message: Message):
    if not message.text.isdigit():
       
        text = (
            "🌟 *Assalomu alaykum!* \n"
            "💱 *Kurs hisoblash botiga xush kelibsiz!* \n\n"

            "📌 *Bot buyruqlari:* \n"
            "• /start — bot haqida maʼlumot\n"
            "• /kurs — bugungi valyuta kurslari\n"
            "• Son kiriting — kiritgan summangizni 3 ta valyutaga aylantirib beradi\n\n"

            "ℹ️ *Eslatma:* Faqat *son* kiriting yoki yuqoridagi *buyruqlar*dan foydalaning."
        )

        await message.answer(text, parse_mode="Markdown")
        return

    amount = int(message.text)

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/UZS"
    data = requests.get(url).json()

    usd_rate = data["conversion_rates"]["USD"]
    eur_rate = data["conversion_rates"]["EUR"]
    gbp_rate = data["conversion_rates"]["GBP"]

    usd = amount * usd_rate
    eur = amount * eur_rate
    gbp = amount * gbp_rate

    text = (
        f"*Konvertatsiya natijalari:*\n\n"
        f"*Yani Valyutangiz natijasi:\n\nUSD (AQSH dollari),*\n"
        f"*EUR (Yevro),\nGBP (Funt sterlin) ko'rinishida chiqadi.*\n\n"
        f"{amount:,} so‘m = {usd:.2f} USD\n"
        f"{amount:,} so‘m = {eur:.2f} EUR\n"
        f"{amount:,} so‘m = {gbp:.2f} GBP"
    ).replace(",", " ")

    await message.answer(text, parse_mode="Markdown")


#   Botni ishga tushirish


async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        print("Spyder console aniqlandi → mavjud loopga ulanyapman...")
        loop.create_task(main())
    else:
        asyncio.run(main())
