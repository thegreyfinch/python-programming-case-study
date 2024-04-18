# convert the answers below into code

# SOLANO:
'''
Define the variables x and y as lists of numbers 
x=[1, 2, 3, 4, 5] 
y=[11, 12, 13, 14, 15] 
z=(21, 22, 23, 24, 25)  
A.	What is the value of 3*x?  - Value of 3*x: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
B.	What is the value of x+y? - Value of x+y: [1, 2, 3, 4, 5, 11, 12, 13, 14, 15]
C.	What is the value of x-y?  - Value of x-y: ERROR
D.	What is the value of x[1]? - Value of x[1]: 2
E.	What is the value of x[0]? - Value of x[0]: 1
F.	What is the value of x[-1]? - Value of x[-1]: 5
G.	What is the value of x[:]? - Value of x[:]: [1, 2, 3, 4, 5] 
H.	What is the value of x[2:4]? - Value of x[2:4]: [3, 4]
I.	What is the value of x[1:4:2]? - Value of x[1:4:2]: [2, 4]
J.	What is the value of x[:2]? - Value of x[:2]: [1, 2]
K.	What is the value of x[::2]? - Value of x[::2]: [1, 3, 5]
L.	What is the result of the following two expressions? 
•	x[3]=8 - x[3]=8
•	print x - print x: [1, 2, 3, 8, 5]
'''


# ALOVEROS: 

x = [ 1,2,3,4,5]
y = [11,12,13,14,15,]
z = [21,22,23,24,25]

a = 3 * x
b = x + y
c = [x_val - y_val for x_val, y_val in zip(x,y)]
d = x[1]
e = x[0]
f = x[-1]
g = x[:]
h = x[2:4]
i = x[1:4:2]
j = x[:2]
k = x[::2]
x[3] = 8


print("x =",x)
print("y =",y)
print("z =",z)
print("\n3*x =",a)
print("x+y =",b)
print("x-y =",c)
print("x[1] =",d)
print("x[0] =",e)
print("x[-1] =",f)
print("x[:] =",g)
print("x[2:4] =",h)
print("x[1:4:2] =",i)
print("x[:2] =",j)
print("x[::2] =",k)
print(f"x ={x}")

# SINDAY:
a. [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5] 
b. [1, 2, 3, 4, 5, 11, 12, 13, 14, 15]
c. [1, 2, 3, 4, 5] - [11, 12, 13, 14, 15] 
d. 2
e. 1
f. 5
g. [1, 2, 3, 4, 5]
h. [3, 4]
i. [2, 4]
j. [1, 2]
k. [1, 3, 5]
l. The result of the expression `x[3]=8` assigns the value `8` to the e[1, 2, 3, 8, 5]`. Then, `print x` would output `[1, 2, 3, 8, 5]`.
