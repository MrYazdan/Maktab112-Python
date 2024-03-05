# marks = [10, 20, 12, 15]
# marks = [
#     [15, 15, 20],  # math
#     [14, 12, 16],  # history
# ]

from pprint import pprint

marks = {
    # "math": [
    #     15, 15, 20
    # ],
    #
    "math": {
        "final": 18,
        "mid": 17,
        "class": 20,
        "quiz": 17
    },
    "history": {
        "final": 18,
        "mid": 17,
        "class": 20
    },
    "chemistry": {
        "final": 18,
        "mid": 17,
        "class": 20
    },
    '0': "zero"
}

# pprint(marks)
# print(marks["math"])
# print(marks["physic"]) # KeyError
# print(marks[0])
# print(marks['math']['final'])
# print(marks.get('math').get('final'))
# print(marks.get('math', None))
# print(marks.get('physic', {}))
# print(marks['math'].get("sample"))
# print(marks["quiz"])

# Methods
# marks.clear()

# chemistry:
# marks["chemistry"].clear()
# marks["chemistry"]['final'] = None
# del marks["chemistry"]['final']

# copy_of_marks = marks.copy()
# print(marks.keys())
# pprint(marks.values())
# print(marks.items())

# math = marks.pop('math')
# print(math)

# del marks['math']
# last_item = marks.popitem()
#
# print(last_item[0])
# print(last_item[1])

# print(len(marks))
#
# item_key, item_value = marks.popitem()
#
# print(item_key, item_value)
# pprint(marks, sort_dicts=False)
#
# print(marks.get('math'))
# print(marks.keys())

# marks += {
#     1: "one",
#     2: "two"
# } # error !

# marks[1] = "one"
# marks[2] = "two"

# update:
marks.update({
    '1': "one",
    '2': "two"
})

# marks.update({})

# pprint(marks, sort_dicts=False)

# print(list(marks))
# print(sorted(marks))

# print('math' in marks)
# print('zero' in marks)
# print('zero' in marks.keys())

# Mutable - changeable
marks['1'] = "One"

# Tuple:

# ImMutable - UnChangeable - Ordered - Duplicate
# numbers = (1, 2, 3, 4, 5, 6)
numbers = 1, 2, 3, 1, 1, 1, 2
# numbers = [1, 2, 3, 4]
# numbers[0] = 1 # error
# print(numbers[2:7])
# print(numbers)
# print(type(numbers))
# print(numbers.index(3))
# print(numbers.count(1))

name = "reza"

print("name: %s" % name)
print("name: " + name)
print("name: {}".format(name))  # deprecate !
print(f"name: {name}")
# print(f"name: {name:.^10}")

# ----------------------------
# list-comprehension
# dict-comprehension
# generator-comprehension
# ternary-operator
