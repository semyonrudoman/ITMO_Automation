def add(x, y):
    return x + y

print(add(1,2))
print(add('i a', 'm tester'))

def arg(a, b, c=2, d=3):
    return a + b + c + d
print(arg(1, 1, 1, 1))
print(arg(2, 2))

def range_arg(a, b, c, d):

    return a + ' ' + b + ' ' + c + ' ' + d

print(range_arg('1', '2', '3', '4'))
print(range_arg('1', '2', d='3', c='4'))

def task_1(a=(1, 2, 3, 4)):
    return a[0]

def task_2(radius, pi=3.14159):
    return pi * radius ** 2
