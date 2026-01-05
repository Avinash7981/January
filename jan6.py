class student:
    def __init__(self, name,age):
        self.name=name
        self.age=age

c= student("Avinash",18)
print(c.name)
print(c.age)

    



class animal:
    def __init__(self):
        self._type="Unknown"
class dog(animal):
    def __init__(self):
        super().__init__()
        self._type="dog" 
dog = dog()
print(dog._type)


        

class BankAccount:
    def __init__(self):
        self.__balance=0

    def deposite(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance   


account=BankAccount() 
account.deposite(50000)
print("balance:",account.get_balance()) #Accessing private method
        

class Animal:
    name=""
    def eat (self):
        print("I can eat")
# inherit from Animal
class Dog(Animal):
    def display(self):
        print("My name is ", self.name)


labrador = Dog()
labrador.name = "Jimmy"
labrador.eat ()
# call subclass method
labrador.display()
    





class Student:
    def __init__(self, name, roll_number, dept):
        self.name= name       #Instance attribute 1
        self.roll_number = roll_number # Instance attribute 2
        self.dept = dept   #Instance attribute 3



    def display_details(self):
        print("Student Details:")
        print(f"Name: {self. name}")
        print(f"Ro11 Number: {self.roll_number}")
        print(f"Dept: {self. dept}")
        print("-" * 30)
student1 = Student(name="John", roll_number="A101", dept="AIML")
print("Displaying Details for Student 1")
student1.display_details()


student2 = Student(name="Bob", roll_number="C205", dept="CSE")
print("\nDisplaying Details for Student 2")
student2.display_details()