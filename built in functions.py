#max(),min(),sum(),type(),len(),input(),range(),next()
'''while True:
    n=list(map(int,input("Enter numbers: ").split(",")))
    print("Max:",max(n))
    print("Min:",min(n))
    print("Sum:",sum(n))
    print("Type:",type(n))
    print("Length:",len(n))
    for i in range(len(n)):
        print(n[i])
    x=(i for i in n)
    print("First value:", next(x))
    print("Second value:", next(x))
    print("Second value:", next(x))'''

#built in functions
#from keys()
'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))'''

#print(dict(a))#error

'''a="codegnan"
b=dict.fromkeys(a)
print(b)
c=dict.fromkeys(a,"uma")
print(c)
c["g"]="python"
print(c)'''

#eval
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''

'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''

'''while True:
    a=input("a value")
    b=input("b value")
    print(a+b)'''

'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''

#zip()-> we can collect multiple collections into one collection
'''a=[10,20.30,40,50]
names=["uma","mahi","ammu","vigneswari","ammulu"]
print(a+names)

b=zip(a,names)
print(b) #0x000001BA4BE9D6C0

c=list(zip(a,names))
print(c)

d=tuple(zip(a,names))
print(d)

e=dict(zip(a,names))
print(e)

f=set(zip(a,names))
print(f)'''

#enumerate-> we can give counter to the collection
names=["uma","mahi","ammu","vigneswari","ammulu"]
'''for i in range(names):
    print(i) #error'''

'''for i in range(len(names)):
    print(i)'''

'''for i in range(len(names)):
    print(i,names[i])''' 

'''b=list(enumerate(names))
print(b)'''

'''c=tuple(enumerate(names))
print(c)'''

'''d=set(enumerate(names))
print(d)'''

'''e=dict(enumerate(names))
print(e)'''

#annonymous functions -> these are nameless functions and we can use a keyword called as lambda to create annonymous functions
#task - write a function to calculate 2*x+5 where x=5
'''def f(x):
    print(2*x+5)
f(5)'''

#run time user input
'''def f():
     x=int(input("value"))
     print(2*x+5)
f()'''

#syntax
#a=lambda arg:exp
'''a=lambda x:2*x+5
print(a(5))'''

#run time user input
'''a=int(input("a value"))
b=lambda x:2*x+5
print(b(a))'''

#tasks
'''a=lambda x,y:x*y
print(a(5,8))'''

a="python"
#output:- PYTHON
'''b=lambda x:a.upper()
print(b(a))'''

'''b=lambda a:a.upper()
print(b("python"))'''

#first name + last name = full name
'''firstname=input("first name")
lastname=input("last name")
fullname=lambda a,b:a+" "+b
print(fullname(firstname,lastname))'''

#first name + last name = full name ----- by using generators list comprehension
'''a,b=[x for x in input("names").split(",")]
c=lambda a,b:a+" "+b
print(c(a,b))'''

'''a,b=[x for x in input("names").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''
