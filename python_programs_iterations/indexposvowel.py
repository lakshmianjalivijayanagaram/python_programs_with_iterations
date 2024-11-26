#09-07-2024
#Write a program to print the index position of vowels present in a given string
s=input()
v="aeiouAEIOU"
for ip in range(len(s)):
    if s[ip] in v:
        print(ip)
#PROCESS

"""
ex: s="anjali"
1.taking input as string
2.we need to check for vowel or not so i had taken the vowels in varible v
3.fetch the index positions of every element in the given range
 checks that element is present in vowels or not

i=1: fetch ip=0 cheks s[ip] i.e "a" in "aeiouAEIOU" True so print "a"
i=2: fetch ip=1 cheks s[ip] i.e "n" in "aeiouAEIOU" False
i=3: fetch ip=2 cheks s[ip] i.e "j" in "aeiouAEIOU" False
i=4: fetch ip=3 cheks s[ip] i.e "a" in "aeiouAEIOU" True so print "a"
i=5: fetch ip=4 cheks s[ip] i.e "l" in "aeiouAEIOU" False
i=6: fetch ip=5 cheks s[ip] i.e "i" in "aeiouAEIOU" True so print "i"
