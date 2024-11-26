#write a program to print all the index positions where h is present in a given string

s=input()
for ip in range(len(s)):
    if s[ip]=="h":
        print(ip)
#Process
"""
ex: s="hai python"
1.taking input from user i.e s
2.fetching the index positions of input
    i.e range is len of the collection 0 to 10
i=1: fetching 0 i.e ip=0 checking s[ip] i.e "h"=="h" True so print ip i.e 0
i=2: fetching 1 i.e ip=1 checking s[ip] i.e "a"=="h" False
i=3: fetching 2 i.e ip=2 checking s[ip] i.e "i"=="h" False
i=4: fetching 3 i.e ip=3 checking s[ip] i.e " "=="h" False
i=5: fetching 4 i.e ip=4 checking s[ip] i.e "p"=="h" False
i=6: fetching 5 i.e ip=5 checking s[ip] i.e "y"=="h" False
i=7: fetching 6 i.e ip=6 checking s[ip] i.e "t"=="h" False
i=8: fetching 7 i.e ip=7 checking s[ip] i.e "h"=="h" True so print ip i.e 7

3.print output as 0   7


"""

