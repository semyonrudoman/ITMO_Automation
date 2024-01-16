num = 1

if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')


str_1 = 'test'
str_2 = 'test1'

if str_1 in str_2:
    print('ДА')
else:
    print('НЕТ')

num_float = 0

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

permit_print = False

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

course = int(input('Укажите Ваш год обучения: '))
if course > 0 and course <= 4:
    print('Бакалавр')
elif course > 4 and course <= 6:
    print('Магистр')
elif course > 6 and course <= 9:
    print('Аспирант')
else:
    print('Введите корректный год обучения')

def task(n):
    if n in range (-100, 101):
        print('+')
    else:
        print("-")

task(-190)
