#list comprehension
'''a=["python","java","dsa"]'''
#Output ["PYTHON","JAVA","DSA"]
'''print(a.upper())'''

'''for i in a:
    print(i.upper(),end=" ")'''

'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''

#list comprehension syntax
#a=[expression for var in collection/range]
'''b=[i.upper() for i in a]
print(b)'''

b=["apple","mango"]
#Output ["Apple","Mango"]
'''c=[i.capitalize() for i in b]
print(c)'''

'''a=[1,2,3,5,6,8,12,13]
#[1,4,9,25,36,64,144,169]
b=[i**2 for i in a]
b=[i*i for i in a]
b=[pow(i,2) for i in a]
print(b)'''

#in range
'''a=[i for i in range(21)]
print(a)'''

#if usage in list comprehension
'''a=[i for i in range(16) if i%2==0]
print(a)'''

'''a=[i**2 for i in range(31) if i%2==0]
print(a)'''

'''a=["grapes","berry","mango","kiwi","dragon","apple"]
b=[i for i in a if "a" in i]
print(b)'''

'''a=["grapes","berry","mango","kiwi","dragon","apple"]
b=[i for i in a if "a" not in i]
print(b)'''

#no elif usage in list comprehension

#if-else usage in list comprehension
'''a=[i**2 if i%2==0 else i*5 for i in range(21)]
print(a)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
#Output [6,6,6,6,6]
'''c=a+b
print(c)'''

'''c=[a[i]+b[i] for i in range(5)]
print(c)'''

'''c=[a[i]+b[i] for i in range(len(a))]
print(c)'''
