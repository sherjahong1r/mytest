"""
Created on Mon Nov 2025
Maqola chiqaruvchi bot
@author: Sherjahongir
"""

import wikipedia
import logging
import asyncio
import nest_asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message

API_TOKEN = "8587860656:AAFU5H9M3htzPhOhrF4xCEzT7XgENbEKni8"

logging.basicConfig(level=logging.INFO)

bot = Bot(API_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

# Wikipedia tilini o'rnatamiz
wikipedia.set_lang("uz")


@router.message(F.text == "/start")
async def send_welcome(message: Message):
    await message.answer("Wikipediya botiga Xush kelibsiz!\n\n"
                         "\nBu bot bilan istalgan maqolangizni tez va osson topasiz!\n\n")

    await message.answer("Wikipediya bot buyruqlari:\n"
                         "/start - botni ishga tushirish,\n"
                         "/help - maqolani qidirishni bilmasangiz,\n"
                         "/wiki - bilan maqolani qidirasiz.")

@router.message(F.text == "/help")
async def send_help(message: Message):
    await message.answer("Qanday qidirishni bilmayabsizmi?\n"
                         "Namuna: wiki (maqola nomi)\n"
                         "Misol: wiki O'zbekiston\n"
                         "Eslatma: (wiki so'zini kichik harflarda yozing)")

# Faqat wiki bilan boshlanuvchi xabarlar
@router.message(F.text.startswith("wiki"))
async def wiki_search(message: Message):
    try:
        text = message.text[4:].strip()   # 'wiki' dan keyingi tekstni olish
        result = wikipedia.summary(text)
        await message.answer(result)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi\n"
                             "Iltimos boshqacha mazmunda yozing!")

# Echo faqat wiki bo'lmagan xabarlarga!
@router.message()
async def echo(message: Message):
    if not message.text.startswith("wiki"):
        await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(main())

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
