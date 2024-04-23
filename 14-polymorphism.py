class Human:
    name = ""

    def say_hello(self):
        print(f"Hi, {self.name}")


class PersianHuman(Human):
    def say_hello(self):
        print(f"سلام, {self.name}")


class ArabicHuman(Human):
    def say_hello(self):
        print(f"السلام, {self.name}")


# 2

class Shape:
    def area(self):
        return

    def premier(self):
        return


class Square(Shape):
    def area(self):
        return self.x ** 2

    def premier(self):
        return self.x * 4


class Sina(Human):
    height = 185
    name = "Sina"


class Arash(Human):
    height = "18.4 inch"
    name = "آرش"


sina = Sina()
arash = Arash()


sina.say_hello()
arash.say_hello()
