#variable length arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
b=[4,5,7,1,2,6]
check(*b)
c=(3,4,2,5,1)
check(*c)
d={6,7,5,8,8}
check(*d)
e={"year":2026,"month":"sep"}
check(*e)'''

'''def check1(*a):
    d=1 #creating a variable
    print(a)
    print(type(a))
    for i in a:
        d=d+i
        print(d)
check1()
check1(2,3,4,5,6,7)
check1(2,3,4,3.4,4.2,5.3)
check1(3,4,5.2,3.2,4.4,"uma") #error'''

'''def check1(*a):
    d=1 #creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float): #to rectify the previous error
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6,7)
check1(2,3,4,3.4,4.2,5.3)
check1(3,4,5.2,3.2,4.4,"uma")'''

'''def check1(*a):
    d=1 #creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6,7)
check1(2,3,4,3.4,4.2,5.3)
check1(3,4,5.2,3.2,4.4,"uma",5+9j,True,False) #we added some more'''

#kwargs (keyword variable length arguments) (**) arguments
#to print whole dictionary
'''def details(**a):
    print(a)
    print(type(a))
details()
d={"names":["uma","mahi","ammu"], "marks":[80,90,95], "status":["a","p","p"]}
details(**d)'''

#to print separate keys & values
'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d={"names":["uma","mahi","ammu"], "marks":[80,90,95], "status":["a","p","p"]}
details(**d)'''

#*&** in single code
'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5,3.4,5.2)
details={"name":["uma","mahi","ammu"],"marks":[60,70,80]}
final(**details)
final(*data,**details)'''
