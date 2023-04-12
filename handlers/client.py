import logging
import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ReplyKeyboardRemove
from create_bot import dp, bot
from keyboards import kb_client
from database_proj import db_sqlite

async def welcome_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом в личку ч-з адрес @almazuulu')
        
async def resto_open_command(message: types.Message):
    working_schedule = \
    "ПН - ПТ: 9:00 - 19:00 \
    \nСБ - ВС: 15:00 - 22:00"
    
    await bot.send_message(message.from_user.id, working_schedule)
    await message.delete()
    
# @dp.message_handler(commands=['resto_location'])
async def location_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Горького 123', reply_markup=ReplyKeyboardRemove()) 
    await message.delete()

@dp.message_handler(commands=['Меню'])
async def restoran_menu(message: types.Message):
    await db_sqlite.sql_read_data(message)
  
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(welcome_command, commands=['start', 'Помощь', 'help'])
    dp.register_message_handler(resto_open_command, commands=['Рабочие_часы'])
    dp.register_message_handler(location_command, commands=['Локация'])
