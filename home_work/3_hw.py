def major(n1, n2):
    if n1 > n2:
        print(n1)
    else:
        print(n2)

major(2, 2)

def dif(d1, d2):
    if (abs(d1 - d2) == 135):
        print('yes')
    else:
        print('no')

dif(1, 136)

def year(m):
    if m in range(3, 6):
        print('Весна')
    elif m in range(6, 9):
        print("Лето")
    elif m in range(9, 12):
        print('Осень')
    elif m == 1 or m == 2 or m == 12:
        print('Зима')
    else:
        print('Введите число от 1 до 12')

year(11)

def ten(a1, a2, a3):
    if a1 > 10 and a2 > 10 and a3 > 10:
        print('yes')
    else:
        print('no')

ten(11, 12, 1)


def summa(sm_list: list):
    if len(sm_list) == 5:
        sm = 0
        for i in sm_list:
            if i > 0:
                sm += 1
        print('Кол-во положительных чисел в списке: ', sm)
    else:
        print('Кол-во элементов в списке должно быть 5')

summa((12, -34, 12, -1, 23))

def day(yr: int, mn: int) -> int:
    return yr * 12 * 29 + mn * 29

print(day(25, 1))
