import telebot
import json
from telebot import types
from random import randint
TOKEN = ""
bot = telebot.TeleBot(TOKEN)
STATE_MENU = "menu"
STATE_BISHKEK = "bishkek"
STATE_ALMATY = "almaty"
STATE_ASTANA = "astana"
STATE_MOSCOW = "Moscow"
user_states = {}
@bot.message_handler(commands=['start', 'назад'])
def send_greeting(message):
    user_states[message.chat.id] = STATE_MENU
    photo_path = '/Users/baielmangmail.com/Documents/2024-02-16 01.14.55.jpg'
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn2 = types.KeyboardButton('Просмотреть курсы в Бишкеке')
    btn3 = types.KeyboardButton('Просмотреть курсы в Алматы')
    btn4 = types.KeyboardButton('Просмотреть курсы в Астане')
    # btn7 = types.KeyboardButton('Просмотреть курсы в Москве')
    btn5 = types.KeyboardButton('donat')
    btn6 = types.KeyboardButton('Купить премиум версию')
    markup.add( btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, 'Добро пожаловать!\nЯ могу вам порекомендовать Языковые курсы', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def choose_mode(message):
    if message.text == 'Просмотреть курсы в Бишкеке' or  message.text =='Просмотреть другие курсы в Бишкеке':
        user_states[message.chat.id] = STATE_BISHKEK
        with open('bishkek.json', 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
        i = randint(0, 55)
        dish = data[i]
        title = dish.get('title')
        phone = dish.get('phone')
        link = dish.get('link')
        address = dish.get('address')
        if phone:
            bot.send_message(message.chat.id, text=title)
            bot.send_message(message.chat.id, text=phone)
            bot.send_message(message.chat.id, text=link)
            bot.send_message(message.chat.id, text=address)
            markup = types.ReplyKeyboardMarkup(row_width=1)
            btn3 = types.KeyboardButton('Просмотреть другие курсы в Бишкеке')
            btn5 = types.KeyboardButton('/назад')
            markup.add(btn3,btn5)
            bot.send_message(message.chat.id, text='Выберите следующее действие', reply_markup=markup)
    elif message.text == 'Просмотреть курсы в Алматы' or message.text == 'Просмотреть другие курсы в Алматы':
        user_states[message.chat.id] = STATE_ALMATY 
        with open('almaty.json', 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
        i = randint(0, 170)
        dish = data[i]
        title = dish.get('title')
        phone = dish.get('phone')
        link = dish.get('link')
        address = dish.get('address')
        if phone:
            bot.send_message(message.chat.id, text=title)
            bot.send_message(message.chat.id, text=phone)
            bot.send_message(message.chat.id, text=link)
            bot.send_message(message.chat.id, text=address)
            markup = types.ReplyKeyboardMarkup(row_width=1)
            btn3 = types.KeyboardButton('Просмотреть другие курсы в Алматы')
            btn5 = types.KeyboardButton('/назад')
            markup.add(btn3,btn5)
            bot.send_message(message.chat.id,text='Выберите следующее действие', reply_markup=markup)
    elif message.text == 'Просмотреть курсы в Астане' or message.text == 'Просмотреть другие курсы в Астане':
        user_states[message.chat.id] = STATE_ASTANA
        with open('astana.json', 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
        i = randint(0, 180)
        dish = data[i]
        title = dish.get('title')
        phone = dish.get('phone')
        link = dish.get('link')
        address = dish.get('address')
        if phone:
            bot.send_message(message.chat.id, text=title)
            bot.send_message(message.chat.id, text=phone)
            bot.send_message(message.chat.id, text=link)
            bot.send_message(message.chat.id, text=address)
            markup = types.ReplyKeyboardMarkup(row_width=1)
            btn3 = types.KeyboardButton('Просмотреть другие курсы в Астане')
            btn5 = types.KeyboardButton('Назад')
            markup.add(btn3,btn5)
            bot.send_message(message.chat.id,text='Выберите следующее действие', reply_markup=markup)
    elif message.text == 'Просмотреть курсы в Москве' or message.text == 'Просмотреть другие курсы в Москвы':
        user_states[message.chat.id] = STATE_MOSCOW
        with open('moscow.json', 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
        i = randint(0, 27)
        dish = data[i]
        title = dish.get('title')
        phone = dish.get('phone')
        link = dish.get('link')
        address = dish.get('address')
        if phone:
            bot.send_message(message.chat.id, text=title)
            bot.send_message(message.chat.id, text=phone)
            bot.send_message(message.chat.id, text=link)
            bot.send_message(message.chat.id, text=address)
            markup = types.ReplyKeyboardMarkup(row_width=1)
            btn3 = types.KeyboardButton('Просмотреть другие курсы в Москвы')
            btn5 = types.KeyboardButton('Назад')
            markup.add(btn3,btn5)
            bot.send_message(message.chat.id,text='Выберите следующее действие', reply_markup=markup)
    elif message.text == 'donat':
        bot.send_message(message.chat.id, f'Mbank:{770200017},\n            {755444385}')
    elif message.text == 'Купить премиум версию':
        bot.send_message(message.chat.id, 'Еще в разработке.....')
    elif message.text == 'Назад':
        current_state = user_states.get(message.chat.id, STATE_MENU)
        if current_state == STATE_MENU:
            send_greeting(message)
        elif current_state == STATE_BISHKEK:
            user_states[message.chat.id] = STATE_MENU
            send_greeting(message)
        elif current_state == STATE_ALMATY:
            user_states[message.chat.id] = STATE_MENU
            send_greeting(message)
        elif current_state == STATE_ASTANA:
            user_states[message.chat.id] = STATE_MENU
            send_greeting(message)
        elif current_state == STATE_MOSCOW:
            user_states[message.chat.id] = STATE_MENU
            send_greeting(message)
    else:
        bot.send_message(message.chat.id, 'Такая команда не найдена')
bot.polling()
