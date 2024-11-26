def generator_fun(name,_,lang):
	yield name+_+lang
res=generator_fun("panth","_","pythons")
print(next(res))
"""a=[1,3,5]
b=[1,2,6,1000]
print(a>b)
dit1={"apple":3,"banana":1}
dit2={"orange":2,"perl":4}
merge={**dit1,**dit2}
print(merge)
a='26_26'
b='mani'
print(int(a))
print(float(a))
print(str(a))
a=("mani"[1+1])
print(a)

my=[1,2,3,4,5]
my.clear()
print(my)

def string(a,b,separator):
	return a+separator+b
x=string('Hii','Mani',',')
print(x)

class python:
	def _init_(self):
		print("python is easy")
	def _init_(self):
		print("pytho is hard")
py=python()



lst=[2,4,6,8,10,12,14]
b=[]
for i in lst:
	b.append(i)
	lst.remove(i)
print(b)
print(lst)




a=[3,2,3,4,2,3,4,3]
b={}
for i in a:
	if i not in b.keys():
		b[i]=0
	b[i]=b[i]+1
n=[]
for key,val in b.items():
	n.append(val)
v=max(n)
for key,val in b.items():
	if val==v:
		print(key)"""	 