#02-07-2024
#Write a program to find the countof even digits and count of odd digits present in a given string
s=input("enter a string ")
ec=0
oc=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            ec+=1
        else:
            oc+=1
print(ec)
print(oc) 

#Process of Program
"""
ex: s="a12n4"
 
1.taking string as input i.e s
2.Assuming that there is no digits present in given input.so taking evensum as 0 and oddsum as 0
    i.e ec=0 and oc=0
3.By using for loop fetching each and every element from given input.
    checking that element is digit or not
    
i=1: it will fetch "a" so i=='a'
        checks 'a'.isdigit() False
i=2: it will fetch "1" so i=='1'
        checks '1'.isdigit() True .% is performed only between digits.so type cast out string input into int.
        Now checks 1%2==0 False. so, oc is incremented from 0 to 1.  i.e oc=1
i=3: it will fetch "2" so i=='2'
        checks '2'.isdigit() True .% is performed only between digits.so type cast out string input into int.
        Now checks 2%2==0 True. so, ec is incremented from 0 to 1.  i.e ec=1
i=4: it will fetch "n" so i=='a'
        checks 'n'.isdigit() False
i=5: it will fetch "4" so i=='4'
        checks '4'.isdigit() True .% is performed only between digits.so type cast out string input into int.
        Now checks 4%2==0 True. so, ec is incremented from 1 to 2.  i.e ec=2

4.after completion of all the iterations of for loop printing ec as 6 and oc as 1
    i.e ec=2 and oc=1

"""



        
