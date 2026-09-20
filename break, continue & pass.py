#break
#used for both no's & letters
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==7:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==7:
        break
    print(a)'''

'''a=10
while a>1:
    a=a-1
    if a==4:
        break
    print(a)'''

'''for i in range(10):
    if i==8:
        break
    print(i)'''

'''a="python"
if a=="h":
    break
print(a)'''#error

'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''

#continue
#used for both no's & letters
'''a=20
while a>5:
    a=a-1
    print(a)
    if a==12:
        continue'''

'''a=20
while a>5:
    a=a-1
    if a==12:
        continue
    print(a)'''

'''for i in range(15):
    if i==10:
        continue
    print(i)'''

'''a="python"
for i in a:
    print(i)
    if i=="y":
        continue'''

'''a="python"
for i in a:
    if i=="y":
        continue
    print(i)'''

#pass - place holder
'''a=5
while a>1:
    print(a)
    a=a-1
    if a==2:
        pass'''

'''for i in range(25):
    if i==10:
        pass
    print(i)'''

#ATM Application - method 1
'''balance=100000
card='c'
pwd=1234
a=input("Enter Type of Card: ")
if card==a:
    print("Welcome Uma")
    b=int(input("Enter the Password: "))
    if pwd==b:
        while True:
            option=int(input("Options: \n1.Balance Enquiry\n2.WithDraw\nEnter Option: "))
            if option==1:
                print(f"Your Balance: {balance}")
            elif option==2:
                withdraw=int(input("Enter Amount: "))
                if withdraw<=balance:
                    balance=balance-withdraw
                else:
                    print("Insufficeint balance")
            else:
                print("Invalid Option")
    else:
        print("Incorrect Password")
else:
    print("Inavlid Card")'''

#ATM Application - method 2
'''while True:
    account=100000
    pwd=1234
    card=input("insert the card")
    if card=="c":
        print("welcome uma")
        password=int(input("enter the password"))
        if password==pwd:
            option=int(input('''choose the option
                                1.balance enquiry
                                2.withdraw'''))
            if option==1:
                print("your account balance is",account)
            elif option==2:
                money=int(input("enter the amount"))
                print(money)
                balance=account-money
                print("remaining account balance is",balance)
            else:
                print("invalid option")
        else:
            print("incorrect password")
    else:
        print("invalid card")'''
