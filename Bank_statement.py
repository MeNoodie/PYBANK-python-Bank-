import random
class account:
    def __init__(self, bal_limit ):
        self.balance = random.randint(1000, bal_limit) # Setting a random initial balance within the limit
        self.account_no = random.randint(10000, 99999) # Setting a random account number within the limit

    #Debit method
    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            #self.balance = self.balance - amount
            self.balance -= amount
            print(f"Rs. {amount} debited from your account")
            print(f"Your account balance is Rs.",self.balance)

    #Credit method
    def credit(self, amount):
        #self.balance += amount
        self.balance = self.balance + amount
        print(f"Rs.{amount} credited to your account")   
        print("Your account balance is Rs.", self.balance)

    #Get balance method
    def get_balance(self):
        print("\nYour account balance is Rs.", self.balance)

#creating an account with a random balance limit
bal_limit = 50000 #maximum limit for intial balance
acc1 = account(bal_limit)
print(f"Your account number is {acc1.account_no}")
print(f"intial balance is Rs. {acc1.balance}")

# User input
while True:
    print("\nChoose an option:")
    print("1. Debit")
    print("2. Credit")
    print("3. Check Balance")
    print("4. Exit\n")
    choice = input("Enter your choice (1/2/3/4): ")


    if choice == "1":
        amount = float(input("Enter the amount to be debited: "))
        acc1.debit(amount)
    elif choice == "2":
        amount = float(input("Enter the amount to be credited: "))
        acc1.credit(amount)
    elif choice == "3":
        acc1.get_balance()
    elif choice == "4":
        print("Thank you for using our service")
    else:
        print("Invalid choice! Please try again.")
     