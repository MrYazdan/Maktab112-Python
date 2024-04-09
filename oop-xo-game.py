import os


def clear():
    os.system('cls' if os.name.lower() == 'nt' else 'clear')


class Table:
    map = {n: n+1 for n in range(10)}
    white_list = [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]

    def check(self):
        for li in self.white_list:
            if self.map[li[0]-1] == self.map[li[1]-1] == self.map[li[2]-1]:
                return True

    def print(self):
        print("""
        -------------------
        |  {}  |  {}  |  {}  |
        -------------------
        |  {}  |  {}  |  {}  |
        -------------------
        |  {}  |  {}  |  {}  |
        """.format(
            *[self.map[i] for i in self.map]
        ))

    def mark(self, cell_no, sign):
        assert isinstance(cell_no, int) and 1 <= cell_no <= 9, "Invalid Cell number"
        assert not self.map[cell_no - 1] in ('o', 'x'), "Cell is filled"

        self.map[cell_no - 1] = sign.lower()


class Setting:
    winners = []
    round = 3


class Player:
    players = []

    def __init__(self, name):
        self.name = name
        self.sign = None

        self.players.append(self)


# start:
print("---------------------------------")
print("| Welcome to Maktab 112 XO Game |")
print("---------------------------------")
player_name = input("> Enter player (1) name: ")
player_1 = Player(player_name)

player_name = input("> Enter player (2) name: ")
player_2 = Player(player_name)

player_1.sign, player_2.sign = 'o', 'x'
print(f"\n{player_1.name.title()}: '{player_1.sign}', \t{player_2.name.title()}: '{player_2.sign}'")
print("---------------------------------")
input("Press enter to start game ...")

table = Table()
loop_count = 0

count_of_winners = len(Setting.winners)
while loop_count < 9:
    loop_count += 1
    clear()

    for player in Player.players:
        clear()
        table.print()

        cell_no = int(input(f"{player.name}[{player.sign}]: Enter cell no (1, 9): "))
        table.mark(cell_no, player.sign)

        if table.check():
            print(f"{player.name} is win ^-0")
            Setting.winners.append(player)
            break

    if count_of_winners != len(Setting.winners):
        break
