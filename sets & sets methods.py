Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets{}
a={7,4.5,"python",5+6j,True,False}
print(a)
{False, True, (5+6j), 4.5, 7, 'python'}
type(a)
<class 'set'>
b={7,8,6,1,8,2,4}
print(b)
{1, 2, 4, 6, 7, 8}
b={7,8,6,1,8,2,4.4.8,6}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
b={7,8,6,1,8,2,4,4,8,6}
print(b)
{1, 2, 4, 6, 7, 8}

#methods
a={4,5,6,7,8,9}
a.add(10)
a
{4, 5, 6, 7, 8, 9, 10}
a.add(12)
a
{4, 5, 6, 7, 8, 9, 10, 12}

#subset
a={4,5,6,7,8,9}
b={7,8,9}
b.issubset(a)
True
a.issubset(b)
False

#superset
a={6,7,8,9,10,11,012}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
a={6,7,8,9,10,11,12}
b=[10,11,12}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
b={10,11,12}
a.issuperset(b)
True
b.issuperset(a)
False

#union
a={3,4,5,6,7}
b={5,6,7,8,9,10]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
b={5,6,7,8,9,10}
a.union(b)
{3, 4, 5, 6, 7, 8, 9, 10}
b.union(a)
{3, 4, 5, 6, 7, 8, 9, 10}
a={3,4,5,6,7}
a={10,11,12,13,14,15}
b={14,15,16,17}
a.intersection(b)
{14, 15}
b.intersection(a)
{14, 15}

#update
a={2,3,4,5,6,7,8}
b={5,6,7,8,9,10}
a.update(b)
a
{2, 3, 4, 5, 6, 7, 8, 9, 10}
a
{2, 3, 4, 5, 6, 7, 8, 9, 10}
b
{5, 6, 7, 8, 9, 10}
b.update(a)
b
{2, 3, 4, 5, 6, 7, 8, 9, 10}
b
{2, 3, 4, 5, 6, 7, 8, 9, 10}

#difference
a={6,7,8,9,10,11}
b={2,3,4,5,6,7,8}
a.difference(b)
{9, 10, 11}
b.difference(a)
{2, 3, 4, 5}

#symmetric difference
a={7,8,9,10,11,12,13}
b={10,11,12,13,14,15}
a.symmetric_difference(b)
{7, 8, 9, 14, 15}

#is difference
a={3,4,5,6,7,8}
b={4,5,6,7,8,9,10}
a.difference_update(b)
a
{3}
a
{3}
b.difference_update(a)
b
{4, 5, 6, 7, 8, 9, 10}

#intersection update
a={3,4,5,6,7,8}
b={1,3,6,7,8,9,10}
a.intersection_upate(b)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a.intersection_upate(b)
AttributeError: 'set' object has no attribute 'intersection_upate'. Did you mean: 'intersection_update'?
a.intersection_update(b)
a
{8, 3, 6, 7}
a
{8, 3, 6, 7}
b.intersection_update(a)
b
{8, 3, 6, 7}
b
{8, 3, 6, 7}

#symmetric difference
#symmetric difference update
a={6,7,8,9,10,11,12}
b=[10,11,12,13,14]
a.symmetric_difference_update(b)
a
{6, 7, 8, 9, 13, 14}
a
{6, 7, 8, 9, 13, 14}
b.symmetric_difference_update(a)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    b.symmetric_difference_update(a)
AttributeError: 'list' object has no attribute 'symmetric_difference_update'
b.symmetric_difference_update(a)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    b.symmetric_difference_update(a)
AttributeError: 'list' object has no attribute 'symmetric_difference_update'

#pop
a={10,20,30,40,50}
a.pop()
50
a
{20, 40, 10, 30}
a.pop()
20
a.remove(10)
a
{40, 30}
a.pop(30)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    a.pop(30)
TypeError: set.pop() takes no arguments (1 given)

#discard
a={4,5,6,7,8,9}
a.discard(8)
a
{4, 5, 6, 7, 9}
a.copy()
{4, 5, 6, 7, 9}
a
{4, 5, 6, 7, 9}
b=a.copy()
b
{4, 5, 6, 7, 9}
>>> 
>>> #clear
>>> a={3,4,5,6,7}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> a.add(50)
>>> b
set()
>>> 
>>> #len
>>> a={5,6,7,8,}
>>> len(a)
4
>>> 
>>> #index
>>> a.index(4)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    a.index(4)
AttributeError: 'set' object has no attribute 'index'
>>> 
>>> #count
>>> a.count(5)
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    a.count(5)
AttributeError: 'set' object has no attribute 'count'
>>> 
>>> #dis joint
>>> a={3,4,5,6,7,8}
>>> b={2,3,4,6,7}
>>> a.isdisjoint(b)
False
>>> a={6,7,8,9}
>>> b={1,2,3,4}
>>> a.isdisjoint(b)
True
