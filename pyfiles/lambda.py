'''square=lambda a:a**2
print(square(5))
iseven=lambda a:a%2==0
print(iseven(12))
mul=lambda m,n:m*n
print(mul(10,20))'''
#map function
def add(n):
    return n+10
print(list(map(lambda a:a+10,[10,20,30,40])))

print(list(map(lambda a:a%2==0,[2,3,4,5,6])))

def mul(n):
    return n*2
print(list(map(mul,[1,2,3,4])))

#filter function
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
print(list(filter(is_even,[1,2,3,4,5])))
print(list(filter(lambda n:n%2==0,[1,2,3,5,4])))
print(list(filter(lambda n:n**2,[1,2,3,5,4])))

#reduce function
from functools import reduce
l=[100,22,104,2,19]
print(reduce(lambda a,b:a if a>b else b,l))
m=['anjali','amma','ammamma','suma']
print(reduce(lambda a,b:a if len(a)>len(b) else b,m))

print(reduce(lambda a,b:a if a<b else b,l))
print(reduce(lambda a,b:a+b,l))
#flattenning the ist of nested list
p=[[10,20,30],[11,23],[11,23,23,44,19]]
print(reduce(lambda a,b:a+b,p))





