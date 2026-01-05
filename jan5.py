class addition:
    def add(self,a,b,c=None):
        if not c:
            return a+b
        else:
            return a*b*c
a=addition()
print(a.add(4,6))
print(a.add(4,5,6))        




class greeting:
    def greet(self,name=None):
        if not name:
            return "Wellcome GUEST"
        else:
            return f"Wellcome {name}"
a=greeting()
print(a.greet())
print(a.greet("Avinash"))      



class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def deposit(self,amount):
        self.__balance += amount
    def checkbalance(self):
        return self.__balance
b=BankAccount("Avinash",100000)
print(b.checkbalance())
b.deposit(10000)
print(b.checkbalance())    



from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def area(self,r):
        return 3.14*r*r    
class rectangle(shape):
    def area(self,l,b):
        return 3.14*r*r  
c=circle()
r=rectangle()
print(c.area(5)) 



print(r.area())      







class car:
    wheels=4
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"color: {self.color}")    
        print(f"wheels: {car.wheels}")
car1 = car("Toyata","red")
car2 = car("BMW","Blue")   
car1.display_info() 
print()
car2.display_info()    
print("\nAll cars have", car.wheels, "wheels")
