from aiogram import executor
from create_bot import dp
from handlers import client, admin, others
from database_proj import db_sqlite

async def on_startup(_):
    print('Бот вышел в онлайн')
    db_sqlite.start_conn()

if __name__ == '__main__':
    client.register_handlers_client(dp)
    others.register_handlers_client(dp)
    admin.register_handlers_client(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)