
]
Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arithmetic operators
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a//b)
0
print(a/b)
0.5
print(a%b)
2


#assignment operator
a=3
b=6
a+=b
a
9
a-=2
a
7
a*=3
a
21
a//=4
a
5
a/=3
a
1.6666666666666667
a%=3
a
1.6666666666666667
a**4
7.716049382716051
a
1.6666666666666667
a
1.6666666666666667
b
6
b+=2
b
8
b=6
b
6
b+=a
b
7.666666666666667
b-=a
b
6.0
b*=3
b
18.0
b//4
4.0
b/4
4.5
b%4
2.0
b/=4
b
4.5
b%=4
b
0.5
b**=2
b
0.25
b
0.25


#comparision operator
a=8
b=10
a<b
True
b>a
True
a>b
False
b<a
False
a!=b
True
a==b
False
a<=b
True
b>=a
True
a>=b
False
b<=a
False
a=10
b=10
a==b
True


#logical operator
a=5
b=10
a<b and b>a
True
a>b and b>a
False
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a<=b or B<a
True
a!=b or a==b
True
not True
False
not False
True


#identify or identity operator
a=4
type(a) is int
True
type(a) is not int
False
b=7.8
type(b) is float
True
type(b) is not float
False
type(a) is not float
True


#membership operator
a=3,4,5,6,7,8,9
9 in a
True
5 in a
True
10 in a
False
10 not in a
True
15 not in a
True
>>> 5 not in a
False
>>> 
>>> 
>>> #bitwise operator
>>> a=
SyntaxError: invalid syntax
>>> a=2
>>> b=6
>>> a&b
2
>>> bin(2)
'0b10'
>>> bin(6)
'0b110'
>>> a=4
>>> ~a
-5
>>> -(a+1)
-5
>>> b=-6
>>> ~b
5
>>> a=3
>>> b=5
>>> a^b
6
>>> a=4
>>> a<<2
16
>>> a=6
>>> a<<3
48
>>> a=3
>>> a>>2
0
>>> a=7
>>> a>>3
0
