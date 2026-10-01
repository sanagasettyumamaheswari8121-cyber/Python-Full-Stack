#filter()-> only remains what we need and delete remaining data 
'''a=[2,6,7,9,10,12,15,20,40,55,60,80]'''
'''if a%2==0: #if condition will not work
    print(a) #error'''

'''for i in a: #we should use for loop
    if i%2==0:
        print(i)'''

'''b=list(filter(lambda a:a%2==0,a)) #instead of for we can use filter
print(b)'''

#[],(),{},set()
'''a=[]
print(type(a))

b=()
print(type(b))

c=set()
print(type(c))

d={}
print(type(d))'''

'''a=[[],(),set(),{}," ",None,3,6.7,"python",6+9j,True,False] #withspace " "
b=list(filter(None,a)) 
print(b)'''

'''a=[[],(),set(),{},"",None,3,6.7,"python",6+9j,True,False]  #without space
b=list(filter(None,a)) 
print(b)'''

'''a=[[],(),set(),{}," ",3,6.7,"python",6+9j,True,False] #without none 
b=list(filter(None,a)) 
print(b)'''

#map()-> each ojbject from a collection and forms a new collection
#using max
'''a=[2,4,6,8,9,10,12,15,20,25]
b=[1,5,3,0,4,20,25,30,60,80]'''
'''c=list(map(max,a,b))
print(c)'''

#using min
'''d=list(map(min,a,b))
print(d)'''

#run time user input
#using int
'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)'''

#using list comprehension
'''a,b=[int(x) for x in input("values").split(",")]
print(a+b)'''

'''a,b=int(input("enter the values").split(","))
print(a+b) #error'''

#using map
'''a,b=map(int,input("enter the values").split(","))
print(a+b)'''

'''a=input("data1")
b=input("data2")
print(a+b)'''

'''a,b=[x for x in input("data").split(",")]
print(a+b)'''

'''a,b=input("data").split(",")
print(a+b)'''

'''a,b=map(str,input("data").split(","))
print(a+b)'''

'''a=list(map(int,input("data").split(",")))
print(a)'''

'''a=tuple(map(int,input("Data").split(",")))
print(a)'''

'''a=set(map(int,input("Data").split(",")))
print(a)'''

'''a=list(map(int,input("data").split(",")))
print(a)'''

'''a=tuple(map(int,input("data").split(",")))
print(a)'''

'''a=set(map(int,input("data").split(",")))
print(a)'''

'''a=list(map(str,input("data").split(",")))
print(a)'''

'''a=list(map(eval,input("data").split(",")))
print(a)'''

#using dictionary
'''a=input("enter the keey and value pairs")
b=dict(i.split(":") for i in a.split(","))
print(b)'''
