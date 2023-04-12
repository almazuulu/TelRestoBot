from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_load = KeyboardButton('/Создатьеду')
button_delete = KeyboardButton('/Удалить')

button_admin = ReplyKeyboardMarkup(resize_keyboard=True)
button_admin.add(button_load).add(button_delete)

