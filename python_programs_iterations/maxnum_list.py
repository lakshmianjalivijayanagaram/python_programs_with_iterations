#03-07-2024
#Write a program to find maximum present in given list
l=eval(input())
mx=l[0]
for i in l:
    if i>mx:
        mx=i
print(mx)

#Process of Program
"""
ex: l=[10,12,1,23]

1.using eval function for taking list type as input
2.Assuming that first val is max i.e Taking max as mx=l[0]
3.By using for loop fetching each and every element from given input.
    checking that the element is greater than remaining element
    
i=1: it will fetch 10 so i=10
        checks 10 is greater than assumed first max
        i.e 10>10 False
i=2: it will fetch 12 so i=12
        checks 12 is greater than i
        i.e 12>10 True so replacing mx with i i.e mx=12
i=3: it will fetch 1 so i=1
        checks 1 is greater than assumed first max
        i.e 1>12 False
i=4: it will fetch 23 so i=23
        checks 23 is greater than i
        i.e 23>10 True so replacing mx with i i.e mx=23
4.after completion of all the iterations of for loop printing mx as 23
    .e mx=23
