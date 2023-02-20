from aiogram import Bot,Dispatcher,types,executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from config import token_api
import random
import string

TEXT = """
Кнопки для бота находятся справа в строке ввода\(Или слева в списке\)

random \- рандомная буква
start \- начать работу
description \- описание бота и мой вк
sticker \- получить стикер
idsticker \- получить id стикера \(в разработке\)
meme \- отправит мемас
"""

bot = Bot(token_api)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/description')
b2 = KeyboardButton('/random')
b3 = KeyboardButton('/sticker')
b4 = KeyboardButton('/meme')
kb.add(b1).insert(b2).add(b3).insert(b4)

ikb = InlineKeyboardMarkup(row_width=3)
ikb1 = InlineKeyboardButton(text="Мой ВК",
                            url='https://vk.com/id_asasin_cross')
ikb2 = InlineKeyboardButton(text="Получить рандомную букву",
                            callback_data='crandom')
ikb.add(ikb1).add(ikb2)

async def on_startup(_):
    print("Бот запущен!")

@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await message.answer(text='*Доступные команды:*\n' + TEXT,
                           parse_mode=types.ParseMode.MARKDOWN_V2,
                           reply_markup=kb)

@dp.message_handler(commands=['description'])
async def desc_comm(message:types.Message):
    await message.answer(text='Этот бот \- мой учебный проект, я сюда сую всё чему учусь',
                           parse_mode=types.ParseMode.MARKDOWN_V2,
                           reply_markup=ikb)


@dp.message_handler(commands=['random'])
async def random_letter(message: types.Message):
    await message.answer(random.choice(string.ascii_letters))

@dp.message_handler(commands=['sticker'])
async def random_letter(message: types.Message):
    await message.answer(text='Чел, твоя просьба это')
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEHy3Rj8Lz5dQkBvGSlZakdSy5_vc1faQACBQADumTPD5yB1fhcw5K-LgQ")

"""@dp.message_handler(commands=['idsticker'])
async def handle_sticker_command(message: types.Message):
    await message.answer("Ну давай твой стикер...")

    # Use another handler to wait for a sticker message
    @dp.message_handler(content_types=types.ContentTypes.STICKER)
    async def handle_sticker(message: types.Message):
        # Get the sticker ID and send it as a message
        sticker_id = message.sticker.file_id
        await message.answer(f"ID этого стикера - {sticker_id}")


    # Use another handler to wait for a non-sticker message
    @dp.message_handler(content_types=types.ContentTypes.ANY)
    async def handle_non_sticker(message: types.Message):
        # Send an error message and ask for a sticker again
        await message.answer("Чел, ты долбоёб? стикер отправляй или иди нахуй... (Вводи заного /idsticker)")"""

@dp.message_handler(commands=['meme'])
async def random_letter(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         photo='https://i.imgur.com/aLhAw5a.png')

@dp.callback_query_handler()
async def random_callback(callback: types.CallbackQuery):
    if callback.data == 'crandom':
        await callback.answer(random.choice(string.ascii_letters))



@dp.message_handler()
async def zero(message:types.Message):
    if '0' in message.text:
        await message.answer('Ноль есть')
    else:
        await message.answer('Нуля нет')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

