class Bank:
    bank_name='sbi'
    bank_roi=7
    bank_branch='kizikistan'
    def __init__(self,n,a,b,ac):
        self.cname=n
        self.cage=a
        self.cbal=b
        self.caccount=ac
    @classmethod
    def bank_details(cls):
        print(f'name of the bank is {cls.bank_name}')
        print(f'roi of the bank is {cls.bank_roi}')
        print(f'branch of the bank is {cls.bank_branch}')
    def customer_details(self):
        print(f'name of the customer is {self.cname}')
        print(f'age of the customer is {self.cage}')
        print(f'balance of the customer is {self.cbal}')
        print(f'acccount of the customer is {self.caccount}')
    @staticmethod
    def get_int_value():
        iv=int(input('enter value'))
        return iv
    @staticmethod
    def get_str_value():
        sv=input('enter value')
        return sv
    def withdraw(self):
        amount=self.get_int_value()
        if amount>0:
            self.cbal-=amount
            print('withdraw is successfull')
        else:
            print('insufficient balance')
    def deposite(self):
        amount=self.get_int_value()
        if amount>0:
            self.cbal+=amount
            print('deposite has done')
        else:
            print('amount should be greater than 0')
    @classmethod
    def change_roi(cls):
        newroi=cls.get_str_value()
        cls.bank_roi=newroi
        print('roi is modified')
    @classmethod
    def change_branch(cls):
        bn=cls.get_str_value()
        cls.bank_branch=bn
        print('banks branch is modified')
govinda=Bank('govinda govinda',2000000,10000000000,11111)
malik=Bank('malik Bhasha',100,29999999,2222222)
govinda.withdraw()











            
        
