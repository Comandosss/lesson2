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
table_sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]}
]
    
sum_all_product = 0
sum_len_lists = 0 

def main(each_product):
    summa_each = 0
    for element in each_product:
        summa_each += element
    return summa_each

if __name__ == "__main__":
    for count in table_sales:
        print(f"Продукт: {count['product']}, суммарное количество продаж: {main(count['items_sold'])} шт.")
        print(f"Продукт: {count['product']}, среднее количество продаж: {main(count['items_sold'])//len(count['items_sold'])} шт.")    
        sum_all_product += main(count['items_sold'])
        sum_len_lists += len(count['items_sold'])
    print(f"Суммарное количество продаж всех товаров: {sum_all_product} шт.")
    print(f"Среднее количество продаж всех товаров: {sum_all_product//sum_len_lists} шт.")
