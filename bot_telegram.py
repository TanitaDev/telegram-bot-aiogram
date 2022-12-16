from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os
TOKEN = '5815856150:AAGVN1VpgKJpj1233Ady9gNTLjPAYvw378A'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_send(message: types.Message):
    if "привет" in message.text:
        await message.answer('привет, любимый')
    # await message.reply(message.text)
    await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True)
