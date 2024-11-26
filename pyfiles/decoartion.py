'''def outer(arg):#arg=hai function address
    print('outer is started')
    print(arg)
    def inner():
        print('inner is started')
        arg()#hai function address
        print('inner is ended')
    print('inner is ended')
    return inner
@outer#hai=outer(hai function address)# hai=inner function address
def hai():
    print('hai is started')
    print('hai is ended')
hai()
    
def brother(arg):#arg=sister1 function address
    def inner():
        print('brother started monitoring')
        arg()#sisiter1 function address
        print('brother ended monitoring')
    return inner
@brother#sister1=brother(sister1 function address)#sister1=inner function address    
def sister1():
    print('sister1 started talking')
    print('sister1 ended talking')
sister1()
@brother#sister2=brother(sister2 function address)#sister2=inner function address    
def sister2():
    print('sister2 started talking')
    print('sister2 ended talking')
sister2()
'''
