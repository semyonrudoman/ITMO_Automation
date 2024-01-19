# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def square(self):
#         S = self.a * self.b
#         print('Площадь прямоугольника = ', S)
#     def perimetr(self):
#         P = 2 * (self.a + self.b)
#         print('Периметр прямоугольника = ', P)
#
# r1 = Rectangle(2, 3)
# r2 = Rectangle(5, 5)
# r3 = Rectangle(4, 9)
# r1.square()
# r1.perimetr()
# r2.square()
# r2.perimetr()
# r3.square()
# r3.perimetr()

# class Math:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def addition(self):
#         ad = self.a + self.b
#         print("Результат сложения = ", ad)
#     def multiplication(self):
#         mu = self.a * self.b
#         print('Результат умножения = ', mu)
#     def division(self):
#         if self.b == 0:
#             print('Деление на ноль невозможно')
#         else:
#             di = self.a / self.b
#             print('Результат деления = ', di)
#     def substraction(self):
#         su = self.a - self.b
#         print('Результат вычитания = ', su)
#
# math1 = Math(4, 2)
# math1.addition()
# math1.multiplication()
# math1.division()
# math1.substraction()
#
class Buttons:
    def __init__(self, text, type = 'button', loc = None):
        self.text = text
        self.type = type
        self.loc = loc
    def click(self):
        print(f'Клик по кнопке {self.text}')

tb = Buttons('Text Box')
cb = Buttons('Check Box')
rb = Buttons('Radio Button')
wt = Buttons('Web Tables')
b = Buttons('Buttons')
l = Buttons('Links')
bl = Buttons('Broken Links - Images')
ud = Buttons('Upload snd Downloads')
dp = Buttons('Dynamic Properties')
tb.click()
cb.click()
rb.click()
wt.click()
b.click()
l.click()
bl.click()
ud.click()
dp.click()

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    def launch(self):
        print('Автомобиль заведен')
    def stop(self):
        print('Автомобиль заглушен')
    def year1(self, year):
        self.year = year
    def type1(self, type):
        self.type = type
    def color1(self, color):
        self.color = color

