#2.w.r.t a program to print how many times given substring is present in given string
ms=input("enter mainstring")
ss=input("enter substrig")
c=0
for i in ms:
    if i==ss:
        c=c+1
print(c)



#PROCESS OF PROGRAM

"""
ms="anjali"
ss="a"
1.Taking mainstring as input i.e ms
2.Taking substring as input i.e ss
3.By Assuming 'ss' is not present in 'ms' so c=0
4.By assuming for loop fetching each and every element from ms
    and checking ss with ms's each and every element
i=1:  it will fetch 'a' so i="a"
        check "a"=="a" True so c is incremented from 0 to 1 NOW c=1
i=2:  it will fetch 'n' so i="n"
        check "a"=="n" False so c is still 1 only NOW c=1
i=3:  it will fetch 'j' so i="j"
        check "a"=="j" False so c is still 1 only NOW c=1
i=4:  it will fetch 'a' so i="a"
        check "a"=="a" True so c is incremented from 2 to 1 NOW c=2
i=5:  it will fetch 'l' so i="l"
        check "a"=="l" False so c is still 2 only NOW c=2
i=6:  it will fetch 'i' so i="i"
        check "a"=="i" False so c is still 2 only NOW c=2
5.atlast after complete iteration of for loop printing c value i.e c=2

"""

