from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/description')
b2 = KeyboardButton('/random')
b3 = KeyboardButton('/sticker')
b4 = KeyboardButton('/meme')
b5 = KeyboardButton('/start')
kb.add(b1).insert(b2).add(b3).insert(b4)
kb1.add(b5)

ikb1 = InlineKeyboardMarkup(row_width=2)
ikb2 = InlineKeyboardMarkup(row_width=3)
ikb1_1 = InlineKeyboardButton(text="Мой ВК",
                            url='https://vk.com/id_asasin_cross')
ikb1_2 = InlineKeyboardButton(text="Получить рандомную букву",
                              callback_data='crandom')
ikb2_1 = InlineKeyboardButton(text="Зачетная пикча👍",
                              callback_data="like")
ikb2_2 = InlineKeyboardButton(text="Конкретно зачетная пикча😍",
                              callback_data="VeryLike")
ikb2_3 = InlineKeyboardButton(text='👈Вернутся в старт',
                              callback_data='backstart')

ikb1.add(ikb1_1).add(ikb1_2)
ikb2.add(ikb2_1,ikb2_2).add(ikb2_3)
