Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="python java"
b.replace("java", "c")
'python c'

#upper
a="python"
a.upper()
'PYTHON'
b="course"
b.upper()
'COURSE'

#lower
b="CODE"
b.lower()
'code'
c="JAVA"
b.lower()
'code'
c.lower()
'java'
c[0].upper()
'J'

#capitalize
c.capitalize()
'Java'
b.capitalize()
'Code'

d="python course"
d.title()
'Python Course'
e="i am in class"
e.title()
'I Am In Class'
e.capitalize()
'I am in class'

#conditions
a="hello world"
a.startswith("h")
True
a.endswith("d")
True
a.isalpha()
False
b="helloworld"
b.isaplha()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    b.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
b.isalpha()
True
a.isdigit()
False
b=3456
b.isdigit()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    b.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
c="1234"
c.isdigit()
True
a.isalnum()
False
b="java"
b.isalnum()
True
b="pythonisaprogramminglanguage"
b.isalnum()
True

#strip
#lstrip(), rstrip()
a"  pooja    "
SyntaxError: invalid syntax
a="  pooja    "
a.strip()
'pooja'
a.lstrip()
'pooja    '
a.rstrip()
'  pooja'

#concatenation
a="cod"
a="code"
b="gnan"
print(a=b)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    print(a=b)
TypeError: print() got an unexpected keyword argument 'a'
print(a+b)
codegnan
a="pyhton"
a=python"
SyntaxError: unterminated string literal (detected at line 1)
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
fname="pooja"
lname="ch"
print(fname+lname)
poojach
print(fname+" "+lname)
pooja ch
print(fname.title()+" "+lname.title())
Pooja Ch
print(fname+" "+lname).title())
SyntaxError: unmatched ')'
print(fname+" "+lname).title()
pooja ch
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    print(fname+" "+lname).title()
AttributeError: 'NoneType' object has no attribute 'title'
print((fname+" "+lname).title())
Pooja Ch

#split
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am learning python"
b.split()
['i', 'am', 'learning', 'python']

#join
b="vij","hyd",'vzg"
SyntaxError: unterminated string literal (detected at line 1)
b="vij","hyd","vzg"
"".join(b)
'vijhydvzg'
"".join(b)
'vijhydvzg'
" ".join(b)
'vij hyd vzg'
"k".join(b)
'vijkhydkvzg'
"k".join()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    "k".join()
TypeError: str.join() takes exactly one argument (0 given)
"k".join(b)
'vijkhydkvzg'
c="hello"
"m".join(c)
'hmemlmlmo'

#formatting
a=5
b=7
print(a+b)
12
print("the sum is",a+b)
the sum is 12
city='vij"
SyntaxError: unterminated string literal (detected at line 1)
city="vij'
SyntaxError: unterminated string literal (detected at line 1)
city="vij"
print("city is",city)
city is vij

#format method
a="motu"
b="pathulu"
print("hello {}{}".format(a,b))
hello motupathulu
print("hello {} {}".format(a,b))
hello motu pathulu
print("hello {}{}".format(a+" "+b))
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    print("hello {}{}".format(a+" "+b))
IndexError: Replacement index 1 out of range for positional args tuple
print("hello {} hello {}".format(a,b))
hello motu hello pathulu
print("hello {a}{b}".format())
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    print("hello {a}{b}".format())
KeyError: 'a'

#fstring
a="virat"
b="kohli"
print(f"hello {a} {b}")
hello virat kohli
print(f"hello {a}{b}")
hello viratkohli
print(f"hello {a} hello {b}")
hello virat hello kohli

fname="uma'
SyntaxError: unterminated string literal (detected at line 1)
fname="uma"
lname="s"
print("hello {}{}.format(fname,lname))
      
SyntaxError: unterminated string literal (detected at line 1)
print("hello {}{}".format(fname,lname))
      
hello umas
print("hello {} {}.format(fname,lname))
      
SyntaxError: unterminated string literal (detected at line 1)
print("hello {} {}".format(fname,lname))
      
hello uma s
print("hello {} hello {}".format(fname,lname))
      
hello uma hello s

print(f"hello {fname}{lname}")
      
hello umas
print(f"hello {fname} {lname}")
      
hello uma s
print(f"hello {fname} hello {lname}")
      
hello uma hello s

a=2
      
b=5
      
a=2
      
b=5
      
print("the sum is {} {}".format(a,b))
      
the sum is 2 5
>>> print("the sum is {}".format(a+b))
...       
the sum is 7
>>> c=a+b
...       
>>> print("the sum is{}".fromat(c))
...       
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    print("the sum is{}".fromat(c))
AttributeError: 'str' object has no attribute 'fromat'. Did you mean: 'format'?
>>> print("the sum is {}".fromat(c))
...       
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    print("the sum is {}".fromat(c))
AttributeError: 'str' object has no attribute 'fromat'. Did you mean: 'format'?
>>> print("the sum is {}".format(c))
...       
the sum is 7
>>> print(f"the sum is {c}")
...       
the sum is 7
>>> print(f"the sum is {a+b}")
...       
the sum is 7
>>> print(f"the sum is {}",format(a+b))
...       
SyntaxError: f-string: valid expression required before '}'
>>> print(f"the sum is {}".format(a+b))
...       
SyntaxError: f-string: valid expression required before '}'
>>> print("the sum is {}",format(a+b))
...       
the sum is {} 7
>>> print("the sum is {}".format(a+b))
...       
the sum is 7
