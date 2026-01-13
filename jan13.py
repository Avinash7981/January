
def inverted_triangle(N):
  if (N>0):
     for i in range(N, 0, -1):
         for j in range(i):
             print("*", end="")
         print( )

         
inverted_triangle (int(input("enter N: ")))