class demo:
    a=4
o=demo()
o.a=0
print(o.a)
setattr(demo,'a','9')# setattr function
print(demo.a)