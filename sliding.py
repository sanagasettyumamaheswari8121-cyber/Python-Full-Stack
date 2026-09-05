Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="codegnan"
a[0]+a[1]+a[2]+a[3]+a[4]
'codeg'
#slicing
a[0:3]
'cod'
a[0:4]
'code'
a[4:7]
'gna'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a
'codegnan'
a="work until you succeed"
a[5:10]
'until'
a[10:14]
' you'
a[11:14]
'you'
a[15-22]
's'
a[15:22]
'succeed'
a[0:4]
'work'
a;:4]
SyntaxError: unmatched ']'
>>> a[:4]
'work'
>>> b="vijayawada is a royal city"
>>> b[21:25]
' cit'
>>> b[22:26]
'city'
>>> b[16:21]
'royal'
>>> b[0:10]
'vijayawada'
>>> b[11:14]
'is '
>>> 
>>> #negative slicing
>>> c="happpy teachers day"
>>> c[-18:-14]
'appp'
>>> -14:-19]
SyntaxError: unmatched ']'
>>> c[-14:-19]
''
>>> c[-14:-18]
''
>>> a[-13:-18]
''
>>> a[-18:-13]
' unti'
>>> c[-18:-13]
'apppy'
>>> c="happy teachers day'
SyntaxError: unterminated string literal (detected at line 1)
>>> c="happy teachers day"
>>> c=[-18:-13]
SyntaxError: invalid syntax
>>> c[-18:-13]
'happy'
>>> c[-3:0]
''
