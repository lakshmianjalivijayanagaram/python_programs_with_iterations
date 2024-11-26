#02-07-2024
#Write a program to find the sum of even digits and sum of odd digits present in a given string
s=input("enter a string ")
es=0
os=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            es+=k
        else:
            os+=k
print(es)
print(os)

#Process of Program
"""
ex: s="a12n4"

1.taking string as input i.e s
2.Assuming that there is no digits present in given input.so taking evensum as 0 and oddsum as 0
    i.e es=0 and os=0
3.By using for loop fetching each and every element from given input.
    checking that element is digit or not
    
i=1: it will fetch "a" so i=='a'
        checks 'a'.isdigit() False
i=2: it will fetch "1" so i=='1'
        checks '1'.isdigit() True .% is performed only between digits.so type cast out string input into int.
        Now checks 1%2==0 False. so, os is incremented from 0 to 1.  i.e os=1
i=3: it will fetch "2" so i=='2'
        checks '2'.isdigit() True .% is performed only between digits.so type cast out string input into int.
        Now checks 2%2==0 True. so, es is incremented from 0 to 2.  i.e es=2
i=4: it will fetch "n" so i=='a'
        checks 'n'.isdigit() False
i=5: it will fetch "4" so i=='4'
        checks '4'.isdigit() True .% is performed only between digits.so type cast out string input into int.
        Now checks 4%2==0 True. so, es is incremented from 2 to 6.  i.e es=6

4.after completion of all the iterations of for loop printing es as 6 and os as 1
    i.e es=6 and os=1

"""



        
