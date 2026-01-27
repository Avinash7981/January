#sum of 10 numbers
a = [1,2,3,4,5,6,7,8,9,10]
#.   0,1,2,3,4,5,6,7,8,9



# sum = 0
# for i in a:
#     sum += i 
# print(sum)    

#
# sum = 0
# for i in range(2,9):
#     sum += a[i]
# print(sum)    

queries = [(3,9),(4,9),(1,9),(3,8)]
#Time Complexity : 0(N*K)
#N is array size, k is queries. size 
#Space complexity : 0(1)
    
for m,n in queries:
    sum = 0
    for i in range(m,n+1):
        sum += a[i]
    print(sum)

# ============ HOW PYTHON MANAGES MIXED DATATYPES IN ONE LIST ============

# Python uses dynamic typing - each element is an object with its own type info
mixed_list = [42, "hello", 3.14, True, None, [1, 2], {"key": "value"}]

print("\n--- Mixed Data Types in One List ---")
for item in mixed_list:
    print(f"Value: {item:20} | Type: {type(item).__name__:10} | Size: {len(str(item))} chars")

# Type checking - Python stores type information with each element
print("\n--- Type Checking Each Element ---")
print(f"Element 0: {mixed_list[0]} -> {type(mixed_list[0])}")
print(f"Element 1: {mixed_list[1]} -> {type(mixed_list[1])}")

# You can operate on elements based on their type
print("\n--- Type-Specific Operations ---")
print(f"Integer operation: {mixed_list[0]} * 2 = {mixed_list[0] * 2}")
print(f"String operation: '{mixed_list[1]}'.upper() = '{mixed_list[1].upper()}'")
print(f"Float operation: {mixed_list[2]} + 1 = {mixed_list[2] + 1}")

# Safely check types before operations
print("\n--- Safe Type Operations ---")
for item in mixed_list:
    if isinstance(item, int):
        print(f"{item} is an integer, doubled: {item * 2}")
    elif isinstance(item, str):
        print(f"'{item}' is a string, length: {len(item)}")
    elif isinstance(item, list):
        print(f"{item} is a list with {len(item)} elements")    
