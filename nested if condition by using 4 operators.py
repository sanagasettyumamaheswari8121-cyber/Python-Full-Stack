#nested if condition by using comparision operators
'''a=6
b=12
if a<b:
    print("less")
    if b>a:
        print("greater")'''

'''a=6
b=12
if a>b:
    print("a is greater")
    if b>a:
        print("b is greater")'''

'''a=6
b=12
if a==b:
    print("equal")
    if b>a:
        print("b is greater")'''

'''a=10
b=20
if a<b:
    print("a is less")
    if b==a:
        print("equal")'''

'''a=10
b=20
if a<b:
    print("a is less")
    if b==a:
        print("equal")
    else:
        print("false")'''

'''a=30
b=50
if a>b:
    print("a is greater")
    if b>a:
        print("b is greater")
else:
        print("less")'''

'''a=60
b=80
if a<b:
    print("a is less")
    if b>a:
        print("b is greater")
    else:
        print("a is greater")
else:
    print("false")'''

'''a=60
b=80
if a>b:
    print("a is greater")
    if b==a:
        print("equal")
    else:
        print("b is greater")
else:
    print("false")'''

'''a=60
b=80
if a<b:
    print("less")
    if b==a:
        print("equal")
    elif a!=b:
        print("not equal")
    else:
        print("false")
else:
    print("true")'''

#nested if condition by using logical operators
'''a=20
b=40
if a<b and b>a:
    print("less")
    if b>a or b==a:
        print("greater")
        if not b<a and b==a:
            print("not equal")
else:
    print("it is equal")'''

#nested if condition by using identify operators
'''a=5
if type(a) is int:
    print("it is int")
    if type(a) is not int:
        print("it is not int")
else:
    print("it is float")'''

#nested if condition by using membership operators
'''a=[5,6,7,8]
if 10 not in a:
    print("it is in a")
    if 6 not in a:
        print("it is not in a")
    elif 6 in a:
        print("it is in a")
else:
    print("it is in float")'''
