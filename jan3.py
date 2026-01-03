class student:
    college = "MRV"
    def __init__(self,name,rno,dept,fee):
        self.fee =fee
        self.name=name
        self.rno = rno
        self.dept=dept
    def payfee(self,amount):
        self.fee -= amount
        print(amount,"Paid succesfully")
        print("remaining fee:", self.fee)
        
s1=student("Avinash",186,"csd",130000)
s2=student("Rachu",187,"bba",100000)
s1.payfee(40000)
s2.payfee(10000)


class customer:
    bank = "SBI"
    def __init__(self,name,acno,balance):
        self.name=name
        self.acno=acno
        self.balance=balance
    def deposite(self,amount):
        self.balance += amount
        print(amount,"deposite succesfully")
        print("total balance:" ,self.balance) 
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insuficiant balane")
        else:
            self.balance -= amount
        print(amount,"withdraw succesfully")
        self.checkbalance()
        print("remaining balance:" ,self.balance) 
    def checkbalance(self):
        print("balance:",self.balance)    
c1=customer("Avinash",1234567889,7899)     
c1.deposite(800)     
c1.withdraw(90000) 
c1.checkbalance()