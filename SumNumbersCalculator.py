__author__ = 'Sharayah Reyes'

numbers = []
newNum = 1
flag = 'true'

while newNum != 0:
    try:
        newNum = int(input("Please enter a number, enter 0 for sum: "))
        if newNum != 0:
            numbers.append(newNum)
    except ValueError:
        flag = 'false'
        break

if flag == 'true':
    print("The sum of the numbers you entered is: ", end="")
    print(*numbers, sep=" + ", end="")
    print(" =", (sum(numbers)))
else:
    print("Not a valid integer")
