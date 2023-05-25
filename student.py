class Student:
    school = "AkiraChix"
    def __init__(self,first_name,second_name,third_name,age,nationality):
        self.first_name = first_name
        self.second_name = second_name 
        self.third_name = third_name   
        self.age = age
        self.nationality = nationality

        # Methods are used to add behaviours to the class atributes.
        # We use python normal functions to add these behaviours


    def greet_student(self):
        return f"Hello {self.first_name},welcome to {self.school}"
    
    def year_of_birth(self):
        year = 2023-self.age
        return f"Hello{self.first_name}, you were born in {year}"
    # Update the Student Class to include these attributes - first_name, last_name, age, country
    #  - Add these method to the Student class
    #          - show_full_name
    #          - year_of_birth
           
    def show_initials(self):
        return f"Hello,{self.first_name},your initials are, {self.first_name[0]}.{self.third_name[0]}"
    
    
class Car:
    wheels = 4
    def __init__(self,make,model,mileage):
        self.make = make
        self.model = model
        self.mileage = mileage
        
    def move(self):
        return f"{self.make}, {self.model} is now moving" 
    
    def hoot(self):
        return f"peeeeeeeepppeeeeepeeeeepeee!!!!"  
    
    def fueling(self):
        return f"The price of,{self.make}, {self.model} is {self.mileage}*180"
    
    

class Fruit:
    shelf_life = 5  
    def __init__(self,name,color, country ):
        self.name = name
        self.color = color
        self.country = country
    
    def expiry_date(self):
        return f"{self.name}'s expiry date is {self.shelf_life}" 
    
    def origin(self):
        return f"{self.name} is from {self.country}" 
    
    def buy(self):
        return f"You have bought a {self.color} {self.name} from {self.country}" 
    
    

# class Account:
#     account_type = "savings account"
#     def __init__(self,name,account_number,balance):
#         self.name = name
#         self.account_number = account_number
#         self.balance = balance
        
        
#     def deposit(self):
#         deposit_amount=0    
#         return f"You have deposited{deposit_amount},your new balance is {self.balance}+{deposit_amount}"
    
#     def withdrawal(self):
#         withdrawal_amount = 0  
#         return f"You have withdrawn{withdrawal_amount}, your new balance is {self.balance}-{withdrawal_amount}"  
    
#     def create_account(self):
#         return f"Congratulations {self.name} on opening your {self.account_type}"

class Account:
    balance=20000
    def __init__(self,name,number,balance):
        self.name=name
        self.number=number
        self.balance=balance
#Add these attributes and behaviours to the class Account
#Add attributes deposits and withdrawals in the init method which are empty lists
#by default and another attribute loan_balance which is zero by default.
        self.deposits=[]
        self.withdrawals=[]
        self.loan_balance=0
    def get_new_balance(self):
        return self.balance+self.deposits
    def get_details(self):
        return f"The owner of Account{self.number} is {self.name}."
    def confirm(self):
        return f"{self.name} is a KCB customer."
# Add a method check_balance which returns the account’s balance
    def check_balance(self):
        return self.balance
# Update the deposit method to append each withdrawal transaction to the deposits list.
#  Each transaction should be in form of a dictionary like this
# {
#    "amount": amount,
#    "narration": “deposit”
# }
    def check_deposit(self,amount):
        transaction = {"amount": amount, "narration": "deposit"}
        deposit_list=self.deposits.append(transaction)
        return deposit_list
# Update the withdrawal method to append each withdrawal transaction to the withdrawals list.
# Each transaction should be in form of a dictionary like like this
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }
    def check_withdraw(self, amount2):
        transaction2 = {"amount": amount2, "narration": "withdrawal"}
        withdrawal_list=self.withdrawals.append(transaction2)
        return withdrawal_list
# Add a new method  print_statement which combines both deposits and withdrawals into one list and,
# using a for loop, prints each transaction in a new line like this
# deposit - 1000
# withdrawal - 500
    def print_statement(self):
        combined_list=self.deposits+self.withdrawals
        print(combined_list)
        for c in combined_list:
            print(f"{c['narration']} - {c['amount']}")
# Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount
    def borrow_loan(self,loan_amount):
        total_deposits = sum(transaction["amount"] for transaction in self.deposits)
        if self.loan_balance==0 and loan_amount>100 and len(self.deposits)>=10 and loan_amount > total_deposits / 3:
           return
        self.loan_balance+=loan_amount
        self.balance+=loan_amount
# Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the accounts current balance
    def repay_loan(self,amount):
        self.loan_balance-=amount
        if amount>self.loan_balance:
            extra=self.loan_balance-amount
            self.balance+=extra
# Add a transfer method which accepts two attributes (amount and instance of another account).
# If the amount is less than the current instances balance, the method transfers the requested amount from the
# current account to the passed account. The transfer is accomplished by reducing the current account balance
# and depositing the requested amount to the passed account.
    def transfer(self,amount,other_account):
        other_account=Account
        if self.balance> amount:
            return
        self.balance -= amount
        other_account.check_deposit
