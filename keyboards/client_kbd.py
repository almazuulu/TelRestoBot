from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Помощь')
b2 = KeyboardButton('/Рабочие_часы')
b3 = KeyboardButton('/Локация')
b4 = KeyboardButton('/Меню')
# b4 = KeyboardButton('/Поделиться контактом', request_contact=True)
# b5 = KeyboardButton('/Поделиться локацией', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

#kb_client.add(b1).add(b2).insert(b3)

# kb_client.row(b1, b2, b3) # Кнопки по горизонтали

kb_client.add(b1).row(b2, b3).add(b4)
