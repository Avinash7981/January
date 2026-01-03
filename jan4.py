class Father():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    haircolor = "Black"
    def work(self):
        return "I will work 10h a day"
class Son(Father):
    def __init__(self,fname,lname,nick):
        super().__init__(fname,lname)
        self.nick=nick
    haircolor = "Pink"   
    def work(self):
       print(super().work())
       return "I dont want to work"
f=Father("Nagarguna","Akkineni")
s=Son("Akhil","Akkineni","Chimtu")
print(f.work())
print(s.work())    
    