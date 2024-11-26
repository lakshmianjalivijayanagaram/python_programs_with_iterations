l=[]
s="hai anjali"
delimator=" "
dummy=""
for i in s:
    if i!=delimator:
        dummy=dummy+i
    else:
        l.append(dummy)
        dummy=""
l.append(dummy)
print(l)

#PROCESS
"""
1.Taking the input list to store the output
2.taking the input in the form of string
3.taking my delimator as " "
4.taking dummy varable with "" to store each and every element

5.fetching each and every element

i=1: it will fetch i="h"
    checks "h"!=" " true
    dummy=""+"h" i.e dummy="h"
i=2: it will fetch i="a"
    checks "a"!=" " true
    dummy="h"+"a" i.e dummy="ha"
i=3: it will fetch i="i"
    checks "i"!=" " true
    dummy="ha"+"i" i.e dummy="hai"
i=4: it will fetch i=" "
    checks " "!=" " False
    entered into else block
    now dummy i.e "hai" is append to l i.e empty list l=["hai"]
    dummy is reintialized with "" now dummy=""

i=5: it will fetch i="a"
    checks "a"!=" " true
    dummy=""+"a" i.e dummy="a"
i=6: it will fetch i="n"
    checks "n"!=" " true
    dummy="n"+"a" i.e dummy="an"
i=7: it will fetch i="j"
    checks "j"!=" " true
    dummy="an"+"j" i.e dummy="anj"
i=8: it will fetch i="a"
    checks "a"!=" " true
    dummy="anj"+"a" i.e dummy="anja"
i=9: it will fetch i="l"
    checks "l"!=" " true
    dummy="anja"+"l" i.e dummy="anjal"
i=10: it will fetch i="i"
    checks "i"!=" " true
    dummy="anjal"+"i" i.e dummy="anjali"
now loop end no further elements
"anjali" is still there
so append "anjali" to l i.e ["hai","anjali"]
finally print the l as output i.e  ["hai","anjali"]
"""














