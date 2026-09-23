#max(),min(),sum()
'''print(max(2,4,5,9,14,19,25))'''

'''print(min(2,4,5,9,14,19,25))'''

'''print(sum(2,4,5,9,14,19,25))''' #error

'''a=2,4,5,9,14,19,25
print(sum(a))''' #crct procedure

'''print(sum([2,4,5,9,14,19,25]))'''

#marks analysis report task
'''print("--------Marks Analysis Report-----------")
students_count=int(input("No. of students: "))
a=[]
for i in range(1,students_count+1):
    marks=int(input(f"student no. {i} marks"))
    a.append(marks)
print("Total no.of students:",students_count)
print("Highest marks:",max(a))
print("Lowest marks:",min(a))
print("Total marks:",sum(a))
print("Average marks:",sum(a)/students_count)'''

#task on BMI
'''print("----------BMI-------------")
while True:
    weight=float(input("enter your weight: "))
    height=float(input("enter your height: "))
    BMI=weight/(height)**2
    if BMI<=18.5:
        print("Under Weight")
    elif BMI>18.5 and BMI<=24.5:
        print("Healthy Weight")
    elif BMI>24.5 and BMI<=29.5:
        print("Over Weight")
    elif BMI>30:
        print("Obesity")
    else:
        print("Pls enter valid data")'''
