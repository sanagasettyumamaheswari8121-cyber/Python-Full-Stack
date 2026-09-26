#Right angle triangle
'''for i in range(1,6):     #rows
    for j in range(i):      #columns
        print("*",end="")   #stars
    print()                 #next row'''

#run tym user input 
'''n=int(input("enter the number: "))
for i in range(1,n+1):
    for j in range(i):
      print("*",end="")
    print()'''
      
#reverse right angle triangle
'''for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()'''

#run tym user input 
'''n=int(input("enter the number: "))
for i in range(n,0,-1):
    print("*"*i)'''

#square
'''for i in range(4):
    for j in range(4):
        print("*",end="")
    print()'''

#run tym user input 
'''n=int(input("enter the number:"))
for i in range(n):
    for j in range(n):
        print("* ",end="")
    print()'''

#pyramid
'''for i in range(1,5):
    for j in range(4-i):
        print(" ",end="")    
    for j in range(2*i-1):
        print("*",end="")   
    print()'''

#run tym user input 
'''n=int(input("enter the number: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    print("* "*i,end=" ")
    print()'''
