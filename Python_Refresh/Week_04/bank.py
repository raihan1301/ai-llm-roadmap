class Account_Class:
    def __init__(self):
        self._balance = 0

    @property  # this is getter function
    def balance_prop(self):
        return self._balance  # this will initiate the init function
    

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -=n


def main():
    account = Account_Class()
    print("Balance: ", account.balance_prop)
    
    account.deposit(100)
    account.withdraw(50)

    print("Balance: ", account.balance_prop)


if __name__ == "__main__":
    main()
