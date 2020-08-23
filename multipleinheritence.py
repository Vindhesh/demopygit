from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount():
        return 0
    @abstractmethod
    def authenticate():
        return 0
    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def deposit():
        return 0
    @abstractmethod
    def displayBalance():
        return 0
       
class SavingsAccount(Account):
    def __init__(self):
        self.savingAccounts = {}
    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000, 99999)
        self.savingAccounts[self.accountNumber] = [name, initialDeposit]
        print(f"Account creation successful, Your account number is ", self.accountNumber)

    def authenticate(self, name, accountNumber):
        if self.accountNumber in self.savingAccounts.keys():
            if self.savingAccounts[accountNumber][0] == name:
                print("Authentication Successful")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False


    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.savingAccounts[self.accountNumber][1]:
            print("Insufficient Balance")
        else:
            self.savingAccounts[self.accountNumber][1] -= withdrawalAmount
            print("Withdrawl was successful.")
            self.displayBalance()

    def deposit(self, depositAmount):
        self.savingAccounts[self.accountNumber][1] += depositAmount
        print("Deposit Successful")
        self.displayBalance()

    def displayBalance(self):
        print(f"Your account balance is:", self.savingAccounts[self.accountNumber][1])

savingsAccount = SavingsAccount()

while True:
    print(f" \n"
    "Enter 1 to create a new account\n"
        "Enter 2 to access an exisiting account\n"
        "Enter 3 to exit\n")
    userChoice = int(input())

    if userChoice == 1:
        name = input("Enter your Name: ")
        deposit = int(input("Enter initial deposit: "))
        savingsAccount.createAccount(name, deposit)

    elif userChoice == 2:
        name = input("Enter your Name: ")
        accountNumber = int(input("Enter your account Number: "))
        authenticationStatus = savingsAccount.authenticate(name, accountNumber)
        if authenticationStatus == True:
            while True:
                userChoice2 = int(input(f"\n"
                                        "Enter 1 to make a withdrawl\n"
                                        "Enter 2 to make a deposit\n"   
                                        "Enter 3 to display balance\n"
                                        "Enter 4 to go back to previos menu\n"))
                if userChoice2 == 1:
                    withdrawalAmount = int(input("Enter the amount you want to withdraw: "))
                    savingsAccount.withdraw(withdrawalAmount)
                if userChoice2 == 2:
                    depositAmount = int(input("Enter the amount you want to Deposit: "))
                    savingsAccount.deposit(depositAmount)
                if userChoice2 == 3:
                    savingsAccount.displayBalance()
                if userChoice2 == 4:
                    break
    elif userChoice == 3:
        print("Exiting the Banking program...")
        quit()


 
            



        


