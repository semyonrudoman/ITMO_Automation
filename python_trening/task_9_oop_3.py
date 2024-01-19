class Soda:
    def __init__(self, add=None):
        self.add = add
    def show_my_drink(self):
        if self.add:
            print('Газировка и', self.add)
        else:
            print("Обычная газировка")

free = Soda()
free.show_my_drink()

lime = Soda('Лайм')
lime.show_my_drink()