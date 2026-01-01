
#return the sum of two numbers
def sumoftwonumbers(a,b):
    return a + b
x = sumoftwonumbers(5, 10)
print(x)


#return true if the number is even else false 
def is_even(n):
    if n % 2 == 0:
        return True 
    else:
        return False
    
y=is_even(7)
print(y)


#Write a function greet name
def greet_name(name):
    return "Hello, "+ name + "!"
z=greet_name("Avinash")
print(z)



#Returns the larger of the two numbers without using max().
def larger_number(a,b):
    if a > b:
        return a
    else:
        return b    
a = larger_number(15,10)
print(a)   





#Returns how many vowels (a, e, i, o, u) are present in the string.
def count_vowels(b):
    count=0
    for i in b:
        if i in "aeiouAEIOU":
            count += 1
    return count
print(count_vowels("Avinash"))    


#positional argumets 
def sumofsquares(a,b):
    return a*a+b*b
sumofsquares(4,5)


#keyword arguments 
def sumofsquares(a,b):
    return a*a+b*b









