Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="vijayawada"
a[1]
'i'
a[5]
'a'
a[2]
'j'
a[0],a[1]
('v', 'i')
a[0]+a[1]+a[2]+a[3]+a[4]
'vijay'

a="i am in class"
a[8]+a[9]+a[10]=
SyntaxError: cannot assign to expression
>>> a[8]+a[9]+a[10]
'cla'
>>> a[1]
' '
>>> a[5]+a[6]
'in'
>>> a[1]+a[4]+a[7]
'   '
>>> 
>>> a="i am learning python fullstack"
>>> a[14]+a[15]+a[15]+a[16]+
SyntaxError: invalid syntax
>>> a[14]+a[15]+a[15]+a[16]+a[17]+a[18]
'pyytho'
>>> a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
>>> a[2]=a[3]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a[2]=a[3]
TypeError: 'str' object does not support item assignment
>>> a[2]+a[3]
'am'
>>> 
>>> a="time is very precious"
>>> a[-8]+a[-7]
'pr'
>>> a[-8]+a[-7]+a[-6]+a[-5]
'prec'
>>> 
>>> a="codegnan it solutions"
>>> a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'solutions'
>>> a[-21]+a[20]+a[19]+a[18]
'csno'
>>> a[-21]+a[-20]+a[-19]+a[-18]
'code'
>>> a[-17]+a[-16]+a[-15]+a[-14]
'gnan'
