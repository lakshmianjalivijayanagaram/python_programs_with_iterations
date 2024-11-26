class father:
    house='1bhk'
    field='2ecre'
    money=500000
class mother:
    gold='100grams'
class child(father,mother):
    car='TOYOTA'
    house='2bhk'
anjali=child()
print(anjali.house)
print(anjali.gold)
print(anjali.field)
    

