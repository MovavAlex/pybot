import asyncio
import logging
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from diagram import diagram
from ques import man_nature, man_man, man_tech, man_sign_system, man_artist_image
from script import TELEGRAM_TOKEN
from random import choice
from db import db_start, give_info, get_count, get_big, change_count, change_big, del_user


def value_change(key, arr):
    try:
        t = (i for i in arr[key])
        value = next(t)
        return value
    except StopIteration or KeyError:
        pass


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TELEGRAM_TOKEN, parse_mode="HTML")
# Диспетчер
dp = Dispatcher()


async def main():
    user_data = {}

    def get_keyboard():

        buttons = [
            [
                types.InlineKeyboardButton(text='Начать', callback_data="test-klimov")
            ]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def keyboard_test(value, key, big, userID):

        key1 = key
        value1 = value
        key2 = choice(list(big))
        value2 = value_change(key2, big)
        a = [len(x) for x in big.values()]
        user_data[f'key1_{userID}'] = key1
        user_data[f'key2_{userID}'] = key2
        user_data[f'value1_{userID}'] = value1
        user_data[f'value2_{userID}'] = value2

        # Проверка на одинаковые вопросы
        if value1 == value2 and sum(a) != 1 and value1 is not None and value2 is not None:
            n_big = big.copy()
            del n_big[key1]
            b = [len(x) for x in n_big.values()]
            for k in n_big:
                v_2 = n_big[k]
                if len(v_2) != 0 and sum(b) != 0:
                    key2 = k
                    value2 = v_2[0]
                    user_data[f'key2_{userID}'] = key2
                    user_data[f'value2_{userID}'] = value2

                else:
                    v_2 = big[key1]
                    for i in v_2:
                        if i != value1:
                            value2 = i
                            user_data[f'value2_{userID}'] = value2

        # Проверка на значение None у обоих вопросов
        if value1 is None and value2 is None and sum(a) == 0:
            buttons = [
                [
                    types.InlineKeyboardButton(text='Вывести результат', callback_data=f"test-end")
                ],

            ]
            keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
            return keyboard

        # Проверка на значение None у одного из вопросов
        elif value1 is None or value2 is None:

            print('value1 or 2 is None')
            a = [len(x) for x in big.values()]

            if sum(a) >= 2:
                if value1 is None:
                    for k1 in big:
                        v_1 = big[k1]
                        if len(v_1) == sum(a):
                            key1 = k1
                            value1 = v_1[0]
                            key2 = k1
                            value2 = v_1[1]

                            user_data[f'key1_{userID}'] = key1
                            user_data[f'key2_{userID}'] = key2
                            user_data[f'value1_{userID}'] = value1
                            user_data[f'value2_{userID}'] = value2

                        elif len(v_1) != 0 and value2 not in v_1:
                            key1 = k1
                            value1 = choice(v_1)
                            user_data[f'key1_{userID}'] = key1
                            user_data[f'value1_{userID}'] = value1

                if value2 is None:
                    for k2 in big:
                        v_2 = big[k2]
                        if len(v_2) == sum(a):
                            key1 = k2
                            value1 = v_2[0]
                            key2 = k2
                            value2 = v_2[1]

                            user_data[f'key1_{userID}'] = key1
                            user_data[f'key2_{userID}'] = key2
                            user_data[f'value1_{userID}'] = value1
                            user_data[f'value2_{userID}'] = value2

                        elif len(v_2) != 0 and value1 not in v_2:
                            key2 = k2
                            value2 = choice(v_2)
                            user_data[f'key2_{userID}'] = key2
                            user_data[f'value2_{userID}'] = value2
            else:
                buttons = [
                    [
                        types.InlineKeyboardButton(text='Вывести результат', callback_data=f"test-end")

                    ],

                ]
                keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
                return keyboard

            buttons = [
                [
                    types.InlineKeyboardButton(text=str(value1), callback_data=f"test-{key1}")
                ],
                [
                    types.InlineKeyboardButton(text=str(value2), callback_data=f"test-{key2}")
                ]

            ]
            keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
            return keyboard

        elif value1 is not None and value2 is not None:
            buttons = [
                [
                    types.InlineKeyboardButton(text=str(value1), callback_data=f"test-{key1}")
                ],
                [
                    types.InlineKeyboardButton(text=str(value2), callback_data=f"test-{key2}")
                ]

            ]
            keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
            return keyboard

    async def end(message: types.Message, count, userID):
        with suppress(TelegramBadRequest):
            diagram(count, userID)
            await bot.send_photo(message.chat.id, photo=types.FSInputFile(f'photos/{userID}.png'))
            await message.edit_text('Ваши результаты: \n')
            await del_user(userID)

    async def update_num_text(message: types.Message, big, userID):
        with suppress(TelegramBadRequest):
            key_1 = choice(list(big))
            value_1 = value_change(key_1, big)
            await message.edit_text(
                f"Какую работу вы предпочтёте?",
                reply_markup=keyboard_test(value_1, key_1, big, userID)
            )

    @dp.message(Command("start"))
    async def cmd_numbers(message: types.Message):

        user_ID = message.from_user.id
        print('useridstart: ', user_ID)
        start_count = {'count_man_nature': 0, 'count_man_man': 0, 'count_man_tech': 0, 'count_man_sign_system': 0,
                       'count_man_artist_image': 0}

        start_big = {'man_nature': man_nature, "man_man": man_man, "man_tech": man_tech,
                     "man_sign_system": man_sign_system,
                     "man_artist_image": man_artist_image}

        await db_start()

        await give_info(user_ID, start_count, start_big)

        msg = await message.answer_photo(
            photo='https://img.freepik.com/free-photo/3d-illustration-of-academic-hat-with-golden-tassel_107791-16182'
                  '.jpg',
            caption='В наше время среди молодежи остро стоит тема '
                    'профориентации. Мой проект направлен на простое и '    
                    'эргономичное решение этой проблемы.', id='photography')
        await message.answer("Предлагаю пройти тест по профориентации", reply_markup=get_keyboard(), id='first')
        await asyncio.sleep(5)
        try:
            await msg.delete()
        except Exception as _:
            pass

    @dp.callback_query(F.data.startswith("test-"))
    async def callbacks_num(callback: types.CallbackQuery):

        action = callback.data.split("-")[1]
        c = 20

        userid = callback.from_user.id
        try:
            key1 = user_data[f'key1_{userid}']
            key2 = user_data[f'key2_{userid}']
            value1 = user_data[f'value1_{userid}']
            value2 = user_data[f'value2_{userid}']
            print('k1: ', key1, value1)
            print('k2: ', key2, value2)
        except KeyError:
            key1 = None
            value1 = None
            key2 = None
            value2 = None
        print('useridcallback: ', userid)

        print('useridcallback: ', userid)

        if action == "klimov":
            big = await get_big(userid)
            print('big: ', big)

            await update_num_text(callback.message, big, userid)

        elif action == 'end':
            count = await get_count(userid)
            await end(callback.message, count, userid)

        elif action == key1:
            count = await get_count(userid)
            big = await get_big(userid)

            key = key1
            value = value1
            for i in count:
                if i == 'count_' + key and value is not None:
                    count[i] += 1
                    await change_count(userid, count)
                    break

            for k in big:
                if value1 in big[k]:
                    big[k].remove(value1)
                    await change_big(userid, big)

                elif value2 in big[k]:
                    big[k].remove(value2)
                    await change_big(userid, big)

            for x in big.values():
                if len(x) == 0:
                    c -= 1

            if c == 0:
                count = get_count(userid)

                await end(callback.message, count, userid)
            await update_num_text(callback.message, big, userid)

        elif action == key2:
            count = await get_count(userid)
            big = await get_big(userid)

            key = key2

            for i in count:
                if i == 'count_' + key and value2 is not None:
                    count[i] += 1
                    await change_count(userid, count)
                    break

            for x in big:
                if value2 in big[x]:
                    big[x].remove(value2)
                    await change_big(userid, big)
                elif value1 in big[x]:
                    big[x].remove(value1)
                    await change_big(userid, big)

            for j in big.values():
                if len(j) == 0:
                    c -= 1
            if c == 0:
                await end(callback.message, count, userid)
            await update_num_text(callback.message, big, userid)

        await callback.answer()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
