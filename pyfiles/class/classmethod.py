class bank:
    bank_name='sbi'
    bank_ifsc=1234
    bank_branch='kizikistan'
    bank_roi=7
    def __init__(self,cn,ca,cb):
        self.cname=cn
        self.cage=ca
        self.cbalance=cb
    @classmethod
    def modify_roi(cls):
        print('cls value is',cls)
        newr=int(input("enter roi"))
        cls.bank_roi=newr
        print('roi of the bank has changed')
shiva=bank('shiva',22,100000)
durga=bank('durga',21,500000)
print(shiva.bank_roi)
bank.modify_roi()
print(bank.bank_roi)
print(shiva.bank_roi)
print(durga.bank_roi)
print('shiva',shiva)
print('durga',durga)
