# class Maktab:
#     def __init__(self, name, maktab_id):
#         self.name = name
#         self.set_id(maktab_id)
#
#     def set_id(self, value):  # setter
#         assert isinstance(value, int), "..."
#         self.id = value
#
#     def get_id(self):  # getter
#         return hash(str(self.id))


# maktab_105 = Maktab('maktab-105', 105)
# print(maktab_105.get_id())


class Maktab:
    def __init__(self, name, maktab_id):
        self.name = name
        self.id = maktab_id

    @property
    def id(self):  # getter
        print("ID, Getter called !")
        return hash(str(self._id))

    @id.setter
    def id(self, value):  # setter
        print("ID, Setter called !")
        assert isinstance(value, int), "ID must be integer"
        self._id = value

    # @id.deleter #  => del maktab_112.id


# maktab_110 = Maktab('Maktab - 110', '110')
maktab_112 = Maktab('Maktab - 112', 112)
print(maktab_112.id)
# maktab_112.id = '12222'
maktab_112.id = 12222
# print(maktab_112.id)
# maktab_112.id = 1221
# print(maktab_112.id)
# print(maktab_112._id)
