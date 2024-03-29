# Q1: isnumeric vs isdigit vs isdecimal
# isnumeric = ...
# همه کاراکتر ها باید در عددی باشند ( از هر جنسی ! )

# isdigit = ...
# همه کاراکتر ها باید در پایه ۱۰ باشند ( از هر جنسی ! )

# isdecimal = ...
# همه کاراکتر ها باید عددی در پایه ۱۰ باشند ( فقط و فقط از جنس اعداد رسمی )
# فقط و فقط isdecimal قابل تبدیل ۱۰۰ درصدی به int یا float

# def number_type(number):
#     print(f"isnumeric({number}): {number.isnumeric()}")
#     print(f"isdigit({number}): {number.isdigit()}")
#     print(f"isdecimal({number}): {number.isdecimal()}")


# number_type("0978654321")
# number_type("۱۲۳۴۵۶۷۸۹۰")
# print("------------------------------")
# number_type("\u00B2")
# print("------------------------------")
# number_type("🯴")
# print("------------------------------")
# number_type("\u00bd")

# import sys
# for i in range(1, sys.maxunicode):
#     if (number := chr(i)).isnumeric():
#         print(i, number)

# Q2: (shallow vs deep) copy
# a = [1, 2]
# b = a

# a[1] = 10
# print(id(a))
# print(id(b))
# print(a, b)
# ---------------
# a = [1, 2]
# b = a.copy()

# a[1] = 10
# print(id(a))
# print(id(b))
# print(a, b)
# ---------------
# a = [1, 2, [3, 4]]
# b = a.copy()  # shallow copy !

# import copy
# b = copy.copy(a)  # shallow copy !

# a[1] = 10
# a[2][0] = 30
# print(id(a))
# print(id(b))
# print(id(a[2]))
# print(id(b[2]))
# print(a, b)
# ---------------
# a = [1, 2, [3, 4]]

# import copy

# b = copy.deepcopy(a)

# a[1] = 10
# a[2][0] = 30

# print(id(a))
# print(id(b))

# print(id(a[2]))
# print(id(b[2]))

# print(a, b)
# ---------------
# a = [1, 2, 3, [10, 20, 30]]
# b = a[2:]

# print(id(a[2:]))
# print(id(b))
# ---------------
# operators = [
#     "+",
#     "*",
#     "-",
#     "/",
#     "//",
# ]

# numbers = 10, 20
# for operator in operators:
#     print(eval(f"{numbers[0]}{operator}{numbers[1]}"))
# ---------------
# Zip:

en_number_string = "0123456789"
alphabets = "abcdefghijklmnopqrst"
number_table = [
    [
        [1],
        [1, 1],
        [1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]
    ],
    [
        [2],
        [2, 2],
        [2, 2, 2],
        [2, 2, 2, 2],
        [2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2]
    ],
    [
        [3],
        [3, 3],
        [3, 3, 3],
        [3, 3, 3, 3],
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3]
    ],
    [
        [4],
        [4, 4],
        [4, 4, 4],
        [4, 4, 4, 4],
        [4, 4, 4, 4, 4],
        [4, 4, 4, 4, 4, 4]
    ],
    [
        [5],
        [5, 5],
        [5, 5, 5],
        [5, 5, 5, 5],
        [5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 5]
    ],
    [
        [6],
        [6, 6],
        [6, 6, 6],
        [6, 6, 6, 6],
        [6, 6, 6, 6, 6],
        [6, 6, 6, 6, 6, 6]
    ],
    [
        [7],
        [7, 7],
        [7, 7, 7],
        [7, 7, 7, 7],
        [7, 7, 7, 7, 7],
        [7, 7, 7, 7, 7, 7]
    ]
]

# for i in range(min(len(en_number_string), len(alphabets), len(number_table))):
#     print(en_number_string[i], alphabets[i], number_table[i])

# for en_number, alpha, numbers in zip(en_number_string, alphabets, number_table):
#     print(en_number, alpha, numbers)


# *a, b, c = 1, 2, 3, 4, 5, 6

# print(a, type(a))
# print(b)
# print(c)

# Q3: Try|Except

# assert len('ali') == 4, "Mn motmaenam, ke 'ali' 4 tas"

# while True:
#     try:
#         name = input("Please enter your name: ")
#         assert name.isalpha(), "Haji jan, kodom esmi in sheklie !!!"
#
#         age = int(input("Please enter your age: "))
#         # assert age.isdecimal(), "Kodom agei in sheklie -_-"
#         # age = int(age)
#
#     except ValueError as message:
#         print("Eyyyyy khoda !!!")
#         input(message)
#
#     except KeyboardInterrupt:
#         print("\nSheitooni nakon bache !!!")
#         input("Entero bezan ta berim dobare biaim !")
#
#     except AssertionError as text:
#         print(text)
#         input("Enter kon dige !!!")
#
#     else:
#         print(f"Welcome {name}")
#         break
#
#     finally:
#         import os
#         os.system("cls" if os.name.lower() == "nt" else 'clear')

# Len vs Count
# numbers = [1, 2, 3, 3, 4]
# print(len(numbers))
# print(numbers.count(3))
# print(numbers.count())

# map:
# def printer(arg):
#     print(f"print: {arg}")


# for num in range(1, 11):
#     printer(num)

# map( item_1, item_2 )
# item_1 : Callable
# item_2 : Iterable ( Peimayesh pazir )

# list(map(lambda arg: print(f"print: {arg}"), range(1, 11)))
# args = list(map(lambda arg: f"Arg: {arg}", range(1, 11)))
# print(args)

# := operator --> Walrus
# Exit !
# if input("Confirm [Y/n]: ").strip().lower().startswith('n'):
#     exit()

import os


def banner(status):
    print(f"""-----------------------------
-       Python Script       -
-                           -
=>{status}=====================""")


commands = """     1. Get your ip address
     2. Get location
     3. Get os name

     0. Exit
"""


def cleaner():
    os.system("cls" if os.name.lower() == "nt" else 'clear')


def main():
    # clean screen
    cleaner()

    # print banner
    banner(" Main ")
    print(commands)

    # get command
    try:
        if cmd := int(input("\n > ")) == 1:
            cleaner()
            banner('  IP  ')
            print(f'IP: {os.popen("curl -s icanhazip.com").read()}\n')

        elif cmd == 2:
            cleaner()
            banner(' Loc  ')
            print(f'Location: {os.getcwd()}\n')

        elif cmd == 3:
            cleaner()
            banner('  OS  ')
            print(f'OS Name: {os.name}\n')

        elif cmd == 0:
            cleaner()
            banner(' Exit ')

            if input("Confirm [y/N]: ").strip().lower().startswith('y'):
                exit()
        else:
            cleaner()
            banner(' Error')
            print("Command not found !\n")

    except (ValueError, KeyboardInterrupt):
        cleaner()
        banner("Error ")
        print("Errorrorrorororororor -_- !")

    input("Press enter to continue ...")
    main()


# main()

def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)


# print(factorial(1))
# print(factorial(2))
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))

# from datetime import datetime
#
# now = datetime.now()
#
# keys = ['year', 'month', 'day', 'time']
#
# print(now.year)
#
# output_dict = {key: getattr(now, key) for key in keys}
#
# print(output_dict)
