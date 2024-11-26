class Bank:
    bank_name='sbi'
    bank_ifsc=1234
    bank_address='kizikistan'
girish=Bank()
vishnu=Bank()
#accesssing generic property using class
print(Bank.bank_name)
print(Bank.bank_ifsc)
#accessing generic property using object
print(girish.bank_name)
print(vishnu.bank_ifsc)
#modyfyig using object
girish.bank_address='pakistan'
print(girish.bank_address)
print(vishnu.bank_address)
#modifying using class
Bank.bank_ifsc=5678
print(Bank.bank_ifsc)
#del using class
del Bank.bank_ifsc
#print(Bank.bank_ifsc)
#print(girish.bank_ifsc)
#print(vishnu.bank_ifsc)
#del using object not possible
del girish.bank_address
print(girish.bank_address)
#create generic property usig class
Bank.bank_mobile=9876543210
print(Bank.bank_mobile)
print(girish.bank_mobile)
print(vishnu.bank_mobile)
