import itertools

# 1: count
iter_counter = itertools.count(start=10, step=2)


class Count:
    def __init__(self, start=0, step=1):
        self.current = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current
        self.current += self.step
        return result


custom_counter = Count(10, 2)

# for _ in range(10):
#     print(next(iter_counter), next(custom_counter))
#
# for _ in range(10):
#     print(next(iter_counter), next(custom_counter))


# Cycle:
cycler = itertools.cycle(['A', 'B', 'C', 'D', 'E'])


class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.length = len(iterable)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.iterable[self.index]

        # self.index = _ if (_ := self.index + 1) < self.length else 0
        self.index = (self.index + 1) % self.length
        return result


custom_cycler = Cycle(['A', 'B', 'C', 'D', 'E'])

# for _ in range(30):
#     print(next(cycler), next(custom_cycler))

# for _ in range(30):
#     print(next(cycler), next(custom_cycler))

# 3. chain
chainer = itertools.chain([1, 2, 3], [10, 20, 30, 40, 50])
chain_cycler = itertools.cycle(chainer)


class Chain:
    def __init__(self, *iterables):
        self.iterables = iterables
        self.iter_index = 0
        self.current_iter = iter(iterables[self.iter_index])

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.current_iter)
        except StopIteration:
            self.iter_index += 1
            if self.iter_index >= len(self.iterables):
                raise StopIteration

            self.current_iter = iter(self.iterables[self.iter_index])
            return next(self.current_iter)


custom_chain = Chain([1, 2, 3], [10, 20, 30, 40, 50])

# for i in range(10):
#     print(next(chain_cycler))

# for i1, i2 in zip(chainer, custom_chain):
#     print(i1, i2)

# 4. slice

# slicer = itertools.islice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 100)
# slicer = itertools.islice([10, 20, 30, 40, 50, 60, 70, 80, 90][::-1], 3, 8, 2)
slicer = itertools.islice([10, 20, 30, 40, 50, 60, 70, 80, 90], 3, 8, 2)


class Slice:
    def __init__(self, iterable, start, stop, step=1):
        self.iterable = iterable
        self.stop = stop
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration

        result = self.iterable[self.current]
        self.current += self.step
        return result


custom_slicer = Slice([10, 20, 30, 40, 50, 60, 70, 80, 90], 3, 8, 2)

# for i1, i2 in zip(slicer, custom_slicer):
#     print(i1, i2)

combinations = itertools.combinations([1, 2, 3, 4, 5], 3)


def combinations_generator(iterable, r):
    data = list(range(r))

    yield tuple(iterable[i] for i in data)
    while True:
        for x in reversed(range(r)):
            if data[x] != x + len(iterable) - r:
                break
        else:
            return

        data[x] += 1
        for y in range(x + 1, r):
            data[y] = data[y - 1] + 1
        yield tuple(iterable[x] for x in data)


# for i in combinations:
for i in combinations_generator([1, 2, 3, 4, 5], 2):
    print(i)
