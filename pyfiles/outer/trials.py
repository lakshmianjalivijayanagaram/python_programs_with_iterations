'''a=[10,20,30,40,50,60]
b=a[::-1]
summ=0
for i in range(0,len(b)):
    if i%2==0:
        summ+=b[i]
print(summ)
#val=int(input())
def sumprime(val):
    summ=0
    for n in range(1,val):
        if n>1:
            for i in range(2,n//2+1):
                if n%i==0:
                    break
            else:
                summ+=n
                print(n)
    return summ
print(sumprime(10))
summ=0
for i in range(4,9+1):
    summ+=i**3
print(summ)
a=[1,3,2,3,2,4]
b=set(a)
print(sum(b))
a=[1,2,3]
b=a
b.append(4)
print(a)

nums=[0,1,0,3,0,2,2,0]
sum=0
sum_nums=[]
for i in range(0,len(nums)):
    if nums[i]==0:
        if sum>0:
            sum_nums.append(sum)
            sum=0
    else:
        sum+=nums[i]
print(sum_nums)

'''
def romanToDecimal(S): 
        # code here
        d={'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        count=0
        if len(S)==1:
            return d[S[0]]
        else:
            for i in range(0,len(S)-1):
                if S[i]<S[i+1]:
                    count-=d[S[i]]
                else:
                    count+=d[S[i]]
            count+=d[S[-1]]
            return count                    
print(romanToDecimal('MMMDCLXXX'))












