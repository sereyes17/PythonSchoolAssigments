__author__ = 'Sharayah Reyes'
'''A simple calculator that outputs the users selected sum, difference, product or quotient of two numbers.'''

operation = input("Please input your operation (+,-,*,/): ")
numOne = int(input("Please enter your first number: "))
numTwo = int(input("Please enter your second number: "))

flag = 'true'

if (operation == "/" and numOne >= 0 and numTwo != 0):
    result = numOne / numTwo
elif (operation == "/" and numTwo == 0):
    flag = 'false'
    result = print("Sorry! Cannot divide by 0.")
elif (operation == "+"):
    result = numOne + numTwo
elif (operation == "-"):
    result = numOne - numTwo
elif (operation == "*"):
    result = numOne * numTwo
else:
    flag = 'false'
    print(operation, "is an invalid operator.")

if (flag == 'true'):
    print("Result:", result)