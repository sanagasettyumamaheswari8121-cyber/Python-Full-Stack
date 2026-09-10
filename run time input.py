'''a=10
b=20
print(a+b)

a=2
b=5
c=a+b
print(c)

print(4+8)'''

#run time user input
'''a=int(input("enter the a value"))
b=int(input("enter the b value"))
print(a+b)

a=float(input("enter the a value"))
b=float(input("enter the b value"))
print(a+b)'''

'''a=str(input("data1"))
b=str(input("data2"))
print(a+b)'''

'''a=input("data1")
b=input("data2")
print(a+b)'''

'''fname=input("first name")
lname=input("last name")
print((fname+" "+lname).title())'''

'''a=complex(input("enter the a value"))
b=complex(input("enter the b value"))
print(a+b)'''

'''a=bool(input("enter the a value"))
b=bool(input("enter the b value"))
print(a+b)'''

'''a=bool(input("enter the a value"))
b=bool(input("enter the b value"))
c=bool(input("enter the c value"))
print(a+b+c)'''

#run time user input options
'''a=int(input("enter the a value"))
b=int(input("enter the b value"))
option=int(input(choose the option
                 1.add
                 2.sub
                 3.mul))
print(a+b)
print(a-b)
print(a*b)'''

'''a=int(input("enter the a value"))
b=int(input("enter the b value"))
option=int(input("choose the option 1.add 2.sub 3.mul"))
print(a+b)
print(a-b)
print(a*b)

a=int(input("enter the a value"))
b=int(input("enter the b value"))
option=input("choose the option add sub mul")
print(a+b)
print(a-b)
print(a*b)'''

'''a=int(input())
b=int(input())
print(a+b)'''

'''a=input()
print(a)'''

#task 1 Student Profile
'''a=str(input("Student Profile"))
b=int(input("1.Id_No"))
c=str(input("2.Name"))
d=int(input("3.Mobile"))
e=str(input(" 4.MailId"))
f=str(input("5.College"))
g=str(input("6.Branch"))
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)'''

'''idno=int(input("enter the idno"))
name=input("enter the name")
mobileno=int(input("enter the mobile no"))
mailid=input("enter the mailid")
college=input("enter the college")
branch=input("enter the branch")
print("...........Student Profile...............")
print("idno is",idno)
print("name is",name)
print("mobileno is",mobileno)
print("mailid is",mailid)
print("college is",college)
print("branch is",branch)'''

#task 2
'''a=[10,20,30,40,50]
#[10,20,25,30,40,50]
a.insert(2,25)
print(a)'''

#task 3
'''a=["pthon","java","c"]
#{"python","java","c","c","o","d","e"]
a.extend("code")
print(a)'''

#task 4
'''a=("apple","banana","mango")
#("apple","banana","mango","kiwi")
b=list(a)
b.append("kiwi")
c=tuple(b)
print(c)'''

#task 5
'''a={"black","white","red"}
#{"black","red"}
a.remove("white")
print(a)'''

#task 6
a={"name":"pooja","city":"vij"}
#{"name":"pooja","city":"vij","state":"ap"}
a.update({"state":"ap"})
print(a)

