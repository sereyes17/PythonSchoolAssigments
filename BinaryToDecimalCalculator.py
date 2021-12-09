__author__ = 'Sharayah Reyes'


digits = 0
flag = 'true'
binary = input("Please enter an 8-bit binary number: ")

for x in binary:
    try:
        digit = int(x)
        if x not in {'0', '1'}:
            flag = 'error'
            break
        elif len(binary) != 8:
            flag = 'error'
            break
    except ValueError:
        flag = 'error'
        break
    else:
        digits = digits * 2 + int(x)

if flag == 'true':
    print("Decimal is:", digits)
else:
    print("Not a valid 8-bit binary number.")






