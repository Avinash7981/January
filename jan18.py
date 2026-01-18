def print_num(n):
    if n==0 or n ==1:
        return 1
    return n * print_num(n-1)
print(print_num(6))    

def recursive_length(s):
    if s == "":
        return 0
    return 1 + recursive_length(s[1:])

# Example usage:
print(recursive_length("Avinash goud"))  # Output: 5




def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Example usage:
print(gcd(48, 18))  # Output: 6 





def print_num(n):
    if n > 0:
        print_num(n - 1)
        print(n)

# Example usage:
print_num(5)  # This will print 1 2 3 4 5 each on a new line



def print_num_desc(n):
    if n > 0:
        print(n)
        print_num_desc(n - 1)

# Example usage:
print_num_desc(5)  # This will print 5 4 3 2 1 each on a new line






def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n - 1)

# Example usage:
print(sum_natural(195))  # Output: 15

# ...existing code...


def reverse_string(s):
    if s == "":
        return s
    return reverse_string(s[1:]) + s[0]

# Example usage:
print(reverse_string("Avinash goud"))  # Output: duog hsahnivA 