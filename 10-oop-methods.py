class Game:
    # class attr
    memory = 100

    @staticmethod
    def wellcome(name):
        print(f"Welcome, {name}")

    @classmethod
    def clean(cls):
        cls.memory = 0
        print('Memory has been cleaned :)')

    def __init__(self):
        # instance attr
        pass


# Static Method --
Game.wellcome("reza")
cs2 = Game()
cs2.wellcome("ALi")
print(Game.memory)  # 100
print(cs2.memory)  # 100
Game.clean()
print(cs2.memory)  # 100
cs_go = Game()
print(cs_go.memory)

# print(Game.memory)
# Game.clean()
# cs2.clean()
# print(Game.memory)
