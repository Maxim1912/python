import random

print('Добро пожаловать в игру "Угадай число"!')
print('Как ваше имя?')
name = input()
name = name.title()
print ('Привет, ' + name + '. Мы начинаем загадывать число от 1 до 20.')

number = random.randint(1, 20)
counter = 0

# функция угадывания чисел
def guessNumber():
    for counter in range(10):
        if counter == 0:
            print ('Какое число загадано?')
        else:
            print ('Попробуйте ещё раз')

        answer = int(input())

        if answer > number:
            print('Ваше число слишком большое!')

        if answer < number:
            print('Ваше число слишком маленькое!')

        if answer == number:
            break

    if answer == number:
        print('Вы угадали число за ' + str(counter+1) + ' попыток.')
    else:
        print('Вы проиграли!!!')

gameplay = 'да'

while gameplay == 'да':
    guessNumber()
    print('Хотите сыграть ещё раз?')
    gameplay = input()
    gameplay = gameplay.lower()

    while gameplay not in {'да', 'нет'}:
        print('Да или нет?')
        gameplay = input()
        gameplay = gameplay.lower()



    