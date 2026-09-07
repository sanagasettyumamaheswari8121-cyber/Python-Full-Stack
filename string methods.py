Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a="python"
len(a)
6
b='python course"
SyntaxError: unterminated string literal (detected at line 1)
b="python course"
len(b)
13
c""
SyntaxError: invalid syntax
c=""
len(c)
0
d=" "
len(d)
1


#count
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("t")
5
a.count(l)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.count(l)
NameError: name 'l' is not defined
a.count("l")
4
>>> a.count(" ")
3
>>> 
>>> 
>>> #find a string
>>> a="python"
>>> a[1]
'y'
>>> a.find("y")
1
>>> a.find("0")
-1
>>> a.find("o")
4
>>> b="hello"
>>> b.find("l")
2
>>> b[2:4]
'll'
>>> 
>>> 
>>> #escape sequences
>>> #\n->new line
>>> #\t->tab space
>>> a='idno\nname\tmobileno\nmailid\nbranch\tcollege"
SyntaxError: unterminated string literal (detected at line 1)
>>> a="idno\nname\tmobileno\nmailid\nbranch\tcollege"
>>> print(a)
idno
name	mobileno
mailid
branch	college
>>> b="idno:10\nname:pooja\tmobileno:7898908908\nmailid:pooja@codegnan\nbranch:cse\tcollege:NRI college"
>>> print(b)
idno:10
name:pooja	mobileno:7898908908
mailid:pooja@codegnan
branch:cse	college:NRI college
