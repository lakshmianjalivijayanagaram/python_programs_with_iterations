"""s='hai1246798475'
summ=0
for ip in range(len(s)):
    if s[ip].isdigit() and int(s[ip])%2==0:
       if ip%2!=0:
           summ+=int(s[ip])
           print(ip)
print(summ)
 
"""
s=input()
new=""
for i in range(len(s)-1,-1,-1):
    new=new+s[i]
print(new)

