def is_valid(*val):
    try:
        return all(float(i) > 0 for i in val)
    except ValueError:
        return False


def get_square_perimeter_area(side):
    if is_valid(side):
        side = float(side)
        return side * 4, side ** 2
    return f'err - {type(side)} * 4', f'err - {type(side)} ** 2'


def get_rectangle_perimeter_area(side_a, side_b):
    if is_valid(side_a, side_b):
        side_a, side_b = float(side_a), float(side_b)
        return 2 * (side_a + side_b), side_a * side_b
    return f'err - 2 * ({type(side_a)} + {type(side_b)})', f'err - {type(side_a)} * {type(side_b)}'


if __name__ == '__main__':
    square_side = input("Введите длину стороны квадрата: ")
    square_perimeter, square_area = get_square_perimeter_area(square_side)
    print('Периметр квадрата:', square_perimeter)
    print('Площадь квадрата:', square_area)

    print()

    rectangle_length = input("Введите длину прямоугольника: ")
    rectangle_width = input("Введите ширину прямоугольника: ")
    rectangle_perimeter, rectangle_area = get_rectangle_perimeter_area(rectangle_length, rectangle_width)
    print('Периметр прямоугольника', rectangle_perimeter)
    print('Площадь прямоугольника:', rectangle_area)

    print()

    symbol = input('Введите символ разделитель: ')
    try:
        print(symbol * int((square_perimeter + rectangle_perimeter)))
    except ValueError:
        print(symbol * 50)

    print()

    salary = float(input('Введите заработную плату в месяц: '))
    mortgage = float(input('Введите, какой процент(%) уходит на ипотеку: '))
    expenses = float(input('Введите, какой процент(%) уходит на жизнь: '))

    print(f'На ипотеку было потрачено: {salary * mortgage / 100 * 12} руб.')
    print(f'Было накоплено: {(salary * (1 -(mortgage + expenses) / 100)) * 12} руб.')
