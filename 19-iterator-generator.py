# iterable = [1, 2, 3, 4, 5]

# for number in iterable:
#     print(number)

# iterator = iter(iterable)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))  # 6


class EvenNumber:
    def __init__(self, maximum: int):
        self.maximum = maximum
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.maximum:
            raise StopIteration
        self.current += 2
        return self.current - 2


# for number in EvenNumber(20):


class Fibonacci:
    def __init__(self, maximum: int):
        self.maximum = maximum
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.maximum:
            raise StopIteration

        _ = self.a
        self.a, self.b = self.b, self.a + self.b
        return _


# fibo = Fibonacci(1000)
# for number in fibo:
#     print(number, end=" ")

class Combinations:
    def __init__(self, numbers_list: list):
        self.numbers = numbers_list
        self.temp = [0] * len(numbers_list)

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(len(self.numbers) - 1, -1, -1):
            if self.temp[i] == 0:
                self.temp[i] = 1
                return [self.numbers[j] for j in range(len(self.numbers)) if self.temp[j]]
            self.temp[i] = 0
        raise StopIteration


# combinations = [1, 2, 3]
# 3,2,1 | 2,1 | 3,1 | 1 | 3,2 | 2 | 3

# for comb in Combinations([1,2,3]):
#     print(comb, end="\n")

# def simple_generator():
#     yield 1
#     yield 2
#     yield 3


# gen = simple_generator()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


def even_numbers(maximum: int):
    current = 0
    while current <= maximum:
        yield current
        current += 2


# for number in even_numbers(20):
#     print(number)


def fibonacci_generator(maximum: int):
    a, b = 0, 1
    while a < maximum:
        yield a
        a, b = b, a + b


# for number in fibonacci_generator(50):
#     print(number, end=", ")


from time import perf_counter


# start = perf_counter()
# print(sum(i for i in range(10 ** 8)))
# print(f"{(perf_counter() - start)}")

# start = perf_counter()
# print(sum([i for i in range(10 ** 8)]))
# print(f"{(perf_counter() - start)}")

def generate_list(n):
    return [i for i in range(n)]


def generate_generator(n):
    for i in range(n):
        yield i


# start = perf_counter()
# _list = sum(generate_list(10 ** 6))
# end_time = perf_counter() - start
# print(f"List [ELapsed time]: {end_time}")

# start = perf_counter()
# _ = sum(generate_generator(10 ** 8))
# end_time = perf_counter() - start
# print(f"Generator [ELapsed time]: {end_time}")

