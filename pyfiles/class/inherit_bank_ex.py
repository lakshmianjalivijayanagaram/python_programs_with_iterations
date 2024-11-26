class bank_v1:
    bank_name='sbi'
    bank_ifsc=1234
    bank_branch='bangalore'
    def __init__(self,cn,ca,cb,cac):
        self.cname=cn
        self.cage=ca
        self.cbalance=cb
        self.caccount=cac
    @classmethod
    def display_bank_details(cls):
        print(f'bank name is {cls.bank_name}')
        print(f'bank ifsc is  {cls.bank_ifsc}')
        print(f'bank branch is {cls.bank_branch}')
    def customer_details(self):
        print('customer name is',self.cname)
        print('customer age is',self.cage)
        print('customer balance is',self.cbalance)
        print('customer account is',self.caccount)
    @staticmethod
    def get_int_value():
        iv=int(input('enter value'))
        return iv
    def withdraw(self):
        amt=self.get_int_value()
        if amt>self.cbalance:
            print('sorry not enough balance')
        else:
            self.cbalance-=amt

            print('withdraw is successful',self.cbalance)
    def deposite(self):
        amt=self.get_int_value()
        self.cbalance+=amt
        print('deposite is successful',self.cbalance)
class bank_v2(bank_v1):
    bank_branch='hyderabad'
    @staticmethod
    def get_str_value():
        sv=input('enter value')
        return sv
    @classmethod
    def change_branch(cls):
        bn=cls.get_str_value()
        cls.bank_branch=bn
        print('the branch name has changed',cls.bank_branch)
shiva=bank_v2('shiva',22,987654321,123456789)
shiva.withdraw()
        
        
       
        
