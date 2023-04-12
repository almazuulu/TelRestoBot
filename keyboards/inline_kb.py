from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters import Text

API_TOKEN = '6181728094:AAGKVsSZ_xBjzkrq0JvBg4uL777meHElr4U'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

#Кнопки ссылки
url_kb = InlineKeyboardMarkup(row_width=1)
url_Button = InlineKeyboardButton(text='Ссылка StckOverFlow', url='https://stackoverflow.com/questions/54116641/how-to-fix-sqlite3-operationalerror-incomplete-input-when-the-error-is-rega')
url_Button2 = InlineKeyboardButton(text='Ссылка Pypi:', url='https://pypi.org/')
set_url_buttons = [InlineKeyboardButton(text='Ссылка Youtube:', url='https://youtube.com/'), InlineKeyboardButton(text='Ссылка Amazon:', url='https://amazon.com/'), InlineKeyboardButton(text='Ссылка eBay:', url='https://ebay.com/')]
url_kb.add(url_Button, url_Button2).row(*set_url_buttons).insert(InlineKeyboardButton(text='Ссылка Akipress:', url='https://akipress.org/'))


@dp.message_handler(commands=['Ссылки'])
async def command_url(message: types.Message):
    await message.answer('Все ссылки: ', reply_markup=url_kb)

inline_kb = InlineKeyboardMarkup(row_width=1)
# button1 = InlineKeyboardButton(text='Нажать', callback_data='somebtn')
buttonLike = InlineKeyboardButton(text='Нравится', callback_data='like_1')
buttonDislike = InlineKeyboardButton(text='Не Нравится', callback_data='like_-1')
inline_kb.add(buttonLike).add(buttonDislike)

@dp.message_handler(commands=['test'])
async def command_url(message: types.Message):
    await message.answer('Нравится контент?: ', reply_markup=inline_kb)

answ = dict()    

@dp.callback_query_handler(Text(startswith='like_'))
async def callback_func(callback: types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    
    if f'{callback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = res
        await callback.answer('Мы приняли ваш голос!')
    else:
        await callback.answer('Вы уже голосовали ранее!', show_alert=True)
        
        
    
   
    #await callback.answer('Вы нажали на кнопку Ура!')
    # await callback.message.answer('Вы нажали на кнопку Ура!')
    # await callback.answer('Вы нажали на кнопку Ура!', show_alert=True)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




