class GrandFather:
    pass
    # def hi(self):
    #     # super().hi()
    #     print("Hi baby 👨🏻‍🦳 ")


class Father(GrandFather):
    def hi(self):
        # super().hi()
        print("Hi baby 👨🏻 ")


class Mother(GrandFather):
    def hi(self):
        # super().hi()
        print("Hi baby 👩🏼 ")


class Child(Father, Mother):
    def hi(self):
        super().hi()
        print("Hi 🙃 ")


# junior = Child()
# junior.hi()


class One:
    def hi(self):
        # super().hi()
        print("Hi 1 ")


class Two:
    def hi(self):
        # super().hi()
        print("Hi 2 ")


class Three:
    def hi(self):
        print("Hi 3 ")


class Four(One, Two):
    def hi(self):
        super().hi()
        print("Hi 4 ")


class Five(Two, Three):
    def hi(self):
        super().hi()
        print("Hi 5 ")


class Six(Four, Five):
    def hi(self):
        super().hi()
        print("Hi 6 ")


# Six().hi()
# print(*Six.__mro__, sep="\n")


class O:
    pass


class D(O):
    pass


class E(O):
    pass


class F(O):
    pass


class B(D, E):
    pass


class C(D, F):
    pass


class A(B, C):
    pass


print(*A.mro(), sep="\n")
