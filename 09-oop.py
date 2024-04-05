# class Maktab:
#     # class attr
#     instances = []
#     id = None
#
#     def __init__(self, _id):
#         # instance attr
#         # print(self.id)
#         self.id = _id
#
#         # print(self.__class__ == Maktab)
#
#         self.instances.append(self)
#

# Maktab(112)
# Maktab(100)
# Maktab(110)
# Maktab(105)

# for instance in Maktab.instances:
#     print(instance.id)

import os


def clear():
    os.system('cls' if os.name.lower() == 'nt' else 'clear')


class XOTable:
    map = {k: False for k in range(10)}

    def print(self):
        print("""
        -------------------
        |  {}  |  {}  |  {}  |
        -------------------
        |  {}  |  {}  |  {}  |
        -------------------
        |  {}  |  {}  |  {}  |
        """.format(
            *[self.map[i] or '-' for i in self.map]
        ))

    def mark(self, cell_no, sign):
        assert isinstance(cell_no, int) and 1 <= cell_no <= 9, "Invalid Cell number"
        assert not self.map[cell_no - 1], "Cell is filled"

        self.map[cell_no - 1] = sign.lower()


def main():
    table = XOTable()
    sign = 'o'

    while True:
        clear()
        table.print()

        cell = int(input(f"\n > [{sign}] (1 - 9): "))
        table.mark(cell, sign)

        sign = 'x' if sign == 'o' else 'o'


main()


class Setting:
    Round = 3

# class Player
# class Setting

# player 1 : Ali
# player 2 : Reza

# -----

# [1,2,3] , [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]

# Ali win

# -----

