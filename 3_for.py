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


def main(each_product):
    summa_each = sum(each_product, 0)
    return summa_each


if __name__ == "__main__":
    table_sales = [
        {
            'product': 'iPhone 12',
            'items_sold': [
                363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186
            ]
        },
        {
            'product': 'Xiaomi Mi11',
            'items_sold': [
                317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316
            ]
        },
        {
            'product': 'Samsung Galaxy 21',
            'items_sold': [
                343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247
            ]
        },
    ]
    sum_all_products = 0
    sum_len_lists = 0
    for count in table_sales:
        product = count['product']
        sales_count = count['items_sold']
        print(f'Прод: {product}, сумм. кол-во продаж: {main(sales_count)} шт.')
        avg_each_prod = main(count['items_sold']) // len(count['items_sold'])
        print(f'Прод: {product}, среднее кол-во продаж: {avg_each_prod} шт.')
        sum_all_products += main(sales_count)
        sum_len_lists += len(sales_count)
    print(f'Сумм. кол-во продаж всех товаров: {sum_all_products} шт.')
    avg_all_product = sum_all_products // sum_len_lists
    print(f'Среднее кол-во продаж всех товаров: {avg_all_product} шт.')
