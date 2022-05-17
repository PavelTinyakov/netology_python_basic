from collections import Counter
from random import randint

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'новости'
    ]

for i in range(101):
    queries.append('a ' * randint(1, 13))

queries_count = len(queries)
cnt = Counter([len(el.split()) for el in queries])
cnt_sorted = sorted(cnt.items())
print(f'Всего запросов {queries_count}. Из них:')
for el in cnt_sorted:
    word = ('слов', 'слова')[el[0] % 10 == 1 and el[0] % 100 != 11]
    print(f'Запросы из {el[0]} {word} - {el[1]} ({el[1] / queries_count * 100:.2f}%)')
