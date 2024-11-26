#09-07-2024
#Write a program to print even numbers present in even index positions
s=input()
for ip in range(len(s)):
    if s[ip].isdigit():
        if int(s[ip])%2==0:
            if ip%2==0:
                print(s[ip])
#PROCESS

"""
ex: s="anju2146"

1.taking input as string
2.fetch the index positions of every element in the given range
 checks that element is even and it is at even index position or not

i=1: it will fetch "a" ip=0 i.e s[ip]="a" checks "a".isdigit() False
i=2: it will fetch "n" ip=1 i.e s[ip]="n" checks "n".isdigit() False
i=3: it will fetch "j" ip=2 i.e s[ip]="j" checks "j".isdigit() False
i=4: it will fetch "u" ip=3 i.e s[ip]="u" checks "u".isdigit() False

i=5: it will fetch "2" ip=4 i.e s[ip]="2" checks "2".isdigit() True
    checks s[ip] is int so coverting into int i.e 2%2==0 True
    checks ip%2==0 i.e 4%2==0 True print the output 2
    
i=6: it will fetch "1" ip=5 i.e s[ip]="1" checks "1".isdigit() True
    checks s[ip] is int so coverting into int i.e 1%2==0 False
   
i=7: it will fetch "4" ip=6 i.e s[ip]="4" checks "4".isdigit() True
    checks s[ip] is int so coverting into int i.e 4%2==0 True
    checks ip%2==0 i.e 6%2==0 True print the output 4
    
i=8: it will fetch "6" ip=7 i.e s[ip]="6" checks "6".isdigit() True
    checks s[ip] is int so coverting into int i.e 6%2==0 True
    checks ip%2==0 i.e 7%2==0 False 
    
"""
