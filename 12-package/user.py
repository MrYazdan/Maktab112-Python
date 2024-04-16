class User:
    users = []

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.__class__.users.append(self)

    @classmethod
    def login(cls, username, password):
        for user in cls.users:
            if user.username == username and user.password == password:
                return user

        raise ValueError("Invalid username or password")

