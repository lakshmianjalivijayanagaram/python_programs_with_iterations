class vinay:
    house='1bhk'
    bike='chetak'
    money=1000000
lakshmi=vinay()
class narayana(vinay):
    bike='ktm390'
    car='KIA'
asha=narayana()
'''
print(vinay.house)
print(lakshmi.house)
print(narayana.house)
print(asha.house)

print(vinay.money)
print(lakshmi.money)
print(narayana.money)
print(asha.money)
#modifiying parent class properties details by using parent class effetced in all
vinay.money=500000
print(vinay.money)
print(lakshmi.money)
print(narayana.money)
print(asha.money)
#modifiying parent class properties details by using parent class object effect in only parent class object
lakshmi.money=500000
print(vinay.money)
print(lakshmi.money)
print(narayana.money)
print(asha.money)
#modifiying parent class properties details by using child class object effected in child classs and its object
narayana.money=500000
print(vinay.money)
print(lakshmi.money)
print(narayana.money)
print(asha.money)
#modifiying parent class properties details by using child class object effects only in child class object 
asha.money=500000
print(vinay.money)
print(lakshmi.money)
print(narayana.money)
print(asha.money)
