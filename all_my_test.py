class Outfit:
    def __init__(self, name = "anga", age = "27"):
        self.name = name
        self.age = age 

    def print_name(self):
        print(self.name+" d")

    def print_age(self):
        print(self.age)

    def set_weight(self, value):
        global weight 
        weight = value

    def print_weight(self):
        print(weight)

my_outfit = Outfit()

my_outfit.set_weight("80kg")
my_outfit.print_weight()