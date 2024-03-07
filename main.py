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

count = {'count_man_nature': 0, 'count_man_man': 0, 'count_man_tech': 0, 'count_man_sign_system': 0,
         'count_man_artist_image': 0}

big = {'man_nature': man_nature, "man_man": man_man, "man_tech": man_tech, "man_sign_system": man_sign_system,
       "man_artist_image": man_artist_image}

cout = 0


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
                types.InlineKeyboardButton(text='Климов', callback_data="test-klimov")
            ]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def keyboard_test(value, key):
        global value2
        global key2
        global value1
        global key1

        key1 = key
        value1 = value
        key2 = choice(list(big))
        value2 = value_change(key2, big)
        a = [len(x) for x in big.values()]

        global cout
        cout += 1
        print('count: ', cout)
        print('value1 ', value1)
        print('value2: ', value2)






        if value1 == value2 and sum(a) != 1:
            for k in big:
                v_1 = big[k]
                if len(v_1) != 0:
                    print('key1, value1')
                    print(key1, value1)
                    print('----------------')
                    print('key2, value2')
                    print(key2, value2)


                    if value1 == value2:
                        key1 = k
                        value1 = v_1[0]
                    else:
                        break


                    print('res key1, value1')
                    print(key1, value1)
                    print('----------------')
                    print('res key2, value2')
                    print(key2, value2)



        if value1 is None and value2 is None:
            buttons = [
                [
                    types.InlineKeyboardButton(text='Вывести результат', callback_data=f"test-end")
                ],

            ]
            keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
            return keyboard

        if value1 is None or value2 is None:
            if len(big.values()) >= 2:
                if value1 is None:
                    for k in big:
                        v_1 = big[k]
                        if len(v_1) != 0:
                            key1 = k
                            value1 = v_1[0]
                            # big[key1].remove(value1)
                elif value2 is None:
                    for k in big:
                        v_2 = big[k]
                        if len(v_2) != 0 and v_2 != value1:
                            key2 = k
                            value2 = v_2[0]
                            # big[key2].remove(value2)

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

        # elif value2 is None and value1 is None:
        #

        elif value1 is not None and value2 is not None:
            if value1 == value2:
                c_t = 0
                for i in big:
                    v = big[i]
                    for _ in v:
                        c_t += 1
                if c_t == 1:
                    buttons = [
                        [
                            types.InlineKeyboardButton(text='Вывести результат', callback_data=f"test-end")
                        ]
                    ]
                    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
                    return keyboard
            else:
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

    async def end(message: types.Message):
        with suppress(TelegramBadRequest):
            diagram(count)
            await bot.send_photo(message.chat.id, photo=types.FSInputFile('photos/diagram.png'))
            sizes = [int(count['count_man_nature']), int(count['count_man_man']), int(count['count_man_tech']),
                     int(count['count_man_sign_system']), int(count['count_man_artist_image'])]

            c = sum(count.values())

            await message.edit_text(
                'Ваши результаты: \n'
                f'Человек-природа: {round(sizes[0] / (c / 100) if sizes[0] != 0 else 0, 1)}%\n'
                f'Человек-человек: {round(sizes[1] / (c / 100) if sizes[1] != 0 else 0, 1)}%\n'
                f'Человек-техника: {round(sizes[2] / (c / 100) if sizes[2] != 0 else 0, 1)}%\n'
                f'Человек-знаковая система: {round(sizes[3] / (c / 100) if sizes[3] != 0 else 0, 1)}%\n'
                f'Человек-художественный образ: {round(sizes[4] / (c / 100) if sizes[4] != 0 else 0, 1)}%\n'
            )

    async def update_num_text(message: types.Message):
        with suppress(TelegramBadRequest):
            key_1 = choice(list(big))
            value_1 = value_change(key_1, big)
            await message.edit_text(
                f"Какую работу вы предпочтёте?",
                reply_markup=keyboard_test(value_1, key_1)
            )

    @dp.message(Command("start"))
    async def cmd_numbers(message: types.Message):
        user_data[message.from_user.id] = 0
        await message.answer("Выберите тест", reply_markup=get_keyboard(), id='first')

    @dp.callback_query(F.data.startswith("test-"))
    async def callbacks_num(callback: types.CallbackQuery):
        action = callback.data.split("-")[1]
        c = 20

        if action == "klimov":
            await update_num_text(callback.message)

        elif action == 'end':
            await end(callback.message)

        elif action == key1:
            key = key1
            value = value1
            for i in count:
                if i == 'count_' + key and value is not None:
                    count[i] += 1
                    break

            for k in big:
                if value in big[k]:
                    big[k].remove(value)
                elif value2 in big[k]:
                    big[k].remove(value2)

            for x in big.values():
                if len(x) == 0:
                    c -= 1

            if c == 0:
                await end(callback.message)
            await update_num_text(callback.message)

        elif action == key2:

            key = key2

            for i in count:
                if i == 'count_' + key and value2 is not None:
                    count[i] += 1
                    break

            for x in big:
                if value2 in big[x]:
                    big[x].remove(value2)
                elif value1 in big[x]:
                    big[x].remove(value1)

            for j in big.values():
                if len(j) == 0:
                    c -= 1
            if c == 0:
                await end(callback.message)
            await update_num_text(callback.message)

        await callback.answer()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
