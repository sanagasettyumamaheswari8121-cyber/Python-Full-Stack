Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=["hi","how","are","you"]
a.pop()
'you'
a
['hi', 'how', 'are']
a.pop("how")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.pop("how")
TypeError: 'str' object cannot be interpreted as an integer
a.pop(2)
'are'
a
['hi', 'how']

#remove
a.remove("how")
a
['hi']

#sort
a=["vij", "hyd", "vzg", "chennai"]
a.sort()
a
['chennai', 'hyd', 'vij', 'vzg']
b=[8,5,4,9,7,6]
b.sort()
b
[4, 5, 6, 7, 8, 9]
c=[6,9.0,"python",3+8j,True,False]
c.sort()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    c.sort()
TypeError: '<' not supported between instances of 'str' and 'float'

#reverse
a=['mango","banana","dragon"]
   
SyntaxError: unterminated string literal (detected at line 1)
a=["mango","banana","dragon"]
   
a.reverse()
   
a
   
['dragon', 'banana', 'mango']

#len
   
a=["c","c++","java"]
   
a.len(a)
   
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.len(a)
AttributeError: 'list' object has no attribute 'len'
len(a)
...    
3
>>> b="java"
...    
>>> len(b)
...    
4
>>> c=["java"]
...    
>>> len(c)
...    
1
>>> 
>>> #count
...    
>>> a.count("c")
...    
1
>>> #clear
...    
>>> a=["python",".net","hadoop"]
...    
>>> a.clear()
...    
>>> a
...    
[]
>>> b=[]
...    
>>> b.append("pooja")
...    
>>> b
...    
['pooja']
>>> b.append('append')
...    
>>> b
...    
['pooja', 'append']
