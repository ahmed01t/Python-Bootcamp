def conversion(f):
    c=5*(f-32)/9
    return c
f=int(input("enter temperature in fahrenhiet\n"))
a=conversion(f)
print(f"temperature is {round(a,2)}")