class Bank:
    bank_name='sbi'
    bank_ifsc=1234
    bank_address='kizikistan'
    bank_roi=7
    def __init__(self,cn,ca,cb):
        self.cname=cn
        self.cage=ca
        self.cbal=cb
    def customer_details(self):
        print('customer name',self.cname)
        print('customer age',self.cage)
        print('customer balance',self.cbal)
    def withdraw(self):
        amt=self.get_int_val()
        if amt<=self.cbal:
            self.cbal-=amt
            print('amount is',self.cbal)
        else:
            print('insufficient amount')
    def deposite(self):
        amt=self.get_int_val()
        if amt>0:
            self.cbal+=amt
            print('amount is',self.cbal)
        else:
            print('amount should be greater than 0')
    @classmethod
    def bank_details(cls):
        print('bank name is',cls.bank_name)
        print('bank ifsc is',cls.bank_ifsc)
        print('bank address is',cls.bank_address)
        print('bank rate of interest is',cls.bank_roi)
    @classmethod
    def change_roi(cls):
        #print('cls value',cls)
        new_roi=cls.get_int_val()
        cls.bank_roi=new_roi
        print('roi is changed',cls.bank_roi)
    @staticmethod
    def get_int_val():
        iv=int(input('enter val'))
        return iv
        
anjali=Bank('anjali',21,10000)
anjali.customer_details()
anjali.withdraw()
anjali.deposite()
anjali.bank_details()
anjali.change_roi()


















        
        
        
