# Data persistence
# Pickling :)
import pickle

class Shape:
    shapes = []

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.__class__.shapes.append(self)

    @classmethod
    def load(cls, file_path):
        with open(file_path, 'rb') as _:
            cls.shapes = pickle.load(_)

        # with open(file_path, 'r') as _:
        #     for line in _.readlines():
        #         if line.strip():
        #             cls(*line.split())

    @classmethod
    def save(cls, file_path):
        with open(file_path, 'wb') as _:
            pickle.dump(cls.shapes, _)

    #     with open(file_path, 'w') as _:
    #         for shape in cls.shapes:
    #             print(shape.name, shape.x, shape.y, file=_)


# triangle = Shape("Triangle", 10, 100)
# circle = Shape("Circle", 1, 2)
# rectangle = Shape("Rectangle", 50, 500)
# square = Shape("Square", 4, 4)
#
# Shape.save("shapes.save")

# Shape.load("shapes.save")

# for shape in Shape.shapes:
#     print(shape.name, shape.x + shape.y)


# dill
# shelve
