from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from database_proj import db_sqlite
from keyboards import admin_kb

ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    nameFood = State()
    description = State()
    price = State()
    
# getting id of admin
@dp.message_handler(commands=['moderator'], is_chat_admin=True)    
async def make_changes_command(message: Message): 
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что вы желаете  админ?', reply_markup=admin_kb.button_admin)
    await message.delete()

# start of conversation
@dp.message_handler(commands='Создатьеду', state=None)
async def start_conv(message: Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Загрузи фото')
    else:
        await message.reply('Неизвестная команда')
    
# catching the photo from user
# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def upload_photo(message: Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo']= message.photo[0].file_id
        
        await FSMAdmin.next()
        await message.reply("Теперь задай название еде")
    else:
        await message.reply('Неизвестная команда')
    
# catching the name of food
# @dp.message_handler(state=FSMAdmin.nameFood)
async def load_nameFood(message: Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['nameFood'] = message.text
        await FSMAdmin.next()
        await message.reply("Теперь введите описание еды")
    else:
        await message.reply('Неизвестная команда')
    
# catching the description of a food
# @dp.message_handler(state=FSMAdmin.description)
async def load_descr_food(message: Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply("Теперь введите цену для еды") 
        
    else:
        await message.reply('Неизвестная команда')

# catching the price for the food
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)
        await db_sqlite.sql_add_item_menu(state)
        await state.finish()
            
    #     async with state.proxy() as data:
    #         await message.reply(str(data))
    #     await state.finish()
    # else:
    #     await message.reply('Неизвестная команда')
    # await state.finish()
    # await message.reply("Теперь введите цену для еды") 

# exit from FSM
@dp.message_handler(state='*', commands='отмена')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_fsm(message: Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')
    else:
        await message.reply('Неизвестная команда')
    
def register_handlers_client(dp: Dispatcher):
    # dp.register_message_handler(start_conv, commands=['Загрузить'], state=None)
    dp.register_message_handler(upload_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_nameFood, state=FSMAdmin.nameFood)
    dp.register_message_handler(load_descr_food, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    # dp.register_message_handler(cancel_fsm, state='*', commands='отмена')
    # dp.register_message_handler(cancel_fsm, Text(equals='отмена', ignore_case=True), state='*')
    
    

    
    


    
    
    
    
    
    
    


    
    
    
