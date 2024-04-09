from time import time


# start_time = time()
# print("Before <process>")
# print(process(9))
# print("After <process>")
# end_time = time()
# print(f"<process> : {end_time - start_time}")


def timer(_callable):
    def inner(number):
        start_time = time()
        # print(f"Before <{_callable.__name__}>")
        result = _callable(number)
        # print(f"After <{_callable.__name__}>")
        end_time = time()
        print(f"Timer of <{_callable.__name__}>({number})", end_time - start_time)
        return result

    return inner


# @timer
# def process(number):
#     return sum(range(number ** number))


# res = timer(process)(6)
# print(res)


# print(process(9))
# print(process(6))
# print(process(7))
# print(process(5))
# print(process(4))
# print(process(9))


def safe(callback):
    def _(*args, **kwargs):
        while True:
            try:
                res = callback(*args, **kwargs)
            except (Exception, KeyboardInterrupt):
                print("Error: Try again !\n")
                continue

            return res

    return _


@safe
def get_phone_number():
    raw_number = input("Please enter phone number: ")
    assert raw_number.isdecimal() and len(raw_number) == 11 and raw_number.startswith('09')
    return raw_number


@safe
def get_age():
    raw_number = input("Please enter your age: ")
    assert 3 >= len(raw_number) >= 1 and raw_number.isdecimal()
    return raw_number


# get_phone_number()
# get_age()


class Maktab:
    @safe
    def __init__(self, phone, age):
        assert phone.isdecimal() and len(phone) == 11 and phone.startswith('09')
        assert 3 >= len(age) >= 1 and age.isdecimal()


# Maktab('091233344444', '123')
cached_values = {}


def cache(callback):
    def _(number):
        if res := cached_values.get(number, None):
            print("-- From Cache --")
            return res

        res = callback(number)
        cached_values[number] = res
        return res

    return _


# @timer
# @cache
# def process(number):
#     return sum(range(number ** number * 10))


# print(process(8))
# print(process(8))


def printer(count=1, title="Printer"):
    def _(callback):
        def __(*args, **kwargs):
            res = callback(*args, **kwargs)

            for i in range(count):
                print(f"{title} [{i + 1}]: {res}")

            return res

        return __

    return _


@printer()
def process(number):
    return sum(range(number ** number * 10))


# print(process(7))


def writer(file_path):
    def _(callback):
        def __(*args, **kwargs):
            result = callback(*args, **kwargs)

            with open(file_path, "w") as file:
                print(result, file=file)

            return result

        return __

    return _


@writer("double_sum.log")
def double_sum(x, y):
    return 2 * (x + y)


print(double_sum(10, 100))

new_double_sum = writer("new_double_sum.log")(double_sum)
print(new_double_sum(10, 100))
