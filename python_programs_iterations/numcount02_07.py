#3.W.r.t a program to print how many numbers are present in given string
s=input("enter a sting")
c=0
for i in s:
    if i.isdigit():
        c=c+1
print(c)

#PROCESS OF PROGRAM
"""
s="an92j6"
1.Taking Sring as input i.e s
2.Assuming that 0 digits are present in given string So c=0
3.By assuming for loop fetching each and every element from string
    checking is that element is digit or not
i=1: it will fetch 'a' so i="a"
        check "a".isdigit() False so c is 0 i.e c=0
i=2: it will fetch 'n' so i="n"
        check "n".isdigit() False so c is 0 i.e c=0
i=3: it will fetch '9' so i="9"
        check "9".isdigit() True so c is incremented from 0 to 1 i.e c=1
i=4: it will fetch '2' so i="2"
        check "2".isdigit() True so c is incremented from 1 to 2 i.e c=2
i=5: it will fetch 'j' so i="j"
        check "j".isdigit() False so c is 2 i.e c=2
i=6: it will fetch '6' so i="6"
        check "6".isdigit() True so c is incremented from 2 to 3 i.e c=3
4.after completion of all the iterations of for loop print c value i.e c=3

"""

    

#one more type for solving the program
"""s=input("enter a sting")
numbers="012345789"
c=0
for val in s:
    if val in numbers:
        c=c+1
print(c)

#PROCESS OF PROGRAM

s="an92j6"

1.Taking Sring as input i.e s
2.Taking numbers as input it contains all the numbers from 0-9
3.Assuming that no digits are present in given string i.e in s So c=0
4.By assuming for loop fetching each and every element from string
    checking that is that element is present in numbers
i=1: it will fetch 'a' so val="a"
        check "a" in "0123456789" False so c is 0 i.e c=0
i=2: it will fetch 'n' so val="n"
        check "n" in "0123456789" False so c is 0 i.e c=0
i=3: it will fetch '9' so val="9"
        check "9" in "0123456789" True so c is incremented from 0 to 1
        i.e c=1
i=4: it will fetch '2' so val="2"
        check "2" in "0123456789" True so c is incremented from 1 to 2
        i.e c=2
i=5: it will fetch 'j' so val="j"
        check "j" in "0123456789" False so c is 2 i.e c=2
i=6: it will fetch '6' so val="6"
        check "6" in "0123456789" True so c is incremented from 2 to 3
        i.e c=3
5.after completion of all the iterations of for loop print c value i.e c=3
"""


