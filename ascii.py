#ASCII - American Standard Code for Information Interchange
#Chr, Ord
'''print(chr(65))'''
'''print(chr(90))'''
'''print(chr(92))'''
'''print(ord("a"))'''
'''print(ord("z"))'''
'''print(chr("a"))#error'''
'''print(ord(65))#error'''

#A-Z in single line
'''for i in range(65,91):
    print(chr(i),end= " ")'''

#a-z in single line
'''for i in range(97,123):
    print(chr(i),end= " ")'''

#ascii for my name
'''n=input("enter your name")
for i in n:
    print(ord(i),end=" ")'''

'''n=input("enter your name")
for i in n:
    print(i,ord(i))'''

'''n=input("enter your name")
for i in n:
    print(i,"-",ord(i))'''
