# 2. Write a Python program to implement a class named BankAccount with the following requirements:
#   -> The class should contain two instance variables:
#       -> Name (Account holder name)
#       -> Amount (Account balance)
#   -> The class should contain one class variable:
#       -> ROT (Rate of Interest), initialized to 10.5
#   -> Define a constructor (init) that accepts Name and initial Amount.
#   -> Implement the following instance methods:
#       -> Display() - displays account holder name and current balance
#       -> Deposit() - accepts an amount from the user and adds it to balance
#       -> Withdraw() - accepts an amount from the user and subtracts it from balance (Ensure withdrawal 
#           is allowed only if sufficient balance exists)
#       -> CalculateInterest() - calculates and returns interest using formula
#           Interest = (Amount * ROT) / 100
#   -> Create Multiple objects to Demonstrate all methods

class BankAccount:
    ROT = 10.5

    def __init__(self, name, Initialamount):
        self.Name = name
        self.Amount = Initialamount

    def Display(self):
        print("Account Holder Name :", self.Name)
        print("Current Account Balanace :", self.Amount)

    def Deposite(self):
        print("Enter the Amount to Deposite :")
        Amt = float(input())

        self.Amount = self.Amount + Amt

    def Withdraw(self):
        print("Enter the Amount to Withdraw :")
        Amt = float(input())

        if(Amt > self.Amount):
            print("Unsufficient Balance")
            print("Please Enter sufficient Amount to Withdraw")
            return -1

        self.Amount = self.Amount - Amt

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROT) / 100
        return Interest

def main():
    obj1 = BankAccount("Aryan Dhumal", 200000000)
    obj2 = BankAccount("Pandharinath Dhumal", 400000000)
    
    obj1.Display()
    obj1.Deposite()
    obj1.Withdraw()
    print("Interest on amount is :",obj1.CalculateInterest())
    obj1.Display()

    obj2.Display()
    obj2.Deposite()
    obj2.Withdraw()
    print("Interest on amount is :",obj2.CalculateInterest())
    obj2.Display()

    print("End of main")

if __name__ == "__main__":
    main()