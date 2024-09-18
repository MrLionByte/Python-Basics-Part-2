class Accounts:
    def __init__(self,name, balance, previous_balance=0) -> None:
        self.name = name
        self.__balance = balance
        self._previous_balance = previous_balance
    
    def deposit(self,amount):
        self._previous_balance = self.__balance
        self.__balance += amount
    
    def get_balance(self):
        return f"Balance is {self.__balance}"
    
    def __str__(self) -> str:
        return f"{self.name}'s balance is {self.__balance} and previous was {self._previous_balance}"

account = Accounts("alice",1)
print(account)
account.deposit(800)
print(account.get_balance())
print(account)