class bank_v1():
    bank_name='sbi'
    bank_ifsc=1234
    bank_branch='bangalore'
    def __init__(self,cn,ca,cb,cac):
        self.cname=cn
        self.cage=ca
        self.cbal=cb
        self.caccount=cac
        
    @classmethod
    def display_bank_details(cls):
        print('bank name is',cls.bank_name)
        print('bank ifsc is',cls.bank_ifsc)
        print('bank branch is',cls.bank_branch)
        
    def customer_details(self):
        print('customer name is',self.cname)
        print('customer age is',self.cage)
        print('customer balance is',self.cbal)
        print('customer account is',self.caccount)
        
    @staticmethod
    def get_int_val():
        iv=int(input("enter value"))
        return iv
    
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
    
class bank_v2(bank_v1):
    bank_branch='hyderabad'
    bank_roi=7
    
    def __init__(self,cn,ca,cb,cac,cp):
        #super().__init__(cn,ca,cb,cac)
        bank_v1.__init__(self,cn,ca,cb,cac)
        self.cpinnum=cp

        
    @classmethod
    def display_bank_details(cls):
        super().display_bank_details()
        #bank_v1.display_bank_details()
        print('bank roi is',cls.bank_roi)

    def withdraw(self):
        cpinnum=self.get_int_val()
        if cpinnum==self.cpinnum:
            #super().withdraw()
            bank_v1.withdraw(self)
        else:
            print('incorrect pin')

              
    @staticmethod
    def get_str_val():
        sv=input("enter string value")
        return sv

        
    @classmethod
    def change_branch(cls):
        cls.bank_branch=cls.get_str_val()
        print('ban branch has changed to',cls.bank_branch)

        
    @classmethod
    def change_roi(cls):
        iv=cls.get_int_val()
        cls.bank_roi=iv
        print('bank roi is changed to',cls.bank_roi)

        
anjali=bank_v2('anjali',21,1000000,987654321,243)

#anjali.change_roi()
anjali.withdraw()
anjali.display_bank_details()

        
    

