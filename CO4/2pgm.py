class Bank:
    def_init_(self,accNo,name,accType,balance=0):
        self.accNo=accNo
        self.name=name
        self.accType=accType
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposit successful!New balance:{self.balance}")
        else:
            print("Invalid deposit amount.Enter a positive value.")
        
