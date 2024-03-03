import asyncio
import telebot.async_telebot
from datetime import date
TOKEN = '6790110505:AAGRBcF-QZLg6DWEOh2D9EWphtDE3hiv4Oc'
bot = telebot.async_telebot.AsyncTeleBot(TOKEN)
chat_id = "-4023351869"
dates = [
    date(2024, 3, 15),
    date(2024, 4, 12),
    date(2024, 5, 10),
    date(2024, 6, 7),
    date(2024, 7, 5),
    date(2024, 8, 2),
    date(2024, 8, 30),
    date(2024, 9, 27),
    date(2024, 10, 25),
    date(2024, 11, 22),
    date(2024, 12, 20),
]

async def periodic_remind():
    while True:
        global bot
        global chat_id
        today = date.today()
        for date_item in dates:
            days_difference = (date_item - today).days
            if days_difference == 3:
                await bot.send_message(chat_id=chat_id, text = f"Через 3 дня {date_item} будет вывоз мусора")
            elif days_difference == 1:
                await bot.send_message(chat_id=chat_id, text = f"Завтра {date_item} будет вывоз мусора")

        await asyncio.sleep(21600)  # Ждать 5 секунд между выполнениями

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:  # Если нет текущего цикла событий
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    loop.create_task(periodic_remind())  # Запуск нашей функции напоминания
    loop.run_forever()