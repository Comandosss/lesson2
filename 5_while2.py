"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:
    Пользователь: Что делаешь?
    Программа:Программирую
"""


def ask_user(answer):
    while True:
        question = input("Введите вопрос: ").capitalize()
        if question in answer:
            answer = questions_and_answers[question]
            print(answer)
            break
        print("Переформулируй вопрос!")


if __name__ == "__main__":
    questions_and_answers = {
        "Как дела?": "Плохо",
        "Что делаешь?": "Пою в душе",
        "Какие планы на сегодня?": "Пробежать полумарафон",
        "Чем планируешь заниматься?": "Писать код",
    }
    ask_user(questions_and_answers)
