from telebot import types, telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from script import TELEGRAM_TOKEN

API_TOKEN = TELEGRAM_TOKEN

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    photo_url = 'https://img.freepik.com/free-photo/3d-illustration-of-academic-hat-with-golden-tassel_107791-16182.jpg'
    bot.send_photo(message.chat.id, photo=photo_url, caption='В наше время среди молодежи остро стоит тема '
                                                             'профориентации. Мой проект направлен на простое и '
                                                             'эргономичное решение этой проблемы. ')
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("25 профессий будущего по версии Forbes", callback_data="but_1"))
    markup.add(InlineKeyboardButton("Тесты на профориентацию", callback_data="but_2"))

    bot.send_message(message.chat.id, text="Ниже представлены инструменты для помощи в профориентации",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def but_pressed(call: types.CallbackQuery):
    markup2 = InlineKeyboardMarkup(row_width=2)
    if call.message:
        if call.data == 'but_1':
            btn1 = types.InlineKeyboardButton("Инженер-композитчик", callback_data="1")
            btn2 = types.InlineKeyboardButton('IT-генетик', callback_data='2')
            btn3 = types.InlineKeyboardButton('Урбанист-эколог', callback_data='3')
            btn4 = types.InlineKeyboardButton('Строитель «умных» дорог ', callback_data='4')
            btn5 = types.InlineKeyboardButton('Оценщик интеллектуальной собственности ', callback_data='5')
            markup2.row(btn1, btn2, btn3)
            markup2.row(btn4, btn5)
            btn6 = types.InlineKeyboardButton('Менеджер краудфандинговых и краудинвестинговых платформ ',
                                              callback_data='6')
            btn7 = types.InlineKeyboardButton('Менеджер космотуризма ', callback_data='7')
            btn8 = types.InlineKeyboardButton('Молекулярный диетолог ', callback_data='8')
            btn9 = types.InlineKeyboardButton('Генетический консультант ', callback_data='9')
            btn10 = types.InlineKeyboardButton('Сити-фермер ', callback_data='10')
            markup2.row(btn6, btn7, btn8)
            markup2.row(btn9, btn10)
            btn11 = types.InlineKeyboardButton('Дизайнер виртуальных миров ', callback_data='11')
            btn12 = types.InlineKeyboardButton('Консультант по здоровой старости ', callback_data='12')
            btn13 = types.InlineKeyboardButton('Прораб-вотчер ', callback_data='13')
            btn14 = types.InlineKeyboardButton('Экопроповедник ', callback_data='14')
            btn15 = types.InlineKeyboardButton('Специалист по преодолению системных экологических катастроф ',
                                               callback_data='15')
            markup2.row(btn11, btn12, btn13)
            markup2.row(btn14, btn15)
            btn16 = types.InlineKeyboardButton('IT-медик ', callback_data='16')
            btn17 = types.InlineKeyboardButton('Космобиолог и космогеолог ', callback_data='17')
            btn18 = types.InlineKeyboardButton('Проектировщик «умной» среды ', callback_data='18')
            btn19 = types.InlineKeyboardButton('Сетевой юрист ', callback_data='19')
            btn20 = types.InlineKeyboardButton('Мультивалютный переводчик ', callback_data='20')
            markup2.row(btn16, btn17, btn18)
            markup2.row(btn19, btn20)
            btn21 = types.InlineKeyboardButton('Проектировщик медицинских роботов ', callback_data='21')
            btn22 = types.InlineKeyboardButton('Электрозаправщик ', callback_data='22')
            btn23 = types.InlineKeyboardButton('Проектировщик 3D-печати в строительстве ', callback_data='23')
            btn24 = types.InlineKeyboardButton('Системный горный инженер ', callback_data='24')
            btn25 = types.InlineKeyboardButton('Цифровой лингвист ', callback_data='25')
            back = types.InlineKeyboardButton('Вернутся в меню', callback_data='back')
            markup2.row(btn21, btn22, btn23)
            markup2.row(btn24, btn25)
            markup2.row(back)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text="Какие специалисты будут востребованы через 15-20 лет? Бизнес-школа «Сколково» "
                                       "и Агентство стратегических инициатив выпустили «Атлас новых профессий», "
                                       "25 из которых отобрал Forbes\nНиже представлен список ",
                                  reply_markup=markup2)
        elif call.data == 'but_2':
            item1 = types.InlineKeyboardButton('Тест Климова', callback_data='Klimov')
            item2 = types.InlineKeyboardButton('Тест Голланда', callback_data='Holland')
            back = types.InlineKeyboardButton('Вернутся в меню', callback_data='back')
            markup2.add(item1, item2, back)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='⠀Выбрать тест⠀'.rjust(18).ljust(18), reply_markup=markup2)

    if call.message:
        if call.data == '1':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='\u0418\u043d\u0436\u0435\u043d\u0435\u0440\u002d\u043a\u043e\u043c\u043f\u043e\u0437\u0438\u0442\u0447\u0438\u043a\u003a\u000a\u041f\u043e\u0434\u0431\u0438\u0440\u0430\u0435\u0442\u0020\u043a\u043e\u043c\u043f\u043e\u0437\u0438\u0442\u043d\u044b\u0435\u0020\u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b\u0020\u0434\u043b\u044f\u0020\u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u0430\u002c\u0020\u0432\u0020\u0442\u043e\u043c\u0020\u0447\u0438\u0441\u043b\u0435\u0020\u0441\u0020\u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435\u043c\u0020\u0033\u0044\u002d\u043f\u0435\u0447\u0430\u0442\u0438\u002c\u0020\u0440\u043e\u0431\u043e\u0442\u043e\u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0445\u0020\u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0020\u0441\u0020\u0437\u0430\u0434\u0430\u043d\u043d\u044b\u043c\u0438\u0020\u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0430\u043c\u0438\u002e\u000a\u0413\u0434\u0435\u0020\u0443\u0447\u0438\u0442\u044c\u0441\u044f\u003a\u000a\u2022\u0020\u041c\u043e\u0441\u043a\u043e\u0432\u0441\u043a\u0438\u0439\u0020\u0444\u0438\u0437\u0438\u043a\u043e\u002d\u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439\u0020\u0438\u043d\u0441\u0442\u0438\u0442\u0443\u0442\u000a\u2022\u0020\u0422\u043e\u043c\u0441\u043a\u0438\u0439\u0020\u0433\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439\u0020\u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442\u000a\u2022\u0020\u041d\u0430\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0439\u0020\u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0439\u0020\u044f\u0434\u0435\u0440\u043d\u044b\u0439\u0020\u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442\u0020\u00ab\u041c\u0418\u0424\u0418\u00bb\u000a\u2022\u0020\u041d\u0430\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0439\u0020\u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0439\u000a\u2022\u0020\u0422\u043e\u043c\u0441\u043a\u0438\u0439\u0020\u043f\u043e\u043b\u0438\u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439\u0020\u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442\u000a\u2022\u0020\u0421\u0430\u043d\u043a\u0442\u002d\u041f\u0435\u0442\u0435\u0440\u0431\u0443\u0440\u0433\u0441\u043a\u0438\u0439\u0020\u043d\u0430\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0439\u0020\u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0439\u0020\u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442\u0020\u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0445\u0020\u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0439\u002c\u0020\u043c\u0435\u0445\u0430\u043d\u0438\u043a\u0438\u0020\u0438\u0020\u043e\u043f\u0442\u0438\u043a\u0438\u0020\u000a\u2022\u0020\u041c\u043e\u0441\u043a\u043e\u0432\u0441\u043a\u0438\u0439\u0020\u0433\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439\u0020\u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439\u0020\u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442\u0020\u0440\u0430\u0434\u0438\u043e\u0442\u0435\u0445\u043d\u0438\u043a\u0438\u002c\u0020\u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u0438\u043a\u0438\u0020\u0438\u0020\u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u043a\u0438\u0020\u000a\u2022\u0020\u0414\u0430\u043b\u044c\u043d\u0435\u0432\u043e\u0441\u0442\u043e\u0447\u043d\u044b\u0439\u0020\u0444\u0435\u0434\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439\u0020\u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442',
                                  reply_markup=spes)
        elif call.data == '2':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='IT-генетик:\nПрограммирует геном для лечения наследственных заболеваний и генетических проблем у детей.\nГде учиться:\n• РНИМУ им. Пирогова\n• Московский государственный медицинский университет им. Сеченова \n• Санкт-Петербургский государственный медицинский университет им. Павлова \n• Нижегородская государственная медицинская академия \n• Новосибирская государственная медицинская академия \n• Смоленская государственная медицинская академия\n• Кубанская государственная медицинская академия',
                                  reply_markup=spes)
        elif call.data == '3':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Урбанист-эколог:\nПроектирует новые экологически чистые города.\nГде учиться:\n• Томский политехнический университет\n• Московский государственный университет\n• Санкт-Петербургский государственный университет\n• Северный (Арктический) федеральный университет\n• Удмуртский государственный университет\n• Дальневосточный государственный технический рыбохозяйственный университет\n• Российский государственный аграрный университет — МСХА им. Тимирязева ',
                                  reply_markup=spes)
        elif call.data == '4':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Строитель «умных» дорог:\nВыбирает и устанавливает «умное» дорожное покрытие с датчиками контроля состояния дороги, а также «умные» знаки, разметку и системы видеонаблюдения.\nГде учиться:\n• Московский государственный университет путей сообщения\n• Московский государственный технологический университет \n• Дальневосточный государственный университет путей сообщения\n• Московский автомобильно-дорожный институт\n• Московский государственный институт электроники и математики\n• Сибирский федеральный университет\n• Ижевский государственный технический университет им. Калашникова ',
                                  reply_markup=spes)
        elif call.data == '5':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Оценщик интеллектуальной собственности:\nОпределяет стоимость нематериальных активов: идеи, изобретения, бизнес-модели и т. п.\nГде учиться:\n• Высшая школа экономики\n• Российский экономический университет им. Плеханова\n• Финансовая академия при правительстве РФ\n• Российская академия народного хозяйства и государственной службы при президенте РФ\n• Санкт-Петербургский государственный университет\n• Московский государственный университет экономики, статистики и информатики ',
                                  reply_markup=spes)
        elif call.data == '6':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Менеджер краудфандинговых и краудинвестинговых платформ:\nОрганизует работу краудфандинговых платформ, предварительно оценивает проекты для краудфандингового финансирования, разбирает конфликты между вкладчиками и авторами проектов.\nГде учиться:\n• Высшая школа экономики\n• Российский экономический университет им. Плеханова\n• Финансовая академия при правительстве РФ\n• Российская академия народного хозяйства и государственной службы при президенте РФ\n• Санкт-Петербургский государственный университет\n• Московский государственный университет экономики, статистики и информатики ',
                                  reply_markup=spes)
        elif call.data == '7':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Менеджер космотуризма:\nБудет разрабатывать туристические программы в околокосмическое пространство, а позднее — на лунные базы и другие космические сооружения.\nГде учиться:\n• Московский авиационный институт \n• Краснодарское высшее военное авиационное училище летчиков (военный институт) им. Серова\n• Московский государственный технический университет им. Баумана \n• Сибирский государственный аэрокосмический университет им. Решетнева\n• Санкт-Петербургский государственный университет аэрокосмического приборостроения',
                                  reply_markup=spes)
        elif call.data == '8':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Молекулярный диетолог:\nДиетолог, разрабатывающий индивидуальную схему питания исходя из молекулярного состава пищи и результатов генетического анализа человека.\nГде учиться:\n• РНИМУ им. Пирогова\n• Московский государственный медицинский университет им. Сеченова \n• Санкт-Петербургский государственный медицинский университет им. Павлова \n• Нижегородская государственная медицинская академия \n• Новосибирская государственная медицинская академия \n• Смоленская государственная медицинская академия \n• Кубанская государственная медицинская академия ',
                                  reply_markup=spes)
        elif call.data == '9':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Генетический консультант:\nСпециалист по генетическому анализу. Анализирует данные, полученные с диагностических устройств, дает заключение и рекомендации по дальнейшей схеме лечения.\nГде учиться:\n• РНИМУ им. Пирогова\n• Московский государственный медицинский университет им. Сеченова \n• Санкт-Петербургский государственный медицинский университет им. Павлова \n• Нижегородская государственная медицинская академия\n• Новосибирская государственная медицинская академия \n• Смоленская государственная медицинская академия \n• Кубанская государственная медицинская академия ',
                                  reply_markup=spes)
        elif call.data == '10':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Сити-фермер:\nВыращивает овощи и фрукты на крышах и стенах небоскребов.\nГде учиться:\n• Томский политехнический университет\n• Московский государственный университет\n• Санкт-Петербургский государственный университет\n• Северный (Арктический) федеральный университет\n• Удмуртский государственный университет\n• Дальневосточный государственный технический рыбохозяйственный университет\n• Российский государственный аграрный университет — МСХА им. Тимирязева ',
                                  reply_markup=spes)
        elif call.data == '11':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Дизайнер виртуальных миров:\nСоздает виртуальные миры со своей природой, архитектурой и своими законами.\nГде учиться:\n• Московский государственный университет\n• Московский физико-технический институт \n• Санкт-Петербургский национальный исследовательский университет информационных технологий, механики и оптики \n• Национальный исследовательский ядерный университет \n• Национальный исследовательский Томский политехнический университет \n• Новосибирский национальный исследовательский государственный университет \n• Нижегородский государственный технический университет им. Алексеева \n• Московский технический университет связи и информатики \n• Московский государственный технический университет радиотехники, электроники и автоматики ',
                                  reply_markup=spes)
        elif call.data == '12':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Консультант по здоровой старости:\nРазрабатывает оптимальные физические нагрузки, образ жизни и систему питания для пожилых людей.\nГде учиться:\n• РНИМУ им. Пирогова\n• Московский государственный медицинский университет им. Сеченова \n• Санкт-Петербургский государственный медицинский университет им. Павлова \n• Нижегородская государственная медицинская академия \n• Новосибирская государственная медицинская академия \n• Смоленская государственная медицинская академия \n• Кубанская государственная медицинская академия ',
                                  reply_markup=spes)
        elif call.data == '13':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Прораб-вотчер:\nСпециалист по строительству, который оценивает и, если нужно, корректирует ход строительства с помощью цифровых проектов зданий.\nГде учиться:\n• Московский архитектурный институт \n• Московский государственный строительный университет\n• Южный федеральный университет\n• Дальневосточный государственный технический университет им. Куйбышева \n• Санкт-Петербургский государственный архитектурно-строительный университет \n• Уральский федеральный университет им. Ельцина\n• Нижегородский государственный архитектурно-строительный университет\n• Курсы при центрах коллективного пользования / фаблабы (места, где обучают технологиям 3D-принтинга)',
                                  reply_markup=spes)
        elif call.data == '14':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Экопроповедник:\nПроповедует экологически осознанный образ жизни, проводит образовательные программы для детей и взрослых.\nГде получить базовое образование:\n• Московский государственный университет\n• Томский государственный университет\n• Санкт-Петербургский государственный университет\n• Дальневосточный федеральный университет\n• Московский государственный технический университет им. Баумана\n• Томский политехнический университет\n• Национальный исследовательский ядерный университет МИФИ\n• Новосибирский государственный технический университет\n• Московский государственный технологический университет',
                                  reply_markup=spes)
        elif call.data == '15':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Специалист по преодолению системных экологических катастроф:\nПредотвращает катастрофы, которые осознаются людьми постепенно: загрязнение вокруг промышленных центров, радиационные свалки, тающие ледники.\nГде учиться:\n• Московский государственный университет\n• Томский государственный университет\n• Санкт-Петербургский государственный университет\n• Дальневосточный федеральный университет\n• Московский государственный технический университет им. Баумана \n• Томский политехнический университет \n• Национальный исследовательский ядерный университет МИФИ\n• Новосибирский государственный технический университет \n• Московский государственный технологический университет ',
                                  reply_markup=spes)
        elif call.data == '16':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='IT-медик:\nСпециалист со знанием IT, который создает и управляет базами физиологических данных пациентов, а также проектирует программное обеспечение для лечебного и диагностического оборудования.\nГде учиться:\n• РНИМУ им. Пирогова\n• Московский государственный медицинский университет им. Сеченова \n• Санкт-Петербургский государственный медицинский университет им. Павлова \n• Нижегородская государственная медицинская академия \n• Новосибирская государственная медицинская академия \n• Смоленская государственная медицинская академия \n• Кубанская государственная медицинская академия ',
                                  reply_markup=spes)
        elif call.data == '17':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Космобиолог и космогеолог:\nКосмобиолог исследует, как ведут себя организмы в космосе, происходят ли генные изменения, и создает экосистемы для орбитальных станций и лунных баз. Космогеолог занимается разведкой и добычей полезных ископаемых на Луне и астероидах.\nГде учиться:\n• Московский авиационный институт\n• Краснодарское высшее военное авиационное училище летчиков (военный институт) им. Серова\n• Московский государственный технический\n• Московский государственный технический университет им. Баумана \n• Сибирский государственный аэрокосмический университет им. Решетнева\n• Санкт-Петербургский государственный университет аэрокосмического приборостроения ',
                                  reply_markup=spes)
        elif call.data == '18':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Проектировщик «умной» среды:\nСоздает программные и технологические решения, позволяющие домам и офисам реагировать на запросы пользователей.\nГде учиться:\n• Московский физико-технический институт \n• Национальный исследовательский технологический университет «МИСиС»\n• Российский химико-технологический университет им. Менделеева \n• Национальный исследовательский Томский политехнический университет \n• Московская государственная академия тонкой химической технологии им. Ломоносова \n• Санкт-Петербургский государственный политехнический университет\n• Нижегородский государственный университет им. Лобачевского \n• Уральский федеральный университет им. Ельцина',
                                  reply_markup=spes)
        elif call.data == '19':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Сетевой юрист:\nРазрабатывает законодательство для виртуального мира и сетей, а также разбирается в вопросах защиты виртуальной собственности.\nГде учиться:\n• Факультет вычислительной математики и кибернетики Московского государственного университета\n• Московский физико-технический институт\n• Санкт-Петербургский национальный исследовательский университет информационных технологий, механики и оптики\n• Национальный исследовательский ядерный университет «МИФИ»\n• Томский политехнический университет\n• Новосибирский национальный исследовательский государственный университет\n• Томский государственный университет\n• Нижегородский государственный технический университет им. Алексеева\n• Московский технический университет связи и информатики\n• Московский государственный технический университет радиотехники, электроники и автоматики ',
                                  reply_markup=spes)
        elif call.data == '20':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Мультивалютный переводчик:\nОрганизует систему обмена и взаиморасчета традиционных и альтернативных, например электронных, валют.\nГде учиться:\n• Национальный исследовательский университет «Высшая школа экономики» \n• Российский экономический университет им. Плеханова\n• Финансовая академия при правительстве РФ\n• Российская академия народного хозяйства и государственной службы при президенте РФ\n• Санкт-Петербургский государственный университет\n• Московский государственный университет экономики, статистики и информатики ',
                                  reply_markup=spes)
        elif call.data == '21':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Проектировщик медицинских роботов:\nСпециалист, проектирующий роботов и киберустройства для медицины: диагностические роботы, роботы-хирурги, киберпротезы.\nГде учиться:\n• Московский физико-технический институт \n• Национальный исследовательский Томский государственный университет \n• Национальный исследовательский ядерный университет «МИФИ»\n• Национальный исследовательский Томский политехнический университет \n• Санкт-Петербургский национальный исследовательский университет информационных технологий, механики и оптики \n• Московский государственный технический университет радиотехники, электроники и автоматики \n• Дальневосточный федеральный университет',
                                  reply_markup=spes)
        elif call.data == '22':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Электрозаправщик:\nОбслуживает заправки для электротранспорта.\nГде учиться:\n• Московский энергетический институт\n• Томский политехнический университет\n• Новосибирский государственный технический университет\n• Санкт-Петербургский политехнический университет',
                                  reply_markup=spes)
        elif call.data == '23':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Проектировщик 3D-печати в строительстве:\nПроектирует макеты конструкций и подбирает наилучшие компоненты для их печати.\nГде учиться:\n• Московский архитектурный институт\n• Национальный исследовательский университет — Московский государственный строительный университет\n• Южный федеральный университет\n• Дальневосточный государственный технический университет им. Куйбышева\n• Санкт-Петербургский государственный архитектурно-строительный университет\n• Уральский федеральный университет им. Ельцина\n• Нижегородский государственный архитектурно-строительный университет\n• Курсы при центрах коллективного пользования / фаблабы (места, где обучают технологиям 3D-принтинга)',
                                  reply_markup=spes)
        elif call.data == '24':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Системный горный инженер:\nПолностью контролирует разработку месторождений: от поисково-разведочных работ до закрытия месторождения.\nГде учиться:\n• Российский государственный университет нефти и газа им. Губкина\n• Дальневосточный федеральный университет\n• Санкт-Петербургский государственный горный институт им. Плеханова\n• Сибирский федеральный университет\n• Российский государственный геологоразведочный университет им. Орджоникидзе\n• Уральский федеральный университет им. Ельцина\n• Северо-Восточный федеральный университет им. Аммосова',
                                  reply_markup=spes)
        elif call.data == '25':
            spes = InlineKeyboardMarkup(row_width=2)
            specials = types.InlineKeyboardButton('Вернутся к профессиям', callback_data='specials')
            spes.add(specials)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Цифровой лингвист:\nРазрабатывает лингвистические системы семантического перевода (перевода с учетом контекста и смысла), обработки текстовой информации (в том числе семантический поиск в интернете) и новые интерфейсы общения между человеком и компьютером на естественных языках.\nГде учиться:\n• Московский государственный университет\n• Московский физико-технический институт\n• Санкт-Петербургский национальный исследовательский университет информационных  технологий, механики и оптики\n• Национальный исследовательский ядерный университет «МИФИ»\n• Томский политехнический университет\n• Новосибирский национальный исследовательский государственный университет\n• Томский государственный университет\n• Нижегородский государственный технический университет им. Алексеева\n• Московский технический университет связи и информатики\n• Московский государственный технический университет радиотехники, электроники и автоматики ',
                                  reply_markup=spes)

    if call.message:
        if call.data == 'Klimov':
            d = InlineKeyboardMarkup(row_width=2)
            oe = types.InlineKeyboardButton('Тест Климова', url='https://postupi.online/test/klimova/',
                                            callback_data='tr')
            by = types.InlineKeyboardButton('Вернутся к тестам', callback_data='b')
            d.row(oe)
            d.row(by)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Ссылка на тест',
                                  reply_markup=d)
        elif call.data == 'Holland':
            d = InlineKeyboardMarkup(row_width=2)
            oe = types.InlineKeyboardButton('Тест Голланда', url='https://postupi.online/test/gollanda/',
                                            callback_data='tr')
            by = types.InlineKeyboardButton('Вернутся к тестам', callback_data='b')
            d.row(oe)
            d.row(by)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Ссылка на тест',
                                  reply_markup=d)

    if call.data == 'b':
        item1 = types.InlineKeyboardButton('Тест Климова', callback_data='Klimov')
        item2 = types.InlineKeyboardButton('Тест Голланда', callback_data='Holland')
        back = types.InlineKeyboardButton('Вернутся в меню', callback_data='back')
        markup2.add(item1, item2, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text='⠀⠀⠀⠀⠀Выбрать тест⠀⠀⠀⠀⠀'.rjust(18).ljust(18), reply_markup=markup2)

    if call.message:
        if call.data == 'back':
            markup = InlineKeyboardMarkup(row_width=2)
            markup.add(InlineKeyboardButton("25 профессий будущего по версии Forbes", callback_data="but_1"))
            markup.add(InlineKeyboardButton("Тесты на профориентацию", callback_data="but_2"))

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Ниже представлены инструменты для помощи в профориентации', reply_markup=markup)

    if call.message:
        if call.data == 'specials':
            btn1 = types.InlineKeyboardButton("Инженер-композитчик", callback_data="1")
            btn2 = types.InlineKeyboardButton('IT-генетик', callback_data='2')
            btn3 = types.InlineKeyboardButton('Урбанист-эколог', callback_data='3')
            btn4 = types.InlineKeyboardButton('Строитель «умных» дорог ', callback_data='4')
            btn5 = types.InlineKeyboardButton('Оценщик интеллектуальной собственности ', callback_data='5')
            markup2.row(btn1, btn2, btn3)
            markup2.row(btn4, btn5)
            btn6 = types.InlineKeyboardButton('Менеджер краудфандинговых и краудинвестинговых платформ ',
                                              callback_data='6')
            btn7 = types.InlineKeyboardButton('Менеджер космотуризма ', callback_data='7')
            btn8 = types.InlineKeyboardButton('Молекулярный диетолог ', callback_data='8')
            btn9 = types.InlineKeyboardButton('Генетический консультант ', callback_data='9')
            btn10 = types.InlineKeyboardButton('Сити-фермер ', callback_data='10')
            markup2.row(btn6, btn7, btn8)
            markup2.row(btn9, btn10)
            btn11 = types.InlineKeyboardButton('Дизайнер виртуальных миров ', callback_data='11')
            btn12 = types.InlineKeyboardButton('Консультант по здоровой старости ', callback_data='12')
            btn13 = types.InlineKeyboardButton('Прораб-вотчер ', callback_data='13')
            btn14 = types.InlineKeyboardButton('Экопроповедник ', callback_data='14')
            btn15 = types.InlineKeyboardButton('Специалист по преодолению системных экологических катастроф ',
                                               callback_data='15')
            markup2.row(btn11, btn12, btn13)
            markup2.row(btn14, btn15)
            btn16 = types.InlineKeyboardButton('IT-медик ', callback_data='16')
            btn17 = types.InlineKeyboardButton('Космобиолог и космогеолог ', callback_data='17')
            btn18 = types.InlineKeyboardButton('Проектировщик «умной» среды ', callback_data='18')
            btn19 = types.InlineKeyboardButton('Сетевой юрист ', callback_data='19')
            btn20 = types.InlineKeyboardButton('Мультивалютный переводчик ', callback_data='20')
            markup2.row(btn16, btn17, btn18)
            markup2.row(btn19, btn20)
            btn21 = types.InlineKeyboardButton('Проектировщик медицинских роботов ', callback_data='21')
            btn22 = types.InlineKeyboardButton('Электрозаправщик ', callback_data='22')
            btn23 = types.InlineKeyboardButton('Проектировщик 3D-печати в строительстве ', callback_data='23')
            btn24 = types.InlineKeyboardButton('Системный горный инженер ', callback_data='24')
            btn25 = types.InlineKeyboardButton('Цифровой лингвист ', callback_data='25')
            back = types.InlineKeyboardButton('Вернутся в меню', callback_data='back')
            markup2.row(btn21, btn22, btn23)
            markup2.row(btn24, btn25)
            markup2.row(back)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text="Какие специалисты будут востребованы через 15-20 лет? Бизнес-школа «Сколково» и Агентство стратегических инициатив выпустили «Атлас новых профессий», 25 из которых отобрал Forbes\nНиже представлен список ",
                                  reply_markup=markup2)


if __name__ == '__main__':
    bot.infinity_polling(skip_pending=True)
