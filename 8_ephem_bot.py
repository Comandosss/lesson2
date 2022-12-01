"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""


import logging
import settings
import ephem
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log',
    datefmt='%H:%M:%S'
)


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def add_planet(update, context):
    now = datetime.date.today()
    now_date = str(now.strftime('%Y/%m/%d'))
    real_planets = {
        'Mercury': ephem.Mercury(now_date),
        'Venus': ephem.Venus(now_date),
        'Mars': ephem.Mars(now_date),
        'Jupiter': ephem.Jupiter(now_date),
        'Saturn': ephem.Saturn(now_date),
        'Uranus': ephem.Uranus(now_date),
        'Neptune': ephem.Neptune(now_date),
        'Pluto': ephem.Pluto(now_date),
        'Sun': ephem.Sun(now_date),
        'Moon': ephem.Moon(now_date)
    }
    text = update.message.text.split()
    input_plan = text[1].capitalize()
    if input_plan in real_planets:
        select_plan = ephem.constellation(real_planets[input_plan])
        update.message.reply_text(
            f'{now_date}: {input_plan} находится в созвездии: {select_plan[1]}'
        )
    else:
        update.message.reply_text('Введи планету! Например: /planet Mars')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', add_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Бот запустился')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
