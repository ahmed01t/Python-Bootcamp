print("Welcome To The Tip Calculator !")
bill=float(input("what is your total bill?\n"))
tip=int(input("how much tip you like to give?\n"))
split=int(input("how many people to split the bill?\n"))
tip_percent=tip/100
total_bill=bill+(bill*tip_percent)
final_bill=total_bill/split
print(f"each person should pay :{final_bill:.2f}$ ")
