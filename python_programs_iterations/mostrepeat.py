#03-07-2024
#Write a program to print most repeated character from a given string
s=input()
mrc=""
c=0
for i in s:
    if s.count(i)>c:
        mrc=i
        c=s.count(i)
print(mrc)

#Process
"""
ex:s="anjali"

1.taking input as string"
2.Assuming that no characher is mostly present in sting i.e mrc=""
3.Assuming that no character is repeated most of the times so taking count as 0
    i.e c=0
4.By using for loop fetching each and every element from given input.
    checking that element is mostrepeated char or not

i=1: it will fetch "a" so i="a"
        checks count of i="a" in given input is greter than previous ones count
        i.e s.count("a")>c  2>0 True
        now assuming "a" is most repeated character i.e mrc='a"
        assuming count 2 is most repeated count i.e c=2
i=2: it will fetch "n" so i="n"
        checks count of i="n" in given input is greter than previous ones count
        i.e s.count("n")>c  1>2 False
i=3: it will fetch "j" so i="j"
        checks count of i="j" in given input is greter than previous ones count
        i.e s.count("j")>c  1>2 False
i=:4  it will fetch "a" so i="a"
        checks count of i="j" in given input is greter than previous ones count
        i.e s.count("a")>c  2>2 False
i=5:  it will fetch "l" so i="l"
        checks count of i="j" in given input is greter than previous ones count
        i.e s.count("l")>c  1>2 False
i=6:   it will fetch "i" so i="i"
        checks count of i="j" in given input is greter than previous ones count
        i.e s.count("i")>c  1>2 False

5.after completion of all the iterations of for loop printing most repeated character
    i.e "a"


        


