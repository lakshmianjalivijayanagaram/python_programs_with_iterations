#09-07-2024
#Write a program to print the elements which are present in even index positions
s=input()
for ip in range(len(s)):
    if ip%2==0:
        print(s[ip])

#PROCESS
"""
ex: s="anjali"
1.taking string input because string is mentioned
2.taking for loop it will fetch each and every index postion of element
    checks that index position is even or not
i=1: it will fetch ip=0 checks 0%2==0 True so print 0th index position element i.e "a"
i=2: it will fetch ip=1 checks 1%2==0 False
i=3: it will fetch ip=2 checks 2%2==0 True so print 2th index position element i.e "j"
i=4: it will fetch ip=3 checks 3%2==0 False
i=5: it will fetch ip=4 checks 4%2==0 True so print 4th index position element i.e "l"
i=6: it will fetch ip=5 checks 5%2==0 False
"""

