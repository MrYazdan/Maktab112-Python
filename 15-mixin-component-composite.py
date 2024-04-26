class Bag:
    def __init__(self):
        self.storage = []


class Player:
    def __init__(self, name):
        self.name = name
        self.bag = Bag()  # Composite


class Game:
    def __init__(self, *players):
        self.players = players  # Component !


fatemeh = Player("Fatemeh")  # Component !
ali = Player("Ali")  # Component !
reza = Player("Reza")  # Component !
hamid = Player("Hamid")  # Component !

my_game = Game([fatemeh, ali, reza, hamid])

ali.name = "reza"


# Composite
# class Game:
#     def __init__(self, player_name1, player_name2):
#         self.players = [
#             Player(player_name1),
#             Player(player_name2)
#         ]
#
#
# _game = Game("Fatemeh", "Ali")


class FastReload:
    reload_time = 2


class Gun:
    def __init__(self, damage, fire_rate):
        self.damage = damage
        self.fire_rate = fire_rate
        self.attachments = []


class Ak47(Gun):
    def __init__(self):
        super().__init__(35, 2)
        self.reload_time = 4


class Ak47Sina(Ak47, FastReload):
    def __init__(self):
        super().__init__()
        self.reload_time -= FastReload.reload_time





