a=int(input("enetre a number"))
b=int(input("enetre a number"))
c=int(input("enetre a number"))
d=int(input("enetre a number"))
if a>b:
    if a>c:
        if a>d:
            print("a is max")
        else:
            print("d is max")
    else:
        if c>d:
            print("c is max")
        else:
            print("d is max")
else:
    if b>c:
        if b>d:
            print("b is max")
        else:
            print("d is max")
    else:
        if c>d:
            print("c is max")
        else: 
            print("d is max")
