stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

# Вариант решения 1
result_1 = [k for k, v in stats.items() if v == max(stats.values())]

# Вариант решения 2
result_2 = sorted(stats.items(), key=lambda x: x[1], reverse=True)[0][0]

# Вариант решения 3
result_3 = tuple(filter(lambda x: x[1] == max(stats.values()), stats.items()))[0][0]

print(*result_1)
print(result_2)
print(result_3)
