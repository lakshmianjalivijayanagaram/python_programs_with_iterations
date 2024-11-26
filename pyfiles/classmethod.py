class Bank:
    bank_name='sbi'
    bank_ifsc=1234
    bank_branch='kizikistan'
    bank_roi=7
    def __init__(self,n,a,b):
        self.cname=n
        self.age=a
        self.cbal=b
    @classmethod
    def modify_roi(cls):
        print('cls value is ',cls)
        new=int(input('enter value'))
        cls.bank_roi=new
        print('roi is changed')
shiva=Bank('shiva',20,100000)
ramya=Bank('ramya',22,150000)
print('shiva',shiva)
print('ramya',ramya)
print('bank',Bank)

#Bank.modify_roi()
print(Bank.bank_roi,"bank")
print(shiva.bank_roi,"shiva")
print(ramya.bank_roi,'ramya')
        
