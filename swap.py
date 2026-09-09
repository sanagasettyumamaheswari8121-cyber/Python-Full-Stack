#swapping of 2 numbers without temp variable
a=10
b=20
a,b=b,a
print("a value is",a)
print("b value is",b)

#swaping of 2 numbers using temp variable
a=10
b=20
temp=a
a=b
b=temp
print("a value is",a)
print("b value is",b)

#swaping of 2 numbers using operators or arithmetic operators
a=10
b=20
a=a+b
b=a-b
a=a-b
print("the value of a is",a)
print("the value of b is",b)

#swaping of 2 numbers using formatting
a=10
b=20
a=a+b
b=a-b
a=a-b
print("after swapping a=%.2f,b=%.2f"%(a,b))

#swapping of 2 strings without temp variable
a="gnan"
b="code"
a,b=b,a
print(a)
print(b)

#swaping of 2 strings using temp variable
a="gnan"
b="code"
temp=a
a=b
b=temp
print("a value",a)
print("b value",b)
