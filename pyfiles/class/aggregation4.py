class bank:
    bank_name='sbi'
    bank_ifsc=1234
    bank_ph=731877577
    def __init__(self,cn,ca,cb):
        self.cname=cn
        self.cage=ca
        self.cbal=cb
    @staticmethod
    def get_int_val():
        iv=int(input())
        return iv
    def withdraw(self):
        amt=self.get_int_val()
        if amt<self.cbal:
            self.cbal-=amt
            print('withdraw is successful')
        else:
            print('insufficient amount')
    @classmethod
    def change_ifsc(cls):
        ifsc=cls.get_int_val()
        cls.bank_ifsc=ifsc
        print('ifsc has changed to',cls.bank_ifsc)
anjali=bank('anjali',21,100000)
#bank.change_ifsc()
#anjali.change_ifsc()
anjali.withdraw()
