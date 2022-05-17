from functools import reduce


data = ['2018-01-01', 'yandex', 'cpc', 100, 'cpa', 20, 'cpl', 40, 'cpm', 60, 'ctr', 40]


# Вариант решения 1
def result_1(arr):
    if len(arr) == 1:
        return arr[0]
    return {arr[0]: result_1(arr[1:])}


# Вариант решения 2
result_2 = reduce(lambda x, y: {y: x}, reversed(data))

# Вариант решения 3
result_3 = data[-1]
for el in data[-2::-1]:
    result_3 = {el: result_3}


print(result_1(data))
print(result_2)
print(result_3)
