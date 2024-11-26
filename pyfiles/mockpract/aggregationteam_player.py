'''class player():
    def __init__(self,pn,pa,pc,pm,pw,pr):
        self.pname=pn
        self.page=pa
        self.pcountry=pc
        self.pmatches=pm
        self.pwickets=pw
        self.pruns=pr
class Team():
    def __init__(self,n):
        self.nop=n
        self.pl=[]
        for i in range(self.nop):
            pn=input('enter name')
            pa=int(input('enter age'))
            pc=int(input('enter age'))
            pm=input('enter country')
            pw=int(input('enter age'))
            pr=int(input('enter age'))
            po=player(pn,pa,pc,pm,pw,pr)
            self.pl.append(po)
    def maxWTaker(self):
        maxwt=self.pl[0]
        for po in self.pl:
            if po.pwickets>maxwt.pwickets:
                maxwt=po
        return maxwt.pname
    def maxRScore(self):
        maxRS=self.pl[0]
        for po in self.pl:
            if po.pruns>maxRS.pruns:
                maxRS=po
        return maxRS.pname

Te=Team(2)
print(Te.maxWTaker())


class Vinay:
    house='1bhk'
    bike='chetak'
    money=100000
lakshmi=Vinay()
class Narayana(Vinay):
    bike='ktm390'
    car='KIA'
asha=Narayana()
print(lakshmi.house)
print(Vinay.house)
print(Narayana.house)
print(asha.house)'''
'''Vinay.money=50000
print(lakshmi.money)
print(Vinay.money)
print(Narayana.money)
print(asha.money)'''
'''lakshmi.money=50000
print(lakshmi.money)
print(Vinay.money)
print(Narayana.money)
print(asha.money)
Narayana.money=50000
print(lakshmi.money)

print(Vinay.money)
print(Narayana.money)
print(asha.money)

'''






















