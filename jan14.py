def hollow_pyramid(N):
  if (N>0):
     for i in range(1, N + 1):
       print(" " * (N - i), end="")
       if i == 1:
          print("*")
       elif i == N:
          print("*" * (2 * N - 1))
       else:
          print("*", end="")
          print(" " * (2 * i - 3), end="")
          print("*")
hollow_pyramid (int(input("enter N: ")))