from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

TOKEN = '5815856150:AAGVN1VpgKJpj1233Ady9gNTLjPAYvw378A'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот вышел в онлайн')

'''*********************КЛИЕНТСКАЯ ЧАСТЬ*********************'''
@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/Pizzanita_bot')


@dp.message_handler(commands=['Режим_работы'])
async def bot_schedule(message: types.Message):
    await bot.send_message(message.from_user.id, 'вт-пт с 09.00 до 22.00')
    await message.answer("вт-пт с 09.00 до 22.00")


@dp.message_handler(commands=['Адрес'])
async def bot_schedule(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Колбасная 59, кв 11')
    await message.answer("ул. Колбасная 59, кв 11")


@dp.message_handler()
async def echo_send(message: types.Message):
    if "привет" in message.text:
        await message.answer('привет, любимый')
    elif "салями" in message.text:
        await message.answer('салями тоже хочу')
    elif "люблю" in message.text:
        await message.answer('люблю тебя')
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup )
