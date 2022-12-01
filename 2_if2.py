"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты
"""


def string_comparison(line_1, line_2):
    if isinstance(line_1, int) and isinstance(line_2, int):
        return 0
    elif line_1 == line_2:
        return 1
    elif line_1 != line_2 and line_2 == 'learn':
        return 3
    elif line_1 != line_2 and len(line_1) > len(line_2):
        return 2


if __name__ == "__main__":
    counter = 0
    print(string_comparison(2, 3))
    print(string_comparison('Pythons', 'Pythons'))
    print(string_comparison('Python', 'burn'))
    print(string_comparison('Pythons', 'learn'))
