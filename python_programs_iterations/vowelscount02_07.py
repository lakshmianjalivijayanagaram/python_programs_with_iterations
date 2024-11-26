#02-07-2024
#Write a program to find how many vowels are present in given sring.
s=input("enter a string ")
vc=0
vowels="aeiouAEIOU"
for i in s:
    if i in vowels:
        vc+=1
print(vc)


#Process of Program
"""
ex: s="Anjali"

1.taking string as input i.e s
2.Assuming that there is no vowels present in given input.so taking vc as 0 
    i.e vc=0
3.storing all the vowels in vowels variable for checking.
4.By using for loop fetching each and every element from given input.
    checking that element is vowel or not

i=1: it will fetch "A" so i="A"
        "A" in vowels True so vc incremented from 0 to 1 i.e vc=1
i=2:  it will fetch "n" so i="n"
        "n" in vowels False so vc still 1 i.e vc=1
i=3:  it will fetch "j" so i="j"
        "j" in vowels False so vc still 1 i.e vc=1
i=4:  it will fetch "a" so i="a"
        "a" in vowels True so vc incremented from 1 to 2 i.e vc=2
i=5:  it will fetch "l" so i="l"
        "l" in vowels False so vc still 2 i.e vc=2
i=6:  it will fetch "i" so i="i"
        "i" in vowels True so vc incremented from 2 to 3 i.e vc=3

5.after completion of all the iterations of for loop printing vc as 3
    i.e vc=3
    """


