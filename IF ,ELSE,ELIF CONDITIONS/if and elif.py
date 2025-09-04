print("welcome to the roller coster\n")
height=int(input("please enter your height sir\n"))
if height>=120:
    print("you can ride sir\n")
    age=int(input("enter your age\n "))
    if age<=12:
    print("pay 5 dollars\n")
    elif age<=18:
    print("pay 10 dollar\n")
    else:
    print("pay 20 dollar")
else:
    print("you cannot ride\n")