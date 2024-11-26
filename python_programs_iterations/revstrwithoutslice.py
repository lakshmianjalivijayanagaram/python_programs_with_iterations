#09-07-2024
#Write a program to reverse a string without using slicing
s=input()
rev=""
for i in s:
    rev=i+rev
print(rev)


"""
s=input()
rev=""
for ip in range(-1,-(len(s)+1),-1):
    rev+=s[ip]
print(rev)

s=input()
rev=""
for ip in range(len(s)-1,-1,-1):
    rev+=s[ip]
print(rev)



#Process


ex: s="anjali"

1.taking str as input
2.taking a string for storing reversed string
3.fetching each and every element

i=1:fetch i="a" i.e rev="a"+""  rev="a"
i=2:fetch i="n" i.e rev="n"+"a"  rev="na"
i=3:fetch i="j" i.e rev="j"+"na"  rev="jna"
i=4:fetch i="a" i.e rev="a"+"jna"  rev="ajna"
i=5:fetch i="l" i.e rev="l"+"ajna"  rev="lajna"
i=6:fetch i="i" i.e rev="i"+"ilajna"  rev="ilajna"
4.After completion of all the iterations printing the output as "ilajna"
"""
