#03-07-2024
#Write a program to  print how many times each and every element is pesent in given collection

#using builtin methods

"""cdt=eval(input())
d={}.fromkeys(cdt,0)
for i in cdt:
    d[i]=d[i]+1
prnt(d)


cdt=eval(input())
d={}
for i in cdt:
    d[i]=cdt.count(i)
print(d)
"""


#without using builtin methods
cdt=eval(input())
d={}
for i in cdt:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)

#Process
"""
ex: cdt="anjalii"

1.using eval function for taking cdt as input
2.taking dictionary as input because otput in the form of key,val pair.i.e d={}
3.By using for loop fetching each and every element from given input.
    checking that the element is in dictionary or not
    
i=1: it will fetch "a" so i="a"
    checks "a" not in d  True so d[i] i.e "a" is created with count 1 i.e 'a':1
i=2:  it will fetch "n" so i="n"
    checks "n" not in d  True so d[i] i.e "n" is created with count 1 i.e 'n':1
i=3: it will fetch "j" so i="j"
    checks "j" not in d  True so d[i] i.e "j" is created with count 1 i.e 'j':1
i=4: it will fetch "a" so i="a"
    checks "a" not in d  False so d[i] i.e "a" is added to its previous "a"s count i.e 'a':1+1,,,"a":2
i=5:  it will fetch "n" so i="n"
     checks "n" not in d  True so d[i] i.e "l" is created with count 1 i.e 'l':1 
i=6:  it will fetch "i" so i="i"
     checks "i" not in d  True so d[i] i.e "i" is created with count 1 i.e 'i':1
i=7:  it will fetch "i" so i="i"
    checks "i" not in d  False so d[i] i.e "i" is added to its previous "i"s count i.e 'i':1+1,,,"a":2
4.after completion of all the iterations of for loop printing element count
    i.e {'a': 2, 'n': 1, 'j': 1, 'l': 1, 'i': 1}
"""
