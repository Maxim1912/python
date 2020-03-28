def go_to_school(name):
    print(f'''
    {name} встаёт с кровати
    {name} чистит зубы
    {name} идёт в школу
    ''')

def calculator(number1, number2, sign):
    number1 = int(number1)
    number2 = int(number2)

    if sign == '+':
        summa = number1 + number2
        print(f'сумма числа {number1} и {number2} равна {summa}')
    elif sign == '-':
        minus = number1 - number2
        print(f'разность числа {number1} и {number2} равна {minus}')
    elif sign == '*':
        umnozhenije = number1 * number2
        print(f'произведение числа {number1} на {number2} равно {umnozhenije}')
    elif sign == '/':
        if number1 == 0 or number2 == 0:
            print('Невозможно делить на 0!')
        else:
            razdelit = number1 // number2
            print(f'деление числа {number1} на {number2} равно {razdelit}')

calculator(input('Введите число 1\n'), input('Введите число 2\n'), input('Выберите знак\n'))
# go_to_school(input('Как тебя зовут?\n'))
# print('ok')
# go_to_school(input('Как тебя зовут?\n'))

