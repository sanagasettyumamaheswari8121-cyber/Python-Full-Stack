#global and local variables
#first case of global variables
'''a=4
def check():
    print("inside value is",a)
check()
print("outside value is",a)'''

#second case of global variables
'''a=5
def check1():
    a=10
    a=a**2
    print("inside value is",a)
check1()
print("outside value is",a)'''

#third case of both global and local variables
'''a=3
def check2():
    a=8
    print("inside value is",a)
    a=10
    print("updated value is",a)
    b=12 #local variable
    b=b+a
    print("value of b is",b)
check2()
print("a value is",a)
print("b value is",b) #error becoz b is not defined outside'''

'''a=3
b=5
def check2():
    a=8
    print("inside value is",a)
    a=10
    print("updated value is",a)
    b=12 
    b=b+a
    print("value of b is",b)
check2()
print("a value is",a)
print("b value is",b)'''

#usage of global keyword
'''a=4
def final():
    global a
    print("inside value is",a)
    a=7
    print("updated value is",a)
    b=13 #local variable
    b=b+a
    print("b value is",b)
final()
print("a value is",a)
print("b value is",b)'''

'''a=4
def final():
    global a
    print("inside value is",a)
    a=7
    print("updated value is",a)
    global b
    b=13 
    b=b+a
    print("b value is",b)
final()
print("a value is",a)
print("b value is",b)'''

'''a=4
def final():
    global a,b
    print("inside value is",a)
    a=7
    print("updated value is",a)
    #global b
    b=13 
    b=b+a
    print("b value is",b)
final()
print("a value is",a)
print("b value is",b)'''
