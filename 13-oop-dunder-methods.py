from time import time


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        print("Convert to string")
        return f"<User: {self.username}>"

    def __repr__(self):
        print("Representation")
        return "<User>"


# print(type((2).__str__()))
# print(type(str(2)))
# print((2).__str__() == str(2))

# user = User("Maktab112", "1234")
# print(str(user))
# print(user)

# print(type((2).__repr__()))

# print(repr(user))
# print(repr(user))

class Number:
    def get_value(self, other):
        return other.value if isinstance(other, self.__class__) else other

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + self.get_value(other)

    def __iadd__(self, other):
        self.value += self.get_value(other)
        return self

    def __lt__(self, other):
        return self.value < self.get_value(other)

    def __gt__(self, other):
        return self.value > self.get_value(other)

    def __le__(self, other):
        return self.value <= self.get_value(other)

    def __ge__(self, other):
        return self.value >= self.get_value(other)

    def __eq__(self, other):
        return self.value == self.get_value(other)

    def __ne__(self, other):
        return self.value != self.get_value(other)


ten = Number(10)
five = Number(5)


# print(ten + five)  # 15 !
# print((5).__add__(10))
# print(5 + 10)
# print(ten + five)

# print((10).__sub__(5))  # -
# print((10).__mul__(5))  # *
# print((10).__truediv__(5))  # /
# print((11).__floordiv__(5))  # //
# print((11).__mod__(5))  # %
# print((11).__divmod__(5))  # ( //, % )
# print((11).__pow__(2))  # **

# ten += 10  # iadd

# print((10).__lt__(5))  # <
# print((10).__gt__(5))  # >
# print((10).__le__(5))  # <=
# print((10).__ge__(5))  # >=
# print((10).__eq__(5))  # ==
# print((10).__ne__(5))  # !=

# print(ten == five)
# print(ten > five)
# print(ten < five)
# print(ten <= five)
# print(ten >= five)
# print(ten != five)

class Bag:
    def __init__(self, *items):
        self.items = items

    def __contains__(self, item):
        print("Contains Called !")
        # return item in self.items
        for i in self.items:
            if (isinstance(i, (list, tuple, set)) and item in i) or i == item:
                return True
        return False

    def __getitem__(self, index):
        return self.items[index]

    def __call__(self, *list_data, **dict_data):
        print("List data:", *list_data)
        print("Dict data:", dict_data)

    def __len__(self):
        return len(self.items)


my_bag = Bag(1, 2, [10, 20, 30, 40], "reza", ten)


# print(len([1, 2, 3, 4]))
# print(([1, 2, 3, 4]).__len__())
# print(len(my_bag))

# print(10 in my_bag)
# print(1 in [1, 2, 3, 4])
# print(([1, 2, 3, 4]).__contains__(1))
# print(1 in my_bag)
# print("reza" in my_bag)
# print(ten in my_bag)
eleven = Number(10)

print(eleven in my_bag)

# print(my_bag.__contains__(ten))

# print(my_bag)
# my_bag()
# my_bag('salam', 123, name="reza")
# my_bag.__call__()
# print(callable(my_bag))

# print(my_bag[0])
# print(my_bag[1])
# print(my_bag[2])
# print(my_bag[3])


class Timer:
    def __init__(self, callback):
        self.callback = callback

    def __call__(self, *args, **kwargs):
        start_time = time()
        result = self.callback(*args, **kwargs)
        print(f"Timer of <{self.callback.__name__}>", time() - start_time)
        return result


# @Timer
# def process(number):
#     return sum(range(number ** number))


# print(process(8))


class Writer:
    def __init__(self, path):
        self.path = path

    def __call__(self, callback):
        assert callable(callback)
        self.callback = callback
        return self.execute

    def execute(self, *args, **kwargs):
        result = self.callback(*args, **kwargs)

        with open(self.path, "w") as file:
            print(result, file=file)

        return result


@Writer(path="process.txt")
def process(number):
    return sum(range(number ** number))


print(process(8))
