g = input("Enter a single letter: ").lower()

if len(g) == 1 and f.isalpha():
   
    if g in 'aeiou':
        print(f"{g} is a vowel.")
    else:
        print(f"{g} is not a vowel.")
else:
    print("Invalid input. Please enter a single letter.")
print("program end")


