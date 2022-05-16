geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

# Вариант решения 1
result_1 = list(filter(lambda x: 'Россия' in tuple(x.values())[0], geo_logs))

# Вариант решения 2
result_2 = [el for el in geo_logs if 'Россия' in tuple(el.values())[0]]

print(result_1)
print(result_2)