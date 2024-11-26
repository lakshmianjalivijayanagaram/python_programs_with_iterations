 
#04-07-2024
#write a program to print lengthiest word in given string
s=input()
words=s.split()
lw=""
c=0
for i in words:
    if len(i)>c:
        lw=i
        c=len(i)
print(lw)

# Process
""""
ex:s="anju anjali jspiders a"

1.taking input as string
2.spliting the string into words 
2.Assuming that no words is lengthiest in words i.e lw=""
3.Assuming that lengthiest word len is 0 so taking count as 0
    i.e c=0
4.By using for loop fetching each and every word from given words.
    checking that element is lengthiest word or not

i=1: it will fetch "anju" so i="anju"
        checks count of i="anju" is greter than previous ones length
        i.e words.len("anju")>c  4>0 True
        now assuming "anju" is lengthiest word so lw='anju'
        assuming 4 is more length so i.e c=4
i=2: it will fetch "anjali" so i="anjali"
        checks count of i="anjali" greter than previous ones length
        i.e words.len("anjali")>c  6>4 True
        now assuming "anjali" is lengthiest word so lw='anjai'
        assuming 6 is more length so i.e c=6
i=3: it will fetch "jspiders" so i="jspiders"
        checks count of i="jspiders" is greter than previous ones length
        i.e words.len("jspiders")>c  8>6 True
        now assuming "jspiders" is lengthiest word so lw='jspiders'
        assuming 8 is more length so i.e c=8
i=4: it will fetch "a" so i="a"
        checks count of i="a" is greter than previous ones length
        i.e words.len("a")>c  1>8 False

        
5.after completion of all the iterations of for loop printing lengthiest word
    i.e "jspiders"

"""






























