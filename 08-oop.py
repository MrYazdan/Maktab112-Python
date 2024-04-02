# from functools import partial


# def teacher_say_hello(name):
#     print(f"Salam, ({name})")
#     print(f"Salam, ({teacher['name']})")


# teachers = [
#     {
#         "name": "Mahdi",
#         "age": 22,
#         "email": "Mahdi22@gmail.com",
#         "score": 15,
#         "say_hello": partial(teacher_say_hello, "Mahdi")
#     },
#     {
#         "name": "Mojtaba",
#         "age": 21,
#         "email": "Mojtaba21@gmail.com",
#         "score": 10,
#         "say_hello": partial(teacher_say_hello, "Mojtaba")
#     },
#     {
#         "name": "Reza",
#         "age": 20,
#         "email": "isMrYazdan@gmail.com",
#         "score": 5,
#         "say_hello": partial(teacher_say_hello, "Reza")
#     },
# ]

# mahdi = teachers[0]
# reza = teachers[2]
# reza["say_hello"](reza)
# reza["say_hello"]()

# print(mahdi['score'] > reza['score'])


# OOP:
# class Human:
#     name = None
#     age = None
#     email = None
#
#     def say_hello(human, name=None):
#
#         print(f"Hi, {name or human.name}")
#
#
# reza = Human()
# reza.name = "Reza"
# reza.age = 24
# reza.say_hello()
# reza.say_hello('mohammad')


class Human:
    def __init__(self, name, age, email=None):
        self.name = name  # instance attr

        assert self.validate_age(age), "Error : Age"
        self.age = age  # instance attr

        self.email = email  # instance attr

    def validate_age(self, age):  # noqa
        return isinstance(age, int)

    def say_hello(self):
        print(f"Hi, {self.name}")


reza = Human('Reza', 24, "ismryazdan@gmail.com")
reza.phone = "09132223333"  # instance attr
# ali = Human("Ali", 22)

# print(reza.phone)

# reza.say_hello()
# ali.say_hello()Please enter email:

# print(isinstance('salam', int))
# print(isinstance('salam', object))
# print(isinstance('salam', str))
# print(isinstance('salam', str))
# print(isinstance(reza, Human))
# print(isinstance(reza, object))

# print(map(int, [1,23,4]))

# print(id(reza))
# print(hash(reza))
# print(reza)
