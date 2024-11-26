class bank:
    bank_name='sbi'
    bank_ifsc=1234
    bank_address='bangalore'
    bank_roi=7
    def __init__(self,cn,cac,cb):
        self.cname=cn
        self.caccount=cac
        self.cbal=cb
    def customer_details(self):
        print('customer name is',self.cname)
        print('customer account is',self.caccount)
        print('customer balance is',self.cbal)
    @staticmethod
    def get_int_val():
        iv=int(input("enter value"))
        return iv
    @staticmethod
    def get_str_val():
        sv=input("enter string value")
        return sv
    def withdraw(self):
        amt=self.get_int_val()
        if self.cbal<amt:
            print('insufficient balance')
        else:
            self.cbal-=amt
            print('withdraw is succefull',self.cbal)
    def deposite(self):
        amt=self.get_int_val()
        if amt>0:
            self.cbal+=amt
            print('deposite is successfull',self.cbal)
        else:
            print('amount should be greater than 0')
    @classmethod
    def bank_address(cls):
        sv=cls.get_str_val()
        cls.bank_address=sv
        print('bank address is changed to',cls.bank_address)
    @classmethod
    def change_roi(cls):
        iv=cls.get_int_val()
        cls.bank_roi=iv
        print('bank roi is changed to',cls.bank_roi)
    @classmethod
    def bank_details(cls):
        print('bank name is',cls.bank_name)
        print('bank ifsc is',cls.bank_ifsc)
        print('bank address is',cls.bank_address)
        print('bank roi is',cls.bank_roi)
    


        
    
anjali=bank('anjali',12345678,100000)
print(anjali.bank_name)
bank.change_roi()
bank.bank_address()
bank.bank_details()
#anjali.change_roi()
#anjali.bank_address()
#anjali.customer_details()
#anjali.withdraw()
#anjali.deposite()

        
