class bank:
    bank_name='sbi'
    bank_ifsc=1234
    bank_branch='bangalore'
    def __init__(self,cn,ca,cb,cac):
        self.cname=cn
        self.cage=ca
        self.cbalance=cb
        self.caccount=cac
    def customer_details(self):
        print('customer name is',self.cname)
        print('customer age is',self.cage)
        print('customer balance is',self.cbalance)
        print('customer account is',self.caccount)
    def withdraw(self):
        amt=int(input('enter amount'))
        if amt>=self.cbalance:
            print('sorry not enough balance')
        else:
            self.cbalance-=amt

            print('withdraw is successful',self.cbalance)
    def deposite(self):
        amt=int(input('enter amount'))
        self.cbalance+=amt
        print('deposite is successful',self.cbalance)
girish=bank('girish',23,500000,12345)
vishnu=bank('vishnu',22,100000,67890)
bank.customer_details(girish)
bank.withdraw(vishnu)
vishnu.deposite()
