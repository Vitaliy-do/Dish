cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }


def get_shop_list_by_dishes(dish_list, person_count):
    shop_list = {}
    for dish in dish_list:
        if dish in cook_book:
            # new_dish_list = dict(dish)
            for ingredient in cook_book[dish]:
                new_dish_list = dict(ingredient)

                new_dish_list['quantity'] = new_dish_list['quantity'] * person_count
                if new_dish_list['ingredient_name'] not in shop_list:
                    shop_list[new_dish_list['ingredient_name']] = new_dish_list
                else:
                    shop_list[new_dish_list['ingredient_name']]['quantity'] += new_dish_list['quantity']

    else:
        print('Нет такого блюда')

    return shop_list

dish_list = ['Запеченный картофель']
person_count = 3
shopping_list = get_shop_list_by_dishes(dish_list, person_count)







