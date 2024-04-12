class Parent:
    money = 0

    def __init__(self, name):
        self.name = name

    def cooler_control(self):
        print(f"{self.name}, Controlling cooler ! :)")


class Child(Parent):
    money = 100

    def __init__(self, name, no):
        super().__init__(name)
        self.no = no

    def play_game(self):
        print("Father money:", super().money)
        print("My money:", self.money)
        print(f"{self.name}, Playing game !")

    def cooler_control(self):
        return True


father = Parent("Mahmood")
reza = Child('Reza', 1)
# reza.cooler_control()
reza.play_game()
