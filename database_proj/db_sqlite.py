import sqlite3 as sqlite
from create_bot import dp, bot

def start_conn():
    global db_base, cursor
    db_base = sqlite.connect('restobase.db')
    cursor = db_base.cursor()
    
    if db_base:
        print('Произошло соединение с БД!')
        
    create_sql_script = \
    """CREATE TABLE IF NOT EXISTS menu(
        img TEXT, 
        nameFood TEXT primary key,
        description TEXT,
        price TEXT)
    """
    # cursor.execute("CREATE TABLE IF NOT EXISTS menu(img TEXT,  nameFood TEXT primary key, description TEXT, price TEXT)")
    cursor.execute(create_sql_script)
    db_base.commit()

async def sql_add_item_menu(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO menu VALUES(?, ?, ?, ?)', tuple(data.values()))
    db_base.commit()
    
async def sql_read_data(message):
    for item in cursor.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, item[0], f'{item[1]}\
                             \nОписание: {item[2]}\nЦена: {item[3]}')
        
       
        