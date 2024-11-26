'''class Bank:
    bank_name='sbi'
    bank_ifsc=1234
    bank_address='kizikistan'
girish=Bank()
#print(girish.bank_name)
#print(Bank.bank_name)
Bank.bank_ifsc=4567
#print(Bank.bank_ifsc)
#print(girish.bank_ifsc)
#girish.bank_address='pakistan'
#print(girish.bank_address)
#print(Bank.bank_address)
Bank.bank_roi=5
#print(Bank.bank_roi)
#print(girish.bank_roi)
#girish.bank_roi=5
#del Bank.bank_roi
print(girish.bank_roi)
print(Bank.bank_roi) '''
'''
class Bank():
    bank_name='sbi'
    bank_ifsc=1234
    bank_address='pakistan'
    def __init__(self,cn,ca,cb):
        self.cname=cn
        self.cage=ca
        self.cbal=cb
    def customer_details(self):
        print('customer name',self.cname)
        print('customer age',self.cage)
        print('customer balabce',self.cbal)
    def withdraw(self):
        amt=int(input('enter amount'))
        if self.cbal>=amt:
            self.cbal-=amt
            print('available balance is',self.cbal)
        else:
            print('insufficient balance')
    def deposite(self):
        amt=int(input('enter amount'))
        if amt>0:
            self.cbal+=amt
            print('available balance is',self.cbal)
        else:
            print('balance should be greater than 0')
anjali=Bank('anjali',21,10000)
anjali.withdraw()
anjali.deposite()
'''





























            


