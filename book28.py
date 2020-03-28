import random
secret = random.randint(1,99)
guess = 0
tries = 0

print ('''Эй на палубе! Я Ужасный пират Робертс, и у меня есть секрет!
Это число от 1 до 99. Я дам тебе 6 попыток.''')

while guess != secret and tries < 6:
    guess = int(input("Твой варивант: "))
    if guess < secret:
        print("Число слишком малое!")
    elif guess > secret:
        print ("Число слишком большое!")

    tries += 1

if guess == secret:
    print ("Ура, ты угадал мой секрет!")
else:
    print('Попытки закончились!')
    print('Ответ:', secret)