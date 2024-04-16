class Sample:
    def __init__(self, value):
        self.value = value

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance


# init: Initialization
Sample(1)


class Parent:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, username):
        self.username = username
        print("Parent init called !")


class User(Parent):
    users = []

    def __new__(cls, username, password):
        for user in cls.users:
            if user.username == username:
                raise "Invalid Username !"
        print("before new")
        user = super().__new__(cls, username)
        print("after new")

        cls.users.append(user)
        return user

    def __init__(self, username, password):
        print("in init")
        self.username = username
        self.password = password


# ali = User("ali1289", "1234")
# admin = User("admin", "12345678")

# try:
    # admin2 = User("admin", "1234567890")
# except Exception:
    # pass

# print(User.users)
