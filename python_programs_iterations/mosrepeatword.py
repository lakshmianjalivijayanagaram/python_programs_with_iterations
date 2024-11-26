 
#04-07-2024
#write a program to print most repeated word in given string
s=input()
words=s.split()
mrw=""
c=0
for i in words:
    if words.count(i)>c:
        mrw=i
        c=words.count(i)
print(mrw)

# Process
""""
ex:s="anjali ant jspiders anjali"

1.taking input as string
2.spliting the string into words 
2.Assuming that no words is mostly present in words i.e mrw=""
3.Assuming that no words is repeated most of the times so taking count as 0
    i.e c=0
4.By using for loop fetching each and every word from given words.
    checking that element is mostrepeated word or not

i=1: it will fetch "anjali" so i="anjali"
        checks count of i="anjali" in given input is greter than previous ones count
        i.e words.count("anjali")>c  2>0 True
        now assuming "anjali" is most repeated word i.e mrc='anjali'
        assuming count 2 is most repeated count i.e c=2
i=2: it will fetch "ant" so i="ant"
        checks count of i="ant" in given input is greter than previous ones count
        i.e words.count("ant")>c  2>1 False
i=3: : it will fetch "jspiders" so i="jspiders"
        checks count of i="jspiders" in given input is greter than previous ones count
        i.e words.count("jspiders")>c  1>2 False
        
5.after completion of all the iterations of for loop printing most repeated word
    i.e "anjali"

"""
























"""s=input()
a=s.split()
lw=""
c=0
for i in a:
    if len(i)>c:
        lw=i
        c=len(i)
print(lw)"""







