#range
#start-stop-step
'''for i in range(10):
    print(i)'''

'''for i in range(15,30):
    print(i)'''

'''for i in range(15,31):
    print(i)'''

#0,4,6,8,10,12,14,16,18
'''for i in range(0,20,2):
    print(i,end=",")'''

#5,10,15,20,25,30,35,40,45
'''for i in range(5,50,5):
    print(i,end=",")'''

#3,6,9,12,15,18,21,24,27
'''for i in range(3,30,3):
    print(i,end=",")'''

#student marks
'''while True:
    marks=int(input("Enter the marks: "))
    if marks in range(91,101):
        print("Grade-A")
    elif marks in range(81,91):
        print("Grade-B")
    elif marks in range(71,81):
        print("Grade-C")
    elif marks in range(50,71):
        print("Grade-D")
    else:
        print("Fail")'''

#student marks using for loop 
'''while True:
    marks=int(input("Enter the marks: "))
    for marks in range(91,101):
        print("Grade-A")'''

#attendence tracker  method 1
'''attendance ={"P","P","A","P","A"}
present = 0
absent = 0
total = 0
for i in attendance.split():
    total = total + 1
    if i == "P":
        present = present + 1
    elif i == "A":
        absent = absent + 1
print("Total students:", total)
print("Present:", present)
print("Absent:", absent)'''

#attendence tracker method 2
'''while True:
    students=int(input("Enter the total no. of students: "))
    p=0
    a=0
    for i in range(1,students+1):
        attendence=input(f"students {i} (p/a)")
        if attendence=="p":
            p+=1
        elif attendence=="a":
            a+=1
        else:
            print("Invalid data")
    print("..........Attendence Tracker..............")
    print("Total no. of students",students)
    print("Total no. of presentees",p)
    print("Total no. of absentees",a)'''
