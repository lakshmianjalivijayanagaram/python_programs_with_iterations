#03-07-2024
#Write a program to find sum of the digits present in given list
l=eval(input())
summ=0
for i in l:
    if type(i)==int:
        summ=summ+i
print(summ)

#Process
"""

ex: l=[4,2,3,[10,20],"anjali",(132,"hai")]

1.using eval function for taking list type as input
2.Assuming that no digits are present in given list i.e summ=0
3.By using for loop fetching each and every element from given input.
    checking that the element is int or not
    
i=1: it will fetch 4 so i=4
        checks 4==int True so summ incremented from 0 to 4 Now summ=4
i=2: it will fetch 2 so i=2
        checks 2==int True so summ incremented from 4 to 6 Now summ=6
i=3: it will fetch 3 so i=3
        checks 3==int True so summ incremented from 6 to 9 Now summ=9
i=4: it will fetch [10,20] so i=[10,20]
        checks [10,20]==int False so summ is still 9 summ=9
i=5:  it will fetch "hai" so i="hai"
        checks "anjali"=int False so summ is still 9 summ=9
i=6: it will fetch  (132,"hai") so i=(132,"hai")
        checks (132,"hai")==int False so summ is still 9 summ=9

5.after completion of all the iterations of for loop printing summ as 9
    i.e summ=9
    """
