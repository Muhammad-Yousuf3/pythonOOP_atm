class Atm:
    def __init__(self):
        self.pin=1234
        self.balance=1000

    def check_pin(self,entered_pin):
        return entered_pin == self.pin
    
    def check_balance(self):
        print(f"Your Balance is : {self.balance}")

    def deposit(self,amount):
        amount += self.balance
        print(f"Rs {amount} Deposited Successfully.")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        
        else:
            self.balance -= amount
            print(f"Rs {amount} Withdrawn Successfully.")

    def exit(self):
        print("Thank You for using the ATM. GoodBye!")


atm=Atm()
print("Welcome to Yousuf's ATM.")

entered_pin=int(input("Enter your 4 digit Pin : "))

if atm.check_pin(entered_pin):
    while True:
        print("\nChoose an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice=int(input("Please Choose a number from 1 to 4 : "))

        if choice == 1:
            atm.check_balance()

        elif choice == 2:
            amount = int(input("Enter amount to deposit: Rs "))
            atm.deposit(amount)

        elif choice == 3:
            amount = int(input("Enter amount to withdraw: Rs "))
            atm.withdraw(amount)

        elif choice == 4:
            atm.exit()
            break

        else:
            print("Invalid Option. Please Try Again!")

else:
    print("Incorrect PIN. Access Denied.")

