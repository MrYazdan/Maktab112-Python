# Built-in Functions:

# 1.
# print() # convert anything to str and print on screen

# 2.
# type()

# 3.
# len() # get length of data

# 4
# abs(-14)  # abstract

# 5
# from math import ceil, floor

# print(round(12.12345))
# print(round(12.12945, 2))
# print(round(12.12345, 20))
# print(round(12, 5))
# print(round(False, 3))
# print(round(True, 3))
# print(round(0.0239, 5))
# print(ceil(0.0239))
# print(floor(0.0239))

# String Formatting:
# print("0.0239".ljust(12, "0"))
# print(f"{0.0239:.10f}")

# 6
# print(sum((1, 2, 3, 4, 6), 10))
#
# result = 10  # start
# for i in (1, 2, 3, 4, 6):
#     result += i
#
# print(result)

# 7
# print(min(100, 10, 1, -10, 1000, 23))
# print(max(100, 10, 1, -10, 1000, 23))
# print(min([100, 10, 1, -10, 1000, 23]))
# print(max([100, 10, 1, -10, 1000, 23]))
# print(min([1, 2, 3, 4], (7, 8, 9)))  # Error !
# print(min([1, 2, 3, 4], (7, 8, 9), key=lambda x: len(x)))  # True
# print(min([1, 2, 3, 4], (7, 8, 9), key=lambda x: sum(x)))  # True

# 8
# numbers = [10, 34, 23, -1, 34]
# numbers.sort()  # numbers = sorted(numbers)

# print(sorted(numbers))
# print(numbers)

# 9
# Average
# user inputs : 12 13 18 19 10.5 15.75 20

# marks = input("> ")
# marks = marks.split()

# sum_of_marks = 0
# for mark in marks:
#     sum_of_marks += float(mark)

# print(f"Average: {sum_of_marks/len(marks)}")

# for i in range(len(marks)):
#     marks[i] = float(marks[i])
#
# print(f"Average: {sum(marks)/len(marks)}")

# Map =>
# marks = input("> ").split()
# print(f"Average: {sum(map(float, marks))/len(marks)}")
#

# for i in map(float, marks):
#     print(i)

# print(print(123))
#
# print("Map in print :", list(map(print, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# print("Map in print :", list(map(float, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# numbers = [
#     [1, 2, 3, 4, 10],
#     [10, 20, 30],
#     [10, 200]
# ]

# print(sum(map(sum, numbers)))

# 10
# add = lambda a, b: a + b

# print(callable(add))
# print(add(10, 20))

# 11
# numbers = [1, 10, 100, 1000, 2, 20, 200, 2000]

# formula = (i ** 5)/ i * 3.14
# for number in numbers:
#     numbers[numbers.index(number)] = (number ** 5) / number * 3.14

# print(numbers)

# print(list(map(lambda i: round(((i ** 5) / (i * 3.14)) % 100), numbers)))
# print(list(filter(lambda i: round(((i ** 5) / (i * 3.14)) % 100) % 2 == 0, numbers)))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # even_numbers = list(map(lambda n: n % 2 == 0, numbers))
# even_numbers = list(map(lambda n: n if n % 2 == 0 else None, numbers))
# odd_numbers = list(map(lambda n: n % 2 != 0, numbers))
#
# print(even_numbers)
# print(odd_numbers)
#
# even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
# odd_numbers = list(filter(lambda n: n % 2 != 0, numbers))
#
# print(even_numbers)
# print(odd_numbers)

text = "salam be rooye mahetoon"

# print("".join(map(lambda char: char.upper() if text.index(char) % 2 == 0 else char, text)))
# print("".join(map(lambda i: text[i].upper() if i % 2 == 0 else text[i], range(len(text)))))

# 12
# from functools import reduce  # noqa
#
# print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5, 6]))

# 13
# print(True and True and False)
# print(all([True, True, False]))

# 14
# print(True or True or False)
# print(any([True, True, []]))

# 15
# print(reversed(text))
# print("".join(reversed(text)))

# 16
# print(list(enumerate('abcdefg')))
# print("".join(map(lambda t: t[1].upper() if t[0] % 2 == 0 else t[1], enumerate(text))))

# for i, v in enumerate(text):
#     print(f"index: {i} - value: {v}")


# 17
# print(list(zip('salam', 'bye', [1, 2, 3, 4, 5])))

# """
#   1: a, I, ۱
#   2: b, II, ۲
#   3: c, III, ۳
#
# """

en_alpha = "abcdefgh"
fa_nums = "۰۱۲۳۴۵۶۷۸۹"

# for i in range(3):
#     print(f"{i + 1}: {en_alpha[i]}, {(i + 1) * 'I'}, {fa_nums[i]}")

for en_num, fa_char in zip(range(0, 10), fa_nums):
    print(f"{en_num}, {fa_char}")
