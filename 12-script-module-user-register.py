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


if __name__ == '__main__':
    # Start scripting:

    counter = int(input("Please enter number of registration user:"))
    while counter > 0:
        print("\n-------- Register User --------\n")
        userpass = input("Username and password [user:pass]: ")
        User(*userpass.split(":"))
        counter -= 1

    print("\n\nRegistration Successful")
