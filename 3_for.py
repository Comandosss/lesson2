"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по количеству проданных телефонов
[
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""


if __name__ == "__main__":
    table_sales = [
        {
            'product': 'iPhone 12',
            'items_sold': [
                363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186,
            ]
        },
        {
            'product': 'Xiaomi Mi11',
            'items_sold': [
                317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316,
            ]
        },
        {
            'product': 'Samsung Galaxy 21',
            'items_sold': [
                343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247,
            ]
        },
    ]
    sum_all = 0
    sum_len_lists = 0
    for count in table_sales:
        product = count['product']
        each_len_list = len(count['items_sold'])
        if count['items_sold']:
            sum_each = sum(count['items_sold'], 0)
            print(f'Прод: {product}, сумм. кол-во продаж: {sum_each} шт.')
            avg_each = sum_each // each_len_list
            print(f'Прод: {product}, сред. кол-во продаж: {avg_each} шт.')
            sum_all += sum_each
            sum_len_lists += each_len_list
        else:
            print(f'Прод: {product}, сумм. кол-во продаж: 0 шт.')
            print(f'Прод: {product}, сред. кол-во продаж: 0 шт.')
    print(f'Сумм. кол-во продаж всех товаров: {sum_all} шт.')
    avg_all = sum_all // sum_len_lists
    print(f'Сред. кол-во продаж всех товаров: {avg_all} шт.')
