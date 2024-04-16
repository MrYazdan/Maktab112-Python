import os
user_module = __import__("12-script-module-user-register")


get_ip_link = "https://icanhazip.com"


def get_ip_in_linux():
    return os.popen(f"curl -s {get_ip_link}").read()


def say_hello(name):
    print(f"Hello, {name.title()}")


def registration_user():
    username = input("Please enter username: ")
    password = input("Please enter password: ")
    return user_module.User(username, password)
