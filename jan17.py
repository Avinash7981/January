'''def calculate_discount(price,discount_present):
    discount_amount = (price/100)*discount_p
    final_price = price - discount_amount
    return final_price
print(calculate_discount(1000,10))'''

#by using Function 10% discount
def calculate_discount(price,discount_present):

    return price-((price)*(discount_present/100))

print(calculate_discount(1000,10))



'''
#by using Function Voting elegibility
def can_vote(age):
    return age>=18
print(can_vote(19))'''

#by using Function right angle triangle
def print_triangle(n):
    for i in range(1,n+1):
        print('*'*i)
print_triangle(5)




#by using Function calculator
def calculato(a,b,operation):
    if operation == 'add':
     return a+b
    elif operation == 'subtract':
       return a-b
    elif operation == 'multiply':
       return a*b
    elif operation == 'divide':
       return a/b
    else:
       return 'invalid operation'
print(calculato(10,2,'multiply'))   

# by using function grades
def get_grade(operation):
    if operation >=90:
     return 'A'
    elif operation >=80:
       return 'B'
    elif operation >=70:
       return "c"
    elif operation >=60:
       return "d"

    else:
       return 'fail'
print(get_grade(89))



#by using  Function Leap Year
def is_leapyear(year):
    return (year%4==0 and year%100!=0)or (year%400==0)
print(is_leapyear(2021))

def is_palindrome(word):
    return word==word[::-1]
print(is_palindrome("level"))