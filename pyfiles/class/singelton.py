def singleton(arg):#arg=multiplex class address#decorator function
    l=[]
    def inner():
        if not l:
            mco=arg()
            l.append(mco)
        return l[0]
    return inner
@singleton#multiplex=singleton(address of multiplex class)#multiplex=innerfunction address
class multiplex:#decorated function
    def __init__(self):
        self.tickets=300
    def booking(self,nt):
        if nt<=self.tickets:
            self.tickets-=nt
            print('tickets booked successfully',)
            print('available tickets are',self.tickets)
        else:
            print('sorry,tickets are unavailable')
            print('available tickets are',self.tickets)
anjali=multiplex()
neethu=multiplex()
anjali.booking(200)
neethu.booking(100)

    
