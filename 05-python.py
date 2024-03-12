# list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# tuple
tuple_numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9

# set
set_of_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 1, 1, 1, 1, 4, 4, 4, 4, 4}

set_of_numbers.add(9)
set_of_numbers.add(90)

set_of_numbers.update({
    1, 2, 3, 5, 6, 8, 100
})

# Short-Hands
# Ternary operators: (condition expression)

# a, b = 10, 20

# if a > b:
#     minimum = b
#     print(f"minimum: {b}")
# else:
#     minimum = a
#     print(f"minimum: {a}")

# minimum = b if a > b else a
# print(f"minimum: {b}" if a > b else f"minimum: {a}")

# a, b, c = 30, 20, 10

# if a < b and a < c:
#     minimum = a
# elif b < a and b < c:
#     minimum = b
# else:
#     minimum = c

# minimum = a if a < b and a < c else b if b < a and b < c else c

# print(minimum)

# Comprehension
# List Comprehension: (inline for)
# 1,100 -> step = 12

# print(list(range(1, 100+1, 12)))

# result = []
# i = 1
# while i <= 100:
#     result.append(i)
#     i += 12
#
# print(result)

# result = [i for i in range(1, 101)]
# print(result)

# fruits = ['mango', 'apple', 'limon', 'orange', 'banana', 'kiwi']

# result = []
# for fruit in fruits:
#     if 'a' in fruit:
#         result.append(fruit)

# print(result)

# print([fruit for fruit in fruits if 'a' in fruit])
# print([fruit if 'a' in fruit else '---' for fruit in fruits])

# Dict Comprehension:
numbers = [1, 2, 2, 3, 1, 23, 1, 2, 4, 5, 2, 3, 3, 6, 7]

# 1
count_of_numbers = {}

# for number in set(numbers):
#   if (count := numbers.count(number)) > 1 and (status := False):
#   if status := False and (count := numbers.count(number)) > 1:
#   if (count := numbers.count(number)) > 1:
#      count_of_numbers[number] = count

#   print(count)
#   print(status)

# print(count_of_numbers)

# print({number: count for number in set(numbers) if (count := numbers.count(number)) > 1})
# print({number: count if (count := numbers.count(number)) > 1 else count*10 for number in set(numbers)})

# inline-Functions = Lambda
# def power_plus_10(num):
#     return num * 2 + 10


# power_plus_10 = lambda num: num * 2 + 10
#
#
# print(power_plus_10(10))
# print(power_plus_10(100))
# print(power_plus_10(1100))

from time import time

start_time = time()
l1 = [i for i in range(1, 1_000_000_000, 10)]
end_time = time()
print(round(end_time - start_time, 8), "\n")


start_time = time()
l2 = (i for i in range(1, 1_000_000_000, 10))
end_time = time()
print(round(end_time - start_time, 8), "\n")
