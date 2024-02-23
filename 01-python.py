# * = Any --> *() -> callable
# i/o -> input:
# name = input("Please enter your name: ")

# output:
# print(name)

# Data Type (1):
# str:
# name = 'maktab 112'
# print(type(name))

# int
# age = 19
# print(type(age))

# bool -> True, False !
# is_active = False
# print(type(is_active))

# float ->
# mark = 18.45
# print(type(mark))

# variables:
# EmAil = "isMrYazdan@gmail.com"
# ___phone = "09123456789"
# Fitst-name = "Reza Yazdani" # Error
# MsgToAdmin = "Hi Admin :)" # msg_to_admin
# 16to2BitConvert = 010110 # Error

# tempory = _
# _ = "Hello World"

# float = 1.2323 # keyword -> Not Recommended
# input = "alireza" # keyword -> Not Recommended
# str = 'alireza' # keyword -> Not Recommended
# class = 123123
# top+ = "bottom"
# !top = "bottom"

# output:
# print("Salam maktabia")
# print("Salam", "maktabia", sep="||")
# print("Salam" + "maktabia", name, sep="...")
# print("salam be hame:\n---------------\n\n\tA: 10\n\tB: 20")
# print(name, end="\n")
# print(age, end=" | ")
# print(is_active, end=" | ")

# print("address pycharm: C:\\Users\\Default\\Desktop")
# print("shoma\tbayad beri \"tehran\"")


# Type Casting
# name = 'maktab 112'
# number = '00000112'
# age = 19
# is_active = False
# mark = 18.95

# print(int(mark))  # => 18
# print(float(age))  # => 19.0

# print(int(name)) # Error
# print(int(number))
# print(str(mark))

# print(bool(0))
# print(bool(-12310))
# print(float('123-23'))

# None
# print(None)
# print(type(None))
# print(bool(None))
# print(False == None)
# print(bool('') == bool(None))

# Example:
# > 12.5
# > 3
# Multi = 37.5
# n1 = float(input("> "))
# n2 = float(input("> "))
# print(n1 * n2)

# Operators:
# Mathematics: + - / * ** % //
# n1 = 10
# n2 = 2

# print(10 + 10)
# print(10 - 10)
# print(10 / 10)
# print(10 * 10)
# print(2 ** 3)
# print(10 % 3)
# print(10 // 3) # Floor division

# Assignment Operator: = += -= *= /=
# x = 5
# x += 5  # x = x + 5
# x -= 5  # x = x - 5
# x *= 5  # x = x * 5

# x **= 2  # x = 5 ** 2
# x //= 2  # x = 5 // 2

# print(x)

# Comparison Operator -> bool
# : == > < >= <= !=
# x = 12
# y = 10

# print(x == y)  # False
# print(x > y)  # True
# print(x < y)  # False
# print(x <= y)  # False
# print(x >= y)  # True
# print(x != y)  # True

# x = 0
# y = 2

# print(-y ** 3 * x + 1 > 10)

# Condition
# age = int(input("Age: "))
#
# if 100 >= age >= 18:
#     print("Access Allowed, age:", age)
# elif age > 100:
#     print("Joke !!!")
# else:
#     print("Access Denied, age:", age)

# Logical Operators:
# : and ,or ,not

# '' and 12 => '' : False
# 10 and '' => '' : False
# 10 and '' and 54 => '' : False
# 10 or False => 10 : True
# None or False or 12 => 12 : True
# 10 or 23 or 12 => 10 : True

# String:
# print("ali" + "reza" )
# print("ali" * 3)

# case:
# msgToSina => Camel Case
# MsgToSina => Pascal Case
# msg_to_sina => Snake Sase

# print("ALIREZA".lower())
# print("ALIREZA".upper())
# print("ALIREZA".title())
# print("ALIREZA".count('A'))
# print("ALIREZA".count('a'))
# print("ALIREZA".split(sep="L"))  # list
# print("ALIREZA".islower())
# print("ALIREZA".isupper())
# print("123123".isnumeric())
# print("123123".isnumeric())
# print("123123".isdecimal())
# print("۱۲۳۴۴۵۴".isdecimal())
# print("123123".isdigit())
# print("123123".isdigit())
# print("salam chetory".startswith('salam'))
# print("salam chetory".endswith('salam'))

text = "Hello world!!!"
# print(text[0])
# print(text[1:3])  # [1:3)
# print(text[2:4])
# print(text[0:2])
# print(text[:2])
# print(text[2:])
# print(text[-2:])
# print(text[-2:-1])
# print(text[:-2])
# print(text[:-2:2])
# print(text[-2:2:-2])
# print(text[::-1])
# print(text[::-1][::-1])
# print(len(text))

# Exists operator:
# print('Hello' in text)
# print('bye' not in text)

# List:
# numbers = [1, 2, 67, "98348923465", 23, 2, 12, 32]
# print(numbers[1])
# print(numbers[50])
# print(numbers.count(2))
# print(len(numbers))
# print(numbers[3].isnumeric())

numbers = []

numbers.append(12)
numbers.append(123)
numbers.append(1234)
numbers.append(12345)
numbers.insert(0, 1)
numbers.insert(len(numbers), 1234567)

# numbers += [12345678, 123456789]
# numbers.append([12345678, 123456789])

# numbers += "1324123"

# numbers.pop
# numbers.remove

print(numbers)

# while
# for
# print(sum(numbers))

# _sum = 0
# while numbers:
#     value = numbers.pop(0)
#     _sum += value
#
#     print(value)
#
# print(_sum)


# for i in range(0, 12):
#     print(i)

for number in numbers:
    print(number)
