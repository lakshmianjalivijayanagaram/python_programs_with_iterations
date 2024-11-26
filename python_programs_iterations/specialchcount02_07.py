#02-07-2024
#Write a program to find how many alphanumerical values are present in given sring.
s=input("enter a string ")
sc=0
for i in s:
    if not i.isalnum():
        sc+=1
print(sc)

#Process of Program
"""
ex: s="a*j@4i"

1.taking string as input i.e s
2.Assuming that there is no alphanumerical values are present in given input.
    so taking sc as 0 i.e sc=0
3.By using for loop fetching each and every element from given input.
    checking that element is special character or not.

i=1: it will fetch "a" so i=="a"
        checks not "a".isalnum() False.
i=2: it will fetch "*" so i=="*"
        checks not "*".isalnum() True. SO sc incremented from 0 to 1 i.e sc=1.
i=3: it will fetch "j" so i=="j"
        checks not "j".isalnum() False.
i=4: it will fetch "@" so i=="@"
        checks nt "@".isalnum() True. SO sc incremented from 1 to 2 i.e sc=2.
i=5: it will fetch "4" so i=="4"
        checks not "4".isalnum() False.
i=6: it will fetch "i" so i=="i"
        checks not "i".isalnum() False.

4.after completion of all the iterations of for loop
    print sc as 5 i.e sc=2.
"""


