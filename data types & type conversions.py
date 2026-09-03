Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatypess
>>> a=
SyntaxError: invalid syntax
>>> a=7
>>> type(a)
<class 'int'>
>>> b=6.7
>>> type(b)
<class 'float'>
>>> c='python'
>>> type(c)
<class 'str'>
>>> d='''codegnan'''
>>> type(d)
<class 'str'>
>>> e="codegnan'
SyntaxError: unterminated string literal (detected at line 1)
>>> e="codegnan"
>>> type(e)
<class 'str'>
>>> f=6+9j
>>> type(f)
<class 'complex'>
>>> g=4j+6
>>> type(g)
<class 'complex'>
>>> h=6j
>>> type(h)
<class 'complex'>
>>> x=5+9i
SyntaxError: invalid decimal literal
>>> i=6j+5j
>>> type(i)
<class 'complex'>
>>> #datatype conversions
>>> #int
>>> int(8)
8
int(7.5)
7
int("hi")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(7+5j)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int(7+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
type(i)
<class 'complex'>

float(8)
8.0
float(80.5)
80.5
float("hloo")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    float("hloo")
ValueError: could not convert string to float: 'hloo'
float(4+5j)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    float(4+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(false)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    float(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
float(False)
0.0

#str
str(8)
'8'
str(8.6)
'8.6'
str('Uma')
'Uma'
str(8+5j)
'(8+5j)'
str(False)
'False'
str(True)
'True'


#complex
complex(8)
(8+0j)
complex(8.6)
(8.6+0j)
complex('uma')
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    complex('uma')
ValueError: complex() arg is a malformed string
complex(8+5j)
(8+5j)
complex(True)
(1+0j)
complex(False)
0j


#boolean
bool(8)
True
bool(8.9)
True
bool(8+6j)
True
bool(True)
True
bool(False)
False
