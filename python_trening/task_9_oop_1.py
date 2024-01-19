from task_9_checks import Checks
class Input(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

search = Input('input#search', "text")
search.check_txt()

class Button(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

run = Button('button#search', "Square")
run.check_txt()

class Title(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

up = Title('title#search', "bold")
up.check_txt()

class Link(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

connect = Link('link#search', "URL")
connect.check_txt()

