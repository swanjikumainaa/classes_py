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
    
    

class Account:
    account_type = "savings account"
    def __init__(self,name,account_number,balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        
        
    def deposit(self):
        deposit_amount=0    
        return f"You have deposited{deposit_amount},your new balance is {self.balance}+{deposit_amount}"
    
    def withdrawal(self):
        withdrawal_amount = 0  
        return f"You have withdrawn{withdrawal_amount}, your new balance is {self.balance}-{withdrawal_amount}"  
    
    def create_account(self):
        return f"Congratulations {self.name} on opening your {self.account_type}"
