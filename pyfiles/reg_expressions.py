import re
s='hai python'
re.match('h',s)
<re.Match object; span=(0, 1), match='h'>
re.match('\w{3}',s)
<re.Match object; span=(0, 3), match='hai'>

print(re.match('w',s))
None
print(re.match('p',s))
None
re.search('p',s)
<re.Match object; span=(4, 5), match='p'>
'?
re.search('h',s)
<re.Match object; span=(0, 1), match='h'>
re.findall('h',s)
['h', 'h']
re.findall('p',s)
['p']
re.findall('pi',s)
[]
re.finditer('h',s)
<callable_iterator object at 0x0000028A9AC0B5B0>
io=re.finditer('h',s)
for i in io:
    print(i)

    
<re.Match object; span=(0, 1), match='h'>
<re.Match object; span=(7, 8), match='h'>


import re
re.findall('h',s)
['h']
re.findall('.',s)
['H', 'a', 'i', ' ', 'h', 'e', '1', '2', '3', '@', '&', '.', '2', '3']
re.search('h',s)
<re.Match object; span=(4, 5), match='h'>
re.search('^h',s)
re.search('h$',s)
s='hai heep hep hp heep hello'
re.findall('hep',s)
['hep']
re.findall('he*p',s)
['heep', 'hep', 'hp', 'heep']

re.findall('he+p',s)
['heep', 'hep', 'heep']
re.findall('he?p',s)
['hep', 'hp']
re.findall('he{2}p',s)
['heep', 'heep']
re.findall('he{1,3}p',s)
['heep', 'hep', 'heep']
re.findall('abc',s)
[]
s='abc hai bye'
re.findall('abc',s)
['abc']
re.findall('he{1,3}p',s)
[]
re.findall('[a-l]',s)
['a', 'b', 'c', 'h', 'a', 'i', 'b', 'e']
s='Hai 123 HELLO'
re.findall('[a-z]',s)
['a', 'i']
re.findall('[a-zA-Z]',s)
['H', 'a', 'i', 'H', 'E', 'L', 'L', 'O']
re.findall('[a-zA-Z0-9]',s)
['H', 'a', 'i', '1', '2', '3', 'H', 'E', 'L', 'L', 'O']







import re
s='hai HELLO 123 BG@Lr'
re.findall('\w',s)
['h', 'a', 'i', 'H', 'E', 'L', 'L', 'O', '1', '2', '3', 'B', 'G', 'L', 'r']
re.findall('\W',s)
[' ', ' ', ' ', '@']
re.findall('\d',s)
['1', '2', '3']

re.findall('\D',s)
['h', 'a', 'i', ' ', 'H', 'E', 'L', 'L', 'O', ' ', ' ', 'B', 'G', '@', 'L', 'r']

re.findall('\s',s)
[' ', ' ', ' ']
re.findall('\S',s)
['h', 'a', 'i', 'H', 'E', 'L', 'L', 'O', '1', '2', '3', 'B', 'G', '@', 'L', 'r']
re.findall('[abc]',s)
['a']
re.findall('[ABCabc]',s)
['a', 'B']
re.findall('[^aAbBcC]',s)
['h', 'i', ' ', 'H', 'E', 'L', 'L', 'O', ' ', '1', '2', '3', ' ', 'G', '@', 'L', 'r']
re.findall('\A',s)
['']
s='hai helo abc 123'
re.findall('[abc]',s)
['a', 'a', 'b', 'c']
re.findall('[a-j]',s)
           
['h', 'a', 'i', 'h', 'e', 'a', 'b', 'c']
re.findall('[01234]',s)
           
['1', '2', '3']
re.findall('[0-4]',s)
           
['1', '2', '3']
s='89675455379071'
           
re.findall('[0-9]',s)
           
['8', '9', '6', '7', '5', '4', '5', '5', '3', '7', '9', '0', '7', '1']
re.findall('[4-9][0-9]',s)
           
['89', '67', '54', '55', '79', '71']
re.findall('[4-9][0-9]{2}',s)
           
['896', '754', '553', '790']
re.findall('[a-zA-Z]',s)
           
[]
s='hai.123.anjali'
           
re.findall('[.]',s)
           
['.', '.']
s='98.765'
re.findall('\d+[.]\d+',s)
['98.765']
re.findall('(\d)[.](\d+)',s)
[('8', '765')]
re.findall('(\d+)[.](\d+)',s)
[('98', '765')]
s='98.77.345678'
re.findall('(\d+)([.])(\d+)',s)
[('98', '.', '77')]
re.findall('(\d+)([.])(\d+)([.])(\d+)',s)
[('98', '.', '77', '.', '345678')]
s='567.56.65789.56789'
re.sub('[.]','@',s)
'567@56@65789@56789'
s
'567.56.65789.56789'
re.sub('[.]','@',s,3)
'567@56@65789@56789'
re.sub('[.]','@',s,2)
'567@56@65789.56789'
re.subn('[.]','#',s)
('567#56#65789#56789', 3)
re.findall('i/B',s)
[]
p='i shivapriya'
re.findall('i\B',p)
['i', 'i']
re.findall('\Bi',p)
['i', 'i']
re.findall('i\b',p)
[]
re.findall('\bi',p)
[]
re.findall(r'i\B',p)
['i', 'i']
re.findall(r'\Bi',p)
['i', 'i']
p='i shivapriyai'
re.findall(r'\Bi',p)
['i', 'i', 'i']
re.findall(r'i\B',p)
['i', 'i']
p='i shivapriyai'
re.findall(r'i\B',p)
['i', 'i']
p='ishivapriyai'
re.findall(r'i\B',p)
['i', 'i', 'i']
p='ia shivapriyai'
re.findall(r'i\B',p)
['i', 'i', 'i']
re.findall(r'i\B',p)
['i', 'i', 'i']
re.findall(r'i\Bi',p)
[]
p='iii'
re.findall(r'i\Bi',p)
['ii']

pa='(([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(0|[1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){2}(0|[1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'













