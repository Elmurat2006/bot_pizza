from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove, InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery,InputMediaPhoto,InputFile
import sqlite3

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.callback_data import CallbackData



menu = open('img/IMG_7663.PNG', 'rb')
menu2 = open('img/IMG_7664.PNG', 'rb')
menu3 = open('img/IMG_7665.PNG', 'rb')
menu4 = open('img/IMG_7666.PNG', 'rb')
nomer = open('img/IMG_7093.PNG', 'rb')


#db

async def db_start():
    global db,cur

    db = sqlite3.connect('database.db')
    cur = db.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY,photo TEXT,description TEXT, цена TEXT)')

    db.commit()

async def get_pizza(user_id):
    user = cur.execute('SELECT 1 FROM PROFILE  = {key} WHERE user_id'.format(key = user_id)).fetchone()

    if not user:
        cur.execute('INSERT INTO PROFILE VALUE(?,?,?,?,?)',(user_id,'','',''))
        db.commit()

async def get_db(state,user_id):
    async with state.proxy() as data:
        cur.execute('SELECT 1 FROM  SET photo = {},description = {},цена={} PROFILE WHERE user_id = {}'.format(user_id,data['photo'],data['description'],data['цена'],))



HELP_COMMAND = """
<b>/help</b> - Команда поддержки команд
<b>/Каталог</b> - Команда показа каталога
<b>/Менеджер</b> -Команда для связи с менеджером
"""

#bot
Token = '5910106813:AAHhC3JBrpEhbkZ-ewI2oW5E3NhmGAhdKsg'
bot = Bot(Token)
dp = Dispatcher(bot)

#kb
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb1 = KeyboardButton('/help')
kb2 = KeyboardButton('/Каталог')
kb3 = KeyboardButton('/Доставка')
kb4 = KeyboardButton('/Заказ')
kb.add(kb1).add(kb2,kb3).add(kb4)

#ikb
ikb = InlineKeyboardMarkup(row_width=3)
ib1 = InlineKeyboardButton('Купить',url='https://www.instagram.com/halal_pizza/')

ikb.add(ib1)



#handlers

@dp.message_handler(commands=['start'])
async def start_command(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id, text = 'Здравствуйте это пиццерия "HALAL PIZZA"',reply_markup=kb)
    await get_pizza(message.from_user.id)


@dp.message_handler(commands=['help'])
async def help_command(message:types.Message):
    await message.answer(text = f'{HELP_COMMAND}',parse_mode='HTML')


@dp.message_handler(commands=['Каталог'])
async def catalog_command(message:types.Message):
    await bot.send_message(chat_id = message.from_user.id, text = "Каталог наших пицц")
    await bot.send_photo(chat_id = message.from_user.id,photo = menu)
    await bot.send_photo(chat_id = message.from_user.id,photo = menu2)
    await bot.send_photo(chat_id = message.from_user.id,photo = menu3)
    await bot.send_photo(chat_id = message.from_user.id,photo = menu4)



@dp.message_handler(commands=['Доставка'])
async def send_command(message:types.Message) -> None:
    await bot.send_message(chat_id = message.from_user.id, text = "БЕСПЛАТНАЯ ДОСТАВКА В РАЙОНЕ 3 КМ")
    await bot.send_photo(chat_id = message.from_user.id,photo = 'https://instagram.ffru7-1.fna.fbcdn.net/v/t51.2885-15/318241721_474112101542503_2987276709179395951_n.jpg?stp=dst-jpg_e35_p240x240&_nc_ht=instagram.ffru7-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=WKmA-BDbWoUAX9nCtep&edm=ANmP7GQBAAAA&ccb=7-5&ig_cache_key=Mjk4NzQ5MjUzMTY5MTk1ODI2NQ%3D%3D.2-ccb7-5&oh=00_AfC-88aTMoP9ITS68TaMrtSEO__HP62reJ1EmcVWmoLg5g&oe=63B70EF2&_nc_sid=276363')

nomer = '<b><a>070989009,0990890099</a></b>'
@dp.message_handler(commands=['Заказ'])
async def zakaz(message:types.Message) -> None:
    await bot.send_message(chat_id = message.from_user.id, text = f"Позвоните на этот номер,закажите пиццу!  {nomer}",parse_mode='HTML')


if __name__ == '__main__':
    executor.start_polling(dp)