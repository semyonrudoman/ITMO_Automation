def task_1(a: int, b: float, c: str, d: list = [1, 2, 3], e: bool = False) -> str:
    return print(a, 'относится к типу', type(a)), print(b, 'относится к типу', type(b)), print(c, 'относится к типу', type(c)), print(d, 'относится к типу', type(d)), print(e, 'относится к типу', type(e)),
print(task_1(23, 12.00003, 'ИТМО'))

def task_2(a=[1, 2, 3, 5, 8, 13, 21]) -> list:
#такая последовательность чисел, где следующее число равняется сумме двах предудущих называется числа Фибоначчи
    return a[0:3]
print(task_2())

def task_3(a: int) -> int:
    return a ** 2
print(task_3(3))
