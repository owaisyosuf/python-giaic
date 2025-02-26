import keyword

#operator in python

# A:Arithmetic operator
# B:Assignment operator
# C:Comparison operator
# D:Logical operator

# A:Arithmetic operator + ,-,/,*,%,**,//
a: int=10
b: int=20
print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplication
print(a/b) #division
print(a%b) #modulus/remainder
print(a**b) #exponent/power
print(a//b) #floor division/remove decimal point

# B:comparison operator ==,!=,>,<,>=,<=
a: int=10
b: int=20
print(a==b) #equal to (false)
print(a!=b) #not equal to (true)
print(a>b) #greater than (false)
print(a<b) #less than (true)
print(a>=b) #greater than or equal to (false)
print(a<=b) #less than or equal to (true)

# C:Logical operator and,or,not
a: int=10
b: int=20
print(a>b and a<b) #false
print(a>b or a<b) #true
print(not a>b) #true

# D:Assignment operator =,+=,-=,*=,/=,%=,**=,//=
a: int=10
a+=10 #a=a+10
print(a) #20  
a-=10 #a=a-10
print(a) #10
a*=10 #a=a*10
print(a) #100
a/=10 #a=a/10
print(a) #10.0
a%=10 #a=a%10
print(a) #0.0
a**=10 #a=a**10
print(a) #0.0
a//=10 #a=a//10
print(a) #0.0

#key word in python
print (keyword.kwlist) #list of keyword in python already import on top

#variable in python

# Valid variable names
name:str = "Alice"
_age:int = 25
salary2024: int = 50000
my_variable:str = "Python"

# Invalid variable names
# 2name = "Bob"          # ❌ Starts with a digit
# my-variable = "Error"  # ❌ Contains a hyphen
# class = "CS101"        # ❌ Uses a reserved keyword
print(name,_age,salary2024,my_variable) #Alice 25 50000 Python

#Assiging multiple values to multiple variables
a,b,c = 10,20,30