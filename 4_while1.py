"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”
"""


def hello_user():
    while True:
        user_say = input('Как дела? ').capitalize()
        if user_say == 'Хорошо':
            break
        else:
            print('Угадай ответ, чтобы закончить диалог')


if __name__ == "__main__":
    hello_user()
