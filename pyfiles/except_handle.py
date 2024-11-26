class PinError(BaseException):
    def __init__(self,msg):
        self.msg=msg
class BalError(BaseException):
    def __init__(self,msg):
        self.msg=msg

class Bank:
    Bank_name='sbi'
    bank_ifsc=1234
    def __init__(self,cn,cbal,pin):
        self.cname=cn
        self.cbalance=cbal
        self.pin=pin
    '''def withdraw(self):
        epin=int(input('enter pin'))
        try:
            if epin!=self.pin:
                raise PinError('Pin is not correct')
        except PinError as PE:
            print(PE)
        else:
            amount=int(input('enter amount'))
try:
    if amount>self.cbalance:
            raise BalError('insufficient balance')
        except BalError as BE:
            print(BE)
        else:
            self.cbalance-=amount
            print(self.cbalance)'''
    def withdraw(self):
        epin=int(input('enter pin'))
        try:
            if epin!=self.pin:
                raise PinError('Pin is not correct')
            
            try:
                if amount>self.cbalance:
                    raise BalError('insufficient balance')
            except BalError as BE:
                print(BE)
            else:
                self.cbalance-=amount
                print(self.cbalance)

        except PinError as PE:
            print(PE)
        else:
            amount=int(input('enter amount'))
anjali=Bank('anjali',10000,1234)
anjali.withdraw()


 






            
