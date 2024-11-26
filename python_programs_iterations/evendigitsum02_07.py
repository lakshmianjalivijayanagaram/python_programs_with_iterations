#02-07-2024
#Write a program to find the sum of even digits present in a given string
s=input("enter a string ")
esum=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            esum+=k
print(esum)

#Process of program
"""
s="an865i

1.taking string as input i.e s
2.Assuming that there is no even digits present in given input.so taking esum as 0
    i.e esum=0
3.By using for loop fetching each and every element from given input.
    checking that element is digit or not

    
i=1: it will fetch "a" so i=='a'
        checks 'a'.isdigit() False
i=2: it will fetch "n" so i=='n'
        checks 'n'.isdigit() False
i=3: it will fetch "8" so i=='8'
        checks '8'.isdigit() True summ is 0 which is int.
    --> so we cant add our input digit which in the form of string .so typecast out digit input into int.i.e k=8
        check k%2==0 True so summ is incremented from 0 to 8  i.e summ=8         
    
i=4: it will fetch "6" so i=='6'
        checks '6'.isdigit() True summ is 8 which is int.
    --> so we cant add our input digit which in the form of string .so typecast out digit input into int.i.e k=6
        check k%2==0 True so summ is incremented from 8 to 14 i.e summ=14
i=5: it will fetch "5" so i=='5'
        checks '5'.isdigit() True summ is 14 which is int.
    --> so we cant add our input digit which in the form of string .so typecast out digit input into int.i.e k=14
        check k%2==0 False so summ is still 14
i=6: it will fetch "i" so i=='i'
        checks 'i'.isdigit() False
4.Now after completion fetching of all the elements using for loop prit the summ value
    i.e summ=14"""
    
    









summ is 0 which is int.
    --> so we cant add our input digit which in the form of string .so typecast out digit input into int
    






















'''s=input("enter a string ")
scount=0
for i in s:
    if not i.isalunum():
        scount+=1
print(scount)
'''
