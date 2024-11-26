#02-07-2024
#write a program to find the sum of digits present in given string

s=input("enter a string")
summ=0
for i in s:
    if i.isdigit():
        k=int(i)
        summ+=k
print(summ)

#process of program
"""
s="an96j4"
1.taking string as input i.e s
2.Assuming that there is no digits present in given input.so taking summ as 0
    i.e summ=0
3.By using for loop fetching each and every element from given input.
    checking that element is digit or not
i=1: it will fetch "a" so i=='a'
        checks 'a'.isdigit() False so summ is 0 i.e summ=0
i=2: it will fetch "n" so i=='n'
        checks 'n'.isdigit() False so summ is 0 i.e summ=0
i=3: it will fetch "9" so i=='9'
        checks '9'.isdigit() True so k=9 summ is 0 which is int.
        so we cant add our input digit which in the form of string .so type cast out digit input into int
        i.e summ=0+9 now sum incremented from 0 to 9 i.e summ=9
i=4: it will fetch "9" so i=='6'
        checks '6'.isdigit() True so k=6  summ is 9 which is int.
        so we cant add our input digit which in the form of string .so type cast out digit input into int
        i.e summ=9+6 now sum incremented from 9 to 15 i.e summ=15
i=5: it will fetch "j" so i=='j'
        checks 'j'.isdigit() False so summ is 15 i.e summ=15
i=6: it will fetch "4" so i=='4'
        checks "4".isdigit() True so k=4  summ is 15 which is int.
        so we cant add our input digit which in the form of string .so type cast out digit input into int
        i.e summ=15+4 now sum incremented from 15 to 19 i.e summ=19
4.Now after completion fetching of all the elements using for loop prit the summ value
    i.e summ=19"""
    
        
