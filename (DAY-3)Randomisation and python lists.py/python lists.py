cities=["lahore","islamabad","peshawar","rawalpindi","karachi"]
print(cities)
print(cities[-1])#last item in this list
cities[2]="KPK"
print(cities)
cities.extend(["sahiwal","okara"])#adds to the orignal list
cities.pop(0)
print(cities)