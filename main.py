from aiogram import Bot,Dispatcher,types,executor
from config import token_api
from keyboards import kb, kb1, ikb1, ikb2
import random
import string

TEXT = """
Кнопки для бота находятся справа в строке ввода\(Или слева в списке\)

/random \- рандомная буква
/start \- начать работу
/description \- описание бота и мой вк
/sticker \- получить стикер
/idsticker \- получить id стикера \(в разработке\)
/meme \- отправит мемас
"""

bot = Bot(token_api)
dp = Dispatcher(bot)

async def on_startup(_):
    print("Бот запущен!")

@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await message.answer(text='*Доступные команды:*\n' + TEXT,
                           parse_mode=types.ParseMode.MARKDOWN_V2,
                           reply_markup=kb)

@dp.message_handler(commands=['description'])
async def desc_comm(message:types.Message):
    await message.answer(text='Этот бот \- мой пет проект, я сюда сую всё чему учусь',
                           parse_mode=types.ParseMode.MARKDOWN_V2,
                           reply_markup=ikb1)
    await message.answer('это сообщение чтобы появилась кнопка',reply_markup=kb1)


@dp.message_handler(commands=['random'])
async def random_letter(message: types.Message):
    await message.answer(random.choice(string.ascii_letters))

@dp.message_handler(commands=['sticker'])
async def random_letter(message: types.Message):
    await message.answer(text='Чел, твоя просьба это')
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEH2V5j9a3kDUz4DO5rCDzQ6R21zrGrjQACIQADumTPDwIruQwj7FhxLgQ")

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
        await message.answer("Чел, ты дурак? стикер отправляй или отвали... (Вводи заного /idsticker)")"""

@dp.message_handler(commands=['meme'])
async def random_letter(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         photo='https://i.imgur.com/aLhAw5a.png',
                         reply_markup=ikb2)

@dp.callback_query_handler()
async def random_callback(callback: types.CallbackQuery):
    match callback.data:
        case 'crandom':
            await callback.message.answer(random.choice(string.ascii_letters))
            await callback.message.delete()
        case 'backstart':
            await help_command(callback.message)
            await callback.message.delete()
"""        case 'idsticker':
            sticker_id = message.sticker.file_id
            await message.answer(f"ID этого стикера - {sticker_id}")"""


@dp.message_handler()
async def answer(message:types.Message):
    await message.answer(text="Я не умею понимать текст пока что, только команды")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


