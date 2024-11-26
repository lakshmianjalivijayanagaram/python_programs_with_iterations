#02-07-2024
#Write a program to find how many consonants are present in given sring.
s=input("enter a string ")
cc=0
vowels="aeiouAEIOU"
for i in s:
    if i.isalpha():
        if i not in vowels:
             cc+=1
print(cc)

#Process of Program
"""
ex: s="anj4li"

1.taking string as input i.e s
2.Assuming that there is no consonants present in given input.so taking cc as 0.
    i.e cc=0
3.storing all the vowels in vowels variable for checking.
4.By using for loop fetching each and every element from given input.
    checking that element is consonant or not.

i=1: it will fetch "a" so i=="a"
        checks "a".isalpha() True "a" not in vowels False.
i=2: it will fetch "n" so i=="n"
        checks "n".isalpha() True "n" not in vowels True.
        SO cc incremented from 0 to 1 i.e cc=1
i=3: it will fetch "j" so i=="j"
        checks "j".isalpha() True "j" not in vowels True.
        SO cc incremented from 1 to 2 i.e cc=2.
i=4:  it will fetch "4" so i=="4"
        checks "4".isalpha() False.
i=5:  it will fetch "l" so i=="l"
        checks "l".isalpha() True "l" not in vowels True.
        SO cc incremented from 2 to 3 i.e cc=3
i=6:  it will fetch "i" so i=="i"
        checks "i".isalpha() True "i" not in vowels False.

5.after completion of all the iterations of for loop
    print cc as 3 i.e cc=3.


