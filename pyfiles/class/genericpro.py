#performing access,modify,update and create using class object
class bank:
    bank_name='sbi'
    bank_ifsc=1234
    bank_address='kizikistan'
girish=bank()
vishnu=bank()
'''#accessing generic property using class
print(bank.bank_name)
print(bank.bank_ifsc)
#accessing generic property using object
print(girish.bank_ifsc)
print(vishnu.bank_name)

#modifing generic property using class
bank.bank_ifsc=5678
print(bank.bank_ifsc)
print(girish.bank_ifsc)
print(vishnu.bank_ifsc)
#modifing generic property using object
vishnu.bank_address='pakistan'
print(vishnu.bank_address)
print(girish.bank_address)
print(bank.bank_address)

#deleting generic property using class
del bank.bank_ifsc
print(bank.bank_ifsc)
print(vishnu.bank_ifsc)
print(girish.bank_ifsc)
'''
#deleting generic property using object
#not poosible
#creating generic property using class
bank.bank_ph=123456789
print(bank.bank_ph)
print(vishnu.bank_ph)
print(girish.bank_ph)
#creating generic property using object-Not POSSIBLE


