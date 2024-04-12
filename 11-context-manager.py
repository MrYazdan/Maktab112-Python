# file = open("./LICENSE", 'a+')
#
# try:
#     # file write
#     # file read
#     pass
# finally:
#     file.close()

# with open("./LICENSE", 'r') as file:
#     pass


# Context Manager !!!
# from contextlib import contextmanager


# @contextmanager
# def editor(file_path, mode="r"):
#     file = open(file_path, mode)
#     yield file
#     file.close()
#
#
# with editor('./LICENSE', "r") as file:
#
#     for index, line in enumerate(file.readlines()):
#         print(index + 1, line, end="")


class Editor:
    def __init__(self, path, mode='r'):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


# with Editor('./LICENSE', "r") as file:
#     for index, line in enumerate(file.readlines()):
#         print(index + 1, line, end="")


class Calculator:
    def __init__(self):
        self.result = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.result)

    def process(self, exp):
        self.result += eval(exp)


with Calculator() as calculator:
    calculator.process("10 + 100")
    calculator.process("100 - 1000")
    calculator.process("10 * 90")
