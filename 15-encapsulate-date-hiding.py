class BankAccount:
    def __init__(self, name):
        self.name = name
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self.__balance += amount
            self.__atm_print()
            return True
        raise ValueError("Amount must be int or float type !")

    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and 0 <= amount <= self.balance:
            self.__balance -= amount
            self.__atm_print()
            return True
        raise ValueError("Amount must be int or float type !")

    def __atm_print(self):
        print("BALANCE :", self.balance)


maktab_sharif_account = BankAccount("Maktab Sharif")
maktab_sharif_account.deposit(1_000_000)
# print(maktab_sharif_account.balance)
# maktab_sharif_account.balance = 100_000_000_000
# print(maktab_sharif_account.balance)

_reza_account = BankAccount("Reza Yazdani")
__sina_account = BankAccount("Sina Maleki")
__amir_account__ = BankAccount("Amirhossein Pak-del")
# maktab_sharif_account.__atm_print()

maktab_sharif_account.withdraw(5000)
