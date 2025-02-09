import webbrowser

from user_schedule import User

import telebot
import time

user = User()
token = '7748783352:AAE7W_otxklZ2eAKIfxLhZnYdJwHqAoGy4g'
bot = telebot.TeleBot(token)

def show_all(message):
    bot.send_message(message.chat.id, user, parse_mode='html')
def show_plans(message):
    bot.send_message(message.chat.id, user.plans_str(), parse_mode='html')
def show_schedule(message):
    bot.send_message(message.chat.id, user.schedule_str(), parse_mode='html')

@bot.message_handler(commands = ['start'])
def start_func(message):
    bot.send_message(message.chat.id,
    f'''\
<u>Если нужно сделать заметку</u>:
    Напишите текст заметки.
    Пример: "Текст заметки"
<u>Если вы хотите поставить в расписание собиытие</u>:
    Укажите день недели, время и текст через знаки "&&&".
    Пример: "Понедельник&&&22:30&&&Подготовка ко сну"\n\n<em>Если нужна дополнительная информация</em> - /help''',
    parse_mode='html')

@bot.message_handler(commands = ['show'])
def show_func(message):
    show_all(message)

@bot.message_handler(commands = ['help'])
def help_func(message):
    bot.send_message(message.chat.id,
f'''<b>Все команды бота:</b>
/start - получить стартовую информацию
/clearp - очистить заметки
/clears - очистить расписание
/git - перейти в репозиторий бота github
/secret - ???''', parse_mode='html')

"""
@bot.message_handler(commands = ['add'])
def add_func(message):
    bot.send_message(message.chat.id,
f'''\
<u>Если нужно сделать заметку</u>:
    Напишите текст заметки.
    Пример: "Текст заметки"
<u>Если вы хотите поставить в расписание собиытие</u>:
    Укажите день недели, время и текст через знаки "&&&".
    Пример: "Понедельник&&&22:30&&&Подготовка ко сну"''', parse_mode='html')
    @bot.message_handler()
    def text(new_message):
        if new_message.text == 'break':
            return 0
        elif '&&&' not in new_message.text:
            user.plans_add(new_message.text)
            show_plans(new_message)
        else:
            day, time, text = new_message.text.split('&&&')
            user.schedule_add(day, time, text)
            show_schedule(new_message)
        bot.reply_to(message, '<em>Действует режим добавления.\nНапишите "break", чтобы остановить режим добавления</em>', parse_mode='html')

"""

@bot.message_handler(commands = ['clearp'])
def showp_func(message):
    user.plans_clear()
    show_all(message)

@bot.message_handler(commands = ['clears'])
def shows_func(message):
    user.schedule_clear()
    show_all(message)

@bot.message_handler(commands = ['git','code','website'])
def git_func(message):
    webbrowser.open('https://github.com/dinarovv/ScheduleTelegramBot')

@bot.message_handler(commands = ['secret'])
def secret_func(message):
    for _ in range(25):
        bot.send_message(message.chat.id,
            '<b><u><em><a href="https://www.youtube.com/watch?v=8CdcCD5V-d8&t=102s">ВЕНОМ</a></em></u></b>',
                parse_mode='html', disable_web_page_preview = True)
        time.sleep(0.333)

@bot.message_handler()
def add_func(message):
    if '&&&' not in message.text:
        user.plans_add(message.text)
        show_plans(message)
    else:
        day, time, text = message.text.split('&&&')
        user.schedule_add(day, time, text)
        show_schedule(message)

try:
    bot.polling(none_stop=True)
except RuntimeError as _ex:
    pass
