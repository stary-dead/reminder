import telebot.async_telebot
import asyncio
from datetime import date
from reminder import periodic_remind

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
TOKEN = '6790110505:AAGRBcF-QZLg6DWEOh2D9EWphtDE3hiv4Oc'
bot = telebot.async_telebot.AsyncTeleBot(TOKEN)

chat_id = "-4023351869"

@bot.message_handler(commands=['start'])
async def start(message):
    global chat_id
    print(f"|{message.chat.id}|")
    await bot.send_message(chat_id, "Привет! Я бот напоминалка.")

@bot.message_handler(commands=['next_musor'])
async def next_musor(message):
    today = date.today()
    next_date = next((d for d in dates if d >= today), None)
    reply_message = (f"Следующая дата вывоза мусора: {next_date.strftime('%A, %d %B')}"
                     if next_date else "Извините, информация о следующем вывозе мусора недоступна.")
    await bot.reply_to(message, reply_message)

@bot.message_handler(commands=['plan'])
async def send_calendar(message):
    with open('plan.jpg', 'rb') as plan_image:
        await bot.send_photo(chat_id, plan_image)

async def periodic_message():
    while True:
        await asyncio.sleep(5)
        remind()

async def remind():
    today = date.today()
    for date_item in dates:
        days_difference = (date_item - today).days
        if days_difference == 3:
            await bot.send_message(chat_id, f"Через 3 дня будет событие {date_item}")
        elif days_difference == 1:
            await bot.send_message(chat_id, f"Завтра будет событие {date_item}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(bot.polling())
    loop.create_task(periodic_remind())
    loop.run_forever()
