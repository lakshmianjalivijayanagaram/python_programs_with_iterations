#02-07-2024
#Write a program to find how many alphanumerical values are present in given sring.
s=input("enter a string ")
ac=0
for i in s:
    if i.isalnum():
        ac+=1
print(ac)

#Process of Program
"""
ex: s="anj@4i"

1.taking string as input i.e s
2.Assuming that there is no alphanumerical values are present in given input.
    so taking ac as 0 i.e ac=0
3.By using for loop fetching each and every element from given input.
    checking that element is alphanumerical or not.

i=1: it will fetch "a" so i=="a"
        checks "a".isalnum() True. SO ac incremented from 0 to 1 i.e ac=1.
i=2: it will fetch "n" so i=="n"
        checks "n".isalnum() True. SO ac incremented from 1 to 2 i.e ac=2.
i=3: it will fetch "j" so i=="j"
        checks "j".isalnum() True. SO ac incremented from 2 to 3 i.e ac=3
i=4: it will fetch "@" so i=="@"
        checks "@".isalnum() False.
i=5: it will fetch "4" so i=="4"
        checks "4".isalnum() True. SO ac incremented from 3 to 4 i.e ac=4.
i=6: it will fetch "i" so i=="i"
        checks "i".isalnum() True. SO ac incremented from 4 to 5 i.e ac=5.

4.after completion of all the iterations of for loop
    print ac as 5 i.e ac=5.
"""

