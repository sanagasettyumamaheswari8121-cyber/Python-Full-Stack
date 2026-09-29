#generators
#a=[expr for var in collection/range]
'''a=[i for i in range(16)]
print(a)
print(type(a))'''

'''a=[i for i in range(16)]
print(a)
print(*a)
print(type(a))'''

'''a=[i for i in range(16)]
#print(list(a))
#print(tuple(a))
print(set(a))'''

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(check(a,b)) #error'''

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        #yield a
        a=a+1
        yield a
print(*check(a,b))'''

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
print(*check(a,b)) #error'''

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check(a,b))'''

#yield v/s return
'''def mygen():
    #return "python"
    #return "java"
    #return "c"
    return "python","java","c"
print(*mygen())'''

'''def mygen1():
    yield "vij"
    yield "hyd"
    yield "vzg"
print(*mygen1())

#next()
b=mygen1()
print(next(b))
print(next(b))
print(next(b))'''
'''print(next(b))#error becoz there are 3 values only in mygen1()'''
