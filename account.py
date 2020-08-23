class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def credit(self, deposit):
        self.balance = self.balance + deposit
        # print(f" The balance in the account of {self.name()} has been updated to {self.balance()}")


    def debit(self, withdrawl):
        self.balance = self.balance - withdrawl
        # print(f" The balance in the account of {self.name()} has been updated to {self.balance()}")
    
    # def get_balance(self):
    #     return self.balance
    #     print(f"The balance in the account of", self.name(), "is :", self.balance())

    # def get_name(self):
    #     return self.name
    #     # print(f"The name of the customer is {self.name()}")

    # def set_name(self, name):
    #     self.name = name
    #     # print(f"The name of the account holder has been updated to {self.name}")

account = Account("Vindhesh", 1000)
print("The balance in account of", account.name, "is", account.balance)

account.credit(500)
print("The balance in account of", account.name, "is updated to ", account.balance)

account.debit(200)
print("The balance in account of", account.name, "is updated to ", account.balance)

account.name = "Aditi"
print("The account user name has been updated as", account.name, "and the balance is", account.balance)
