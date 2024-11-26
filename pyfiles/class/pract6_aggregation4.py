class player():
    def __init__(self,pn,pa,pc,pm,pw,pr):
        self.pname=pn
        self.page=pa
        self.pcountry=pc
        self.pmathes=pm
        self.pwickets=pw
        self.pruns=pr
class team:
    def __init__(self,nop):
        self.noofplayers=nop
        self.pl=[]
        for i in range(self.noofplayers):
            pn=input('enter name')
            pa=int(input('enter age'))
            pc=input('enter country')
            pm=int(input('enter matches'))
            pw=int(input('enter wickets'))
            pr=int(input('enter runs'))
        playerobject=player(pn,pa,pc,pm,pw,pr)
        self.pl.append(playerobject)
    def maxwtaker(self):
        mwto=self.pl[0]
        for playerobject in self.pl:
            if playerobject.pwickets>mwto.pwickets:
                mwto=playerobject
        return mwto.pname
    def maxrunscorer(self):
        mrso=self.pl[0]
        for playerobject in self.pl:
            if playerobject.pruns>mrso.pruns:
                mrso=playerobject
        return mrso.pname
to=team(2)
print(to.maxwtaker())
print(to.maxrunscorer())
        
