import os
from pprint import pprint


def file_path(file_name: str) -> str:
    for root, dirnames, filenames in os.walk('.'):
        for file in filenames:
            if file == file_name:
                return os.path.join(root, file)


def get_cook_book(file_name: str) -> dict:
    recipe_book = dict()
    with open(file_path(file_name), encoding='utf-8') as recipes:
        for row in recipes:
            dish_name = row.strip()
            recipe_book[dish_name] = []
            quantity_ingredients = int(recipes.readline())
            for _ in range(quantity_ingredients):
                ingredient, quantity, measure = recipes.readline().strip().split(' | ')
                ingredients_list = {'ingredient_name': ingredient, 'quantity': int(quantity), 'measure': measure}
                recipe_book[dish_name].append(ingredients_list)
            recipes.readline()
    return recipe_book


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    shopping_list = dict()
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient.pop('ingredient_name')
            if ingredient_name in shopping_list:
                shopping_list[ingredient_name]['quantity'] += ingredient['quantity'] * person_count
            else:
                ingredient['quantity'] *= person_count
                shopping_list[ingredient_name] = ingredient
    return shopping_list


def write_result_file(*files_names: str) -> None:
    files_dict = dict()
    for file_name in files_names:
        with open(file_path(file_name), encoding='utf-8') as f:
            files_dict[file_name] = f.readlines()
    with open('result.txt', 'w', encoding='utf-8') as fw:
        for file in sorted(files_dict, key=files_dict.get, reverse=True):
            fw.write(f'{file}\n{len(files_dict[file])}\n{"".join(files_dict[file])}\n\n')


if __name__ == '__main__':
    cook_book = get_cook_book('recipes.txt')
    pprint(cook_book, sort_dicts=False, width=100)

    pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))

    write_result_file('1.txt', '2.txt', '3.txt')
