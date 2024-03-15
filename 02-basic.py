# def power_two(number):
#     return number ** 2
#
#
# print(power_two(2))
# print(power_two(2) == 4)


# void Functions:
# function -> None
def say_hello(name):
    print("Hi, " + name)
    print("Hello, " + name)
    print("Salam, " + name)

    # return "khorojie !!!"


# print(say_hello("Reza"))
# print(say_hello("Reza"))
# print(say_hello("Reza"))
# print(say_hello("Reza"))
# print(say_hello("Reza"))
# print(say_hello("Reza"))
#
# result = say_hello("Parisa")
# print(result)

# result = say_hello("Ali")
# print(result)

# result = say_hello("Parisa")
# print(result)

# response = say_hello("Mohammad")

# print(type(response))
#
# print(response)
# print(response)
# print(response)

# say_hello('ali')

# Return Functions:
def power_two(number):
    return number ** 2


# print(power_two(10))
# print(power_two())

# print(power_two)


# Positional Args
# def division(num_one, num_two):
#     return num_one / num_two
#
#
# print(division(8, 2))
# print(division(2, num_two=8))
# print(division(num_two=2, num_one=8))

# Positional + Optional(Default Value) Args
# def division(num_one, num_two, floor=False):
#     if floor:
#         return num_one // num_two
#     return num_one / num_two

# print(division(8, 2))
# print(division(2, num_two=8, floor=True))
# print(division(num_two=2, num_one=8))

# *args
# def avg(*fatemeh_numbers):
# def avg(*args):
#     # print(args, type(args))
#     # return (n1 + n2) / 2
#
#     return sum(args) / len(args)
#
#
# print(avg(10, 20, 30, 40, 50, 10))


# **kwargs
# def chap(**kwargs):
#     print(kwargs)
#
#
# chap(num1=1, num2=2, num3=3)

# for i in range(10): --> end = 10
# for i in range(0, 10): --> start = 0, end = 10
# for i in range(0, 10, 1): --> start, stop, step
#     print(i)

# با استفاده از توابع، حلقه ای ایجاد کنید که اعداد را از start تا stop بصورت step بشمارد
# loop: 1 -> value

def loop(*args):
    """
        end => step = 1, start, 0
        start, stop => step = 1
        start, stop, step
    """

    # validation:
    if len(args) == 0 or len(args) > 3:
        print("Error :(")
        return None

    start = 0
    step = 1
    stop = args[0]

    if len(args) == 2:
        start = args[0]
        stop = args[1]
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]

    if (step > 0 and start >= stop) or (step < 0 and start <= stop):
        print("LOOP Finished  ^-0")
        return

    print("In-Loop => value:", start, ",stop:", stop, ",step:", step)
    loop(start + step, stop, step)


# loop(4)
# loop(0, 10)
# loop(0, 10, 3)
# loop(0, 10, 30)
# loop(10, 2, 3)
# loop(0, 100, -30)
# loop(0, -100, -30)
