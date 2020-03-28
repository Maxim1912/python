name = input('What is your name?\n')
age = int(input('What is your age?\n'))

if 0 < age < 7:
    print('You are going to preschool')
elif 6 < age < 19:
    print('You are going to school')
elif 18 < age < 36:
    print('You are going to office')
elif 35 < age < 90:
    print('You are going to business')
