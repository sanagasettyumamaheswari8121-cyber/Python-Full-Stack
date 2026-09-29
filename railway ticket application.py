#railway ticket application
#method 1
'''while True:
    print("----------Railway Ticket------------")
    ticket_price=1000
    print("Ticket Price is:",ticket_price)
    gender=input(("Enter your Gender: ").lower())
    age=int(input("Enter your Age: "))
    discount=0
    def ticket(gender):
        global discount
        if gender=="male":
            if age>=60:
                print("Senior Citizen")
                discount=int(ticket_price*(30/100))
                print("You have to pay:",ticket_price-discount)
            elif age<60:
                print("Normal Citizen")
                print("You have to pay:",ticket_price)
        elif gender=="female":
            if age>=60:
                print("Senior Citizen")
                discount=int(ticket_price*(50/100))
                print("You have to pay:",ticket_price-discount)
            elif age<60:
                print("Normal Citizen")
                discount=int(ticket_price*(30/100))
                print("You have to pay:",ticket_price-discount)
        else:
            print("Pls check your Gender")
    ticket(gender)'''

#method 2
'''def ticket_price(gender, age):
    price = 1000
    if gender == "male":
        if age > 60:
            discount = price * 30 / 100
            final_price = price - discount
            category = "Male Senior Citizen"
        else:
            final_price = price
            category = "Male Normal Citizen"
    elif gender == "female":
        if age > 60:
            discount = price * 50 / 100
            final_price = price - discount
            category = "Female Senior Citizen"
        else:
            discount = price * 20 / 100
            final_price = price - discount
            category = "Female Normal Citizen"
    else:
        print("Invalid gender")
        return
    print("-------Railway Ticket---------")
    print("Gender:", gender)
    print("Age:", age)
    print("Category:", category)
    print("Ticket Price:", price)
    print("Final Price:", final_price)
# Taking input from user
gender = input("Enter gender (male/female): ").lower()
age = int(input("Enter age: "))
ticket_price(gender, age)'''

#method 3
'''while True:
    def railway_ticket():
        ticket=1000
        gender=input("enter the gender")
        age=int(input("enter the age"))
        if gender=="m":
            if age>=60:
                print("senior citizen")
                ticket=ticket-30/100*ticket
                print(ticket)
            elif age<60:
                print("normal citizen")
                print(ticket)
        elif gender=="f":
            if age>=60:
                print("senior citizen")
                ticket=ticket-50/100*ticket
                print(ticket)
            elif age<60:
                print("normal citizen")
                ticket=ticket-30/100*ticket
                print(ticket)
    railway_ticket()'''
