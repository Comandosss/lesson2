"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран
"""


def input_age_user(age):
    try:
        age = int(age)
    except (TypeError, ValueError):
        return 'Неверный ввод! Введите положительное числовое значение!'
    else:
        if 0 <= age <= 6:
            return 'Ходишь в детский сад'
        elif 6 < age <= 18:
            return 'Учишься в школе'
        elif 18 < age <= 23:
            return 'Учишься в ВУЗе'
        elif 23 < age <= 61:
            return 'Работаешь'
        else:
            return 'Люди столько не живут'


if __name__ == "__main__":
    age_user = input('Сколько вам лет? ')
    result_age_user = input_age_user(age_user)
    print(result_age_user)
