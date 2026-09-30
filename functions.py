'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''   

#functions
'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

'''def calculate(a,b):
    print("the integer division is",a//b)
    print("the power is",a**b)
    print("the mod is",a%b)
calculate(5,2)
calculate(6,4)
calculate(5,5)'''

#use cases
'''def add(a,b):
    c=a+b
    print(c)
add(4,5)'''

'''while True:
    def add():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    add()'''

'''def add():
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
    add()
add()'''

'''def fullname():
    fname=input("fname")
    lname=input("lname")
    print((fname+" "+lname).title())
fullname()'''

'''def mul(a,b):
    print(a*b)
mul(3,4)'''

'''def mul(a,b):
    return(a*b)
print(mul(3,4))'''

#print v/s return
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,4)'''

#return works 1st one only
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return(c)
    return(d)
    return(e)
print(cal(2,4))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return(c)
    return(d)
    return(e)
print(cal(2,4))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return(c)
    #return(d)
    #return(e)
    return c,d,e
print(cal(2,4))'''

'''while True:
    def cal():
        a=int(input("a value"))
        b=int(input("b value"))
        option=int(input(choose the option
                         1.add
                         2.sub
                         3.mul))
        if option==1:
            print(a+b)
        elif option==2:
            print(a-b)
        elif option==3:
            print(a*b)
        else:
            print("enter valid data")
    cal()'''

'''while True:       
    def cal():
        a=int(input("a value"))
        b=int(input("b value"))
        while True:
            option=int(input(choose the option
                             1.add
                             2.sub
                             3.mul))
            if option==1:
                print(a+b)
            elif option==2:
                print(a-b)
            elif option==3:
                print(a*b)
            else:
                print("enter valid data")
    cal()'''
        
'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("a value"))
    b=int(input("b value"))
    option=int(input(choose the option
                     1.add
                     2.sub
                     3.mul))
    if(option==1):
        add()
    elif(option==2):
        sub()
    elif(option==3):
        mul()
    else:
        print("invalid data")'''

'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("a value"))
    b=int(input("b value"))
    while True:
        option=int(input(choose the option
                     1.add
                     2.sub
                     3.mul))
        if(option==1):
            add()
        elif(option==2):
            sub()
        elif(option==3):
            mul()
        else:
            print("invalid data")'''
