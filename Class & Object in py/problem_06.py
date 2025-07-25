# write a program to create a classs and object to perform operations like withdraw , deposit , check balance
class BankAccount:
    def __init__(self,AccountName,AccountNumber,IfscCode,Balance):
        self.AccountName = AccountName
        self.AccountNumber = AccountNumber
        self.IfscCode = IfscCode
        self.Balance = Balance
    
    def withdraw(self,amount):
        self.Balance -= amount

    def deposit(self,amount):
        self.Balance += amount
    def CheckBalance(self):
        return self.Balance
    
object = BankAccount("hari prasad",9663258741,"BJU6321454",10000)

print(f"The current account balance is: {object.CheckBalance()}")
object.deposit(5000)
print(f"The current account balance after deposit is: {object.CheckBalance()}")
object.withdraw(3000)
print(f"The current account balance after withdrawal is: {object.CheckBalance()}")