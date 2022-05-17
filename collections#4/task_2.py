ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

# Вариант решения 1
result_1 = set()
for el in ids.values():
    result_1.update(el)

# Вариант решения 2
result_2 = []
for lst in ids.values():
    for val in lst:
        if val not in result_2:
            result_2.append(val)

# Вариант решения 3
result_3 = set(sum(ids.values(), []))


print(list(result_1))
print(result_2)
print(list(result_3))
