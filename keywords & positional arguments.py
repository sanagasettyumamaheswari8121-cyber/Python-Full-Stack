#split bill
'''def splitbill():
    def amount():
        person=int(input("no.of persons:"))
        amount=int(input("amount:"))
        a=(int(amount/person))
        print("the amount per head is:",a)
    amount()
splitbill()'''

'''def splitbill():
    a=int(input("enter the total members"))
    b=int(input("enter the total amount"))
    print("perhead bill is",b//a)
splitbill()'''

#by using format method
'''def splitbill():
    a=int(input("enter the total members"))
    b=int(input("enter the total amount"))
    print("perhead bill is {}".format(b//a))
splitbill()'''

#by using f string
'''def splitbill():
    a=int(input("enter the total members"))
    b=int(input("enter the total amount"))
    print(f"perhead bill is {b/a}")
splitbill()'''

#by using format method
'''def splitbill():
    a=int(input("enter the total members"))
    b=int(input("enter the total amount"))
    c=b//a
    print("perhead bill is {}".format(c))
splitbill()'''

#by using f string
'''def splitbill():
    a=int(input("enter the total members"))
    b=int(input("enter the total amount"))
    c=b//a
    print(f"perhead bill is{c}")
splitbill()'''

#keyword & positional arguments
'''def Details(id,name,mailid):
    id=10
    name="ammu"
    mailid="ammu@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="ammulu",mailid="ammulu@gmail.com")
Details(id=30,name="uma",mailid="uma@gmail.com")
Details(40,"mahi","mahi@gmail.com")
Details("vigneswari","vigneswari@gmail.com",50)
Details(name="viggu",mailid="viggu@gmail.com",id=60)'''

#task
#employee details-> name,salary,designation
'''def employee(name,salary,designation):
    name="lucky"
    salary=20000
    designation="software engineer"
    print(name,salary,designation)
employee(name="name",salary="salary",designation="designation")'''

'''def employee(name,salary,designation):
    print(name,salary,designation)
employee(name="name",salary="salary",designation="designation")
employee(name="radha",salary="23500",designation="software developer")
employee(name="rekha",salary="30000",designation="frontend developer")
employee("ramu",22000,"analyst")
employee(28000,"data scientist","mouni")
employee(designation="backend developer",name="sowji",salary=21000)'''













