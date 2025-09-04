print("welcome to python pizza shop!\n")
size=input("what size do you want ? S,M or L\n")
peppporoni=input("do you want pepporoni on your pizza? Y or N\n")
extra_cheese=input("do you want extra cheese ? Y or N\n")
bill=0
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
else:
    print("you entered wrong inputs\n")
if peppporoni=="Y":
    if size=="S":
        bill+=2
    elif size=="M":
        bill+=3
    elif size=="L":
        bill+=4
else:
    bill+=0
if extra_cheese=="Y":
    bill+=5
else:
    bill+=0
print(f"your final bill is {bill}")