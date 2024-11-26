class player():
    def __init__(self,pn,pa,pc,pm,pw,pr):
        self.pname=pn
        self.page=pa
        self.pcountry=pc
        self.pmatches=pm
        self.pwickets=pw
        self.pruns=pr
class team:
    def __init__(self,nop):
        self.nop=nop
        self.player=[]
        for i in range(self.nop):
            pn=input('enter name')
            pa=int(input('enter age'))
            pc=input('enter country')
            pm=int(input('enter matches'))
            pw=int(input('enter pwickets'))
            pr=int(input('enter pruns'))
            po=player(pn,pa,pc,pm,pw,pr)
            self.player.append(po)
    def maxwtaker(self):
        mwto=self.player[0]
        for po in self.player:
            if po.pwickets>mwto.pwickets:
                mxto=po
        return mxto.pname
t1=team(3)
print(t1.maxwtaker())
        
        
