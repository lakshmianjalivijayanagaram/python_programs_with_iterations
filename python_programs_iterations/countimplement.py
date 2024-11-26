#impliment count method 
s=input()
sub=input()
c=0
ip=0
while ip<(len(s)-len(sub)+1):
    if s[ip:ip+len(sub)]==sub:
        c=c+1
    ip+=1
print(c)

#PROCESS
ex: s="anjali"
sub="al"
1.TAKING sting as input
2.taking the sub string to count how many times its occurance is
3.Assuming occurances of substring as 0
4.assigming i=0
5.taking while loop from i=0 to len(s)-len(sub)+1
    here 6-2+1 i.e 5 upto 5 we have to iterate why beacaue for  eliminating the unwanted sub strings like at end "i" only einas while checking it is single
    so no need to check with sub string having length 2.

i=1: it will fetch ip=0, len(s)-len(sub)+1 i.e 5 0<5 True
    checks s[0:0+2]==sub i.e s[0:2] i.e "an"=="al" False
    ip=ip+1 i.e ip is incremented from 0 to 1
    
i=2: it will fetch ip=1, len(s)-len(sub)+1 i.e 5 1<5 True
    checks s[1:1+2]==sub i.e s[1:3] i.e "nj"=="al" False
    ip=ip+1 i.e ip is incremented from 1 to 2
    
    
i=3: it will fetch ip=2, len(s)-len(sub)+1 i.e 5 2<5 True
    checks s[2:2+2]==sub i.e s[2:4] i.e "ja"=="al" False
    ip=ip+1 i.e ip is incremented from 2 to 3
    
i=4: it will fetch ip=3, len(s)-len(sub)+1 i.e 5 3<5 True
    checks s[3:3+2]==sub i.e s[3:5] i.e "al"=="al" True
    c is incremented from  0 to 1 i.e c=1
    ip=ip+1 i.e ip is incremented from 3 to 4
    
i=5: it will fetch ip=4, len(s)-len(sub)+1 i.e 5 4<5 True
    checks s[1:1+2]==sub i.e s[1:3] i.e "li"=="al" False
    ip=ip+1 i.e ip is incremented from 4 to 5
    
i=6: it will fetch ip=5, len(s)-len(sub)+1 i.e 5 5<5 False
came out from the loop
5.after that print count as c=1

    
    
