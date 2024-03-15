def division(num1, num2):
    return num1 / num2


# raise TypeError("Salaaaaam")
# raise ZeroDivisionError("10 / 0 !!!")
# print(ZeroDivisionError("10 / 0 !!!"))

# print(division(10, 4))
# print(division(10, 2))
# print(division(10, 0))
# print(division(10, '2'))

# Cli Calculator:
# print("Welcome to my calculator \n")
# while True:
#     try:
#         a = float(input("number 1 > "))
#         b = float(input("number 2 > "))
#         operator = input("operator (+,-,/,*) > ")
#
#         if operator == "+":
#             print(a + b)
#         elif operator == "-":
#             print(a - b)
#         elif operator == "/":
#             print(a / b)
#         elif operator == "*":
#             print(a * b)
#         else:
#             print("Operator invalid :(")
#     except (ZeroDivisionError, ValueError) as e:
#         print("Error:", e)
#     except KeyboardInterrupt:
#         continue
#
#     input()

# try:
#     print("Start try")
#     _ = 10/4
#
#     try:
#         var = 12
#         raise ZeroDivisionError
#     except ZeroDivisionError:
#         print("nested try: zero div")
#
#     print("Variable from nested try:", var)
#     # _ = 10/0
# except (ZeroDivisionError, ValueError, TypeError):
#     print("Start except")
# except IndexError:
#     print("Start except")
# else:
#     print("Start else")
# finally:
#     print("Start finally")

# Assertions:
# while True:
#     try:
#         number = float(input("Please enter a number : "))
#         # if number > 0 and number % 2 != 0:
#         #     raise ValueError("Just even number !")
#
#         assert number > 0 and number % 2 == 0, "Just even number !"
#
#     # except TypeError:
#     #     print("einak bedam !!! mage nemibnini goftam number bede !")
#     except ValueError as e:
#         print(e)
#     except AssertionError as e:
#         print(e)
#     finally:
#         input()

# assert 12 < 10, "12 > 10"

# File:
file = open("text.txt", "w")
#
# print(file.read(10))
# # file.seek(0)
# print(file.read(10))
# file.seek(0)
# print(file.readline(10))
# print(file.read(10))

# print(file.readlines())

# file.read(10)
file.write("salam refigh")
