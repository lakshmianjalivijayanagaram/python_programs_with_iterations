#09-07-2024
#Write a program to replace all the vowels with their index positions
s=input()
vowels="aeiouAEIOU"
new=""
for ip in range(len(s)):
    if s[ip] in vowels:
        new+=str(ip)
    else:
        new+=s[ip]
print(new)

#PROCESS

"""
ex: s="anjali"

1.taking input as string
2.we need to check for vowel or not so i had taken the vowels in varible v.
3.Assuming that there is no vowels is present in the input so taking empty string as input i.e new=""
4.fetch the index positions of every element in the given range
 checks that element is present in vowels or not.

i=1: fetch ip=0 checks s[ip] i.e "a" in vowels True so add index position to new .
    new is string so converting ip to str  i.e "0" new=" "+"0" i.e new="0"
i=2: fetch ip=1 checks s[ip] i.e "n" in vowels False so add element to new .
    i.e "n" new="0"+"n" i.e new="0n"
i=3: fetch ip=2 checks s[ip] i.e "j" in vowels False so add element to new .
    i.e "j" new="0n"+"j" i.e new="0nj"
i=4: fetch ip=3 checks s[ip] i.e "a" in vowels True so add index position to new .
    new is string so converting ip to str  i.e "3" new="0nj"+"3" i.e new="0nj3"
i=5: fetch ip=4 checks s[ip] i.e "l" in vowels False so add element to new .
    i.e "l" new="0nj3"+"l" i.e new="0nj3l"
i=6: fetch ip=5 checks s[ip] i.e "i" in vowels True so add index position to new .
    new is string so converting ip to str  i.e "5" new="0nj3l"+"5" i.e new="0nj3l5"

5.After completion of all the iterations prints the output new i.e "0nj3l5"
"""
