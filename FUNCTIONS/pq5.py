def pattern(n):
    if (n==0):
      return print("")
    print("*"*n)
    pattern(n-1)
    print(end="") 
pattern(5)