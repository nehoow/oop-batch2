#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
input1 = int(input("enter first number:"))
input2 = int(input("enter second number:"))
if input1 > input2:
    print (input2) 
else:
    print (input1)
#Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.
input1 = int(input("enter first number:"))
input2 = int(input("enter second number:"))
if input1 != input2:
    print ("Not Equal!")
#Prog03: Create a program that ask user to input 2 numbers. Print the difference of the two numbers.
input1 = int(input("enter first number:"))
input2 = int(input("enter second number:"))
difference = input1 - input2
print(difference)
#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point
input1 = int(input("enter first number:"))
input2 = int(input("enter second number:"))
quotient = input1 / input2
print(quotient)
#Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.
input1 = int(input("enter first number:"))
input2 = int(input("enter second number:"))
remainder = input1 % input2
print(remainder)
#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
d = int(input("enter fourth number:"))
e = int(input("enter fifth number:"))
f = int(input("enter sixth number:"))
g = int(input("enter seventhnumber:"))
h = int(input("enter  eigth number:"))
i = int(input("enter ninth number:"))
j = int(input("enter  tenth number:"))
difference = a - b - c - d - e - f - g - h - i - j
print(difference)

#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
even = 0 

for _ in range (10):
    num = int(input("Enter a number:"))
    if num % 2 == 0:
        even+= 1
        
print(even)
#Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
num = 0
while num <= 100:
    if num % 2 != 0:
        print(num)
    num+= 1
#Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.
for i in range(100):
    if i % 10 != 0:
        print (i)
    num+1
#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 < num2:
    for i in range(num1 + 1, num2):
        print(i, end=" ")
elif num1 > num2:
    for i in range(num2 + 1, num1):
        print(i, end=" ")
