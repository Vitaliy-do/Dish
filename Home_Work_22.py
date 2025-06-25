def read_cookbook(filename):
    cook_book = {}
    with open(filename, encoding='utf-8') as file:
        for line in file:
            dish = line.strip()
            if not dish:
                continue
            count = int(file.readline())
            cook_book[dish] = []
            for _ in range(count):
                ing, qty, measure = file.readline().strip().split(' | ')
                cook_book[dish].append({
                    'ingredient_name': ing,
                    'quantity': int(qty),
                    'measure': measure
                })
            file.readline()
        return cook_book

cook_book = read_cookbook('recipes.txt')

# from pprint import pprint
# pprint(cook_book)

def get_shop_list_by_dishes(dish_list, person_count):
    shop_list = {}
    for dish in dish_list:
        if dish in cook_book:
            new_dish_list = dict('ingredient_name')
            for ingredient in dish_list:
                new_dish_list['quantity'] = new_dish_list['quantity'] * person_count
                if new_dish_list['ingredient_name'] in shop_list:
                    shop_list[new_dish_list['ingridient_name']]['quantity'] += new_dish_list['quantity']
                else:
                    shop_list[new_dish_list['ingridient_name']] = new_dish_list

    else:
        print('Нет такого блюда')

    return shop_list


# from pprint import pprint
# pprint(cook_book)


dishes = ['Омлет', 'Фахитос']
persons = 3
shopping_list = get_shop_list_by_dishes(dishes, persons)






