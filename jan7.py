num = int(input("Enter a two digit number: "))

#Ensure it's a two-digit number
if num < 10 or num >99:
    print("Not a two-digit number")
else:
    first_digit = num // 10
    second_digit = num % 10

    if num % 9 == 0 or first_digit == 9 or second_digit == 9:
        print("Lucky Number") 
    else:
        print("Unlucky Number")                                                

        
              
