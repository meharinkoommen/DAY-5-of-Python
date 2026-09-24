#Arithematic Operators: 

first_number=int(input("Enter the first number"))
second_number=int(input("enter the second number"))

#addition of first number and second number is 30

print(f"Addition of {first_number} and {second_number} is {first_number+second_number}")
print(f"Subtraction of {first_number} and {second_number} is {first_number-second_number}")
print(f"Multiplication of {first_number} and {second_number} is {first_number*second_number}")
print(f"Division of {first_number} and {second_number} is {first_number/second_number}")
#20/5
print(f"Floor division of {first_number} and {second_number} is {first_number//second_number}")
print(f"Modulus of {first_number} and {second_number} is {first_number%second_number}")
print(f"power of {first_number} and {second_number} is {first_number**second_number}")

#area of circle


radius=float(input("enter the radius of the circle"))
area=3.14*radius*radius
print(f"area of the circle is: {area}")




# simple interest

p=int(input("enter the amount"))
t=float(input("enter the time period"))
r=float(input("enter the rate of interest"))

simple_interest=p*t*r/100
print(f"simple interest is :{simple_interest}")



''' 

-----Assignment Operator-----
--> Assigning the value to the variables
eg: a=10

here= represent the assignment operators

'''


#10
a=int(input("Enter the number"))
print(f"Intially the value of a is: {a}")

a+=20

'''
a+=20
a=a+20
a=10+20
a=30

'''
print(f"After the value of a is: {a}")


b=30
b-=25

'''
b-=25
b=b-25
b=30-25
b=5

'''

print(b)


c=50
c+=25
c-=25
c*=25
c/=25
c//=25
c%=25
print(c)

'''
=--> is used to assign the value to the variable
==--> is used to compare the relation between two variable

'''

a=10
b=20

a==b
print(a)