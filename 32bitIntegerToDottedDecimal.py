__author__ = 'Sharayah Reyes'

def inputNum():
    num = input("Please enter a 32-bit integer to convert it to "
                "dotted decimal notation: ")
    return num


def checkLen(num):
    while len(num) != 32:
        flag = 'false'
        return flag
    else:
        flag = 'true'
        return flag


def splitNum(num):
    first = num[0:8]
    second = num[8:16]
    third = num[16:24]
    fourth = num[24:32]
    return [first, second, third, fourth]


def calcDecimal(first):
    digits = 0
    digit = 0
    flag = 'true'
    for x in first:
        try:
            digit = int(x)
            if x not in {'0', '1'}:
                flag = 'false'
                break
        except ValueError:
            flag = 'false'
            break
        else:
            digits = digits * 2 + int(x)

    if flag == 'true':
        return digits
    else:
        print("Invalid Integer.")
        exit()


def main():
    flag = 'true'
    myList = []
    num = inputNum()
    flag = checkLen(num)
    if flag == 'true':
        myList = splitNum(num)
        part1 = calcDecimal(myList[0])
        part2 = calcDecimal(myList[1])
        part3 = calcDecimal(myList[2])
        part4 = calcDecimal(myList[3])
        print("Dotted decimal notation: ", part1, ".", part2, ".", part3, ".", part4, sep="")
    else:
        print("Not a valid 32-bit integer.")



main()


