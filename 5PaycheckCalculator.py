__author__ = 'Sharayah Reyes'
import datetime

#Lab 1
#Calculator program that averages and totals five paychecks
#Input: name, totalPaycheck
#Output: date, totalPaycheck, averagePaycheck

date = datetime.datetime(2020, 9, 15)
print("This program was made on", date.strftime("%x"))
print()

name = input("Please enter your name: ")
print("Hello " + name + " welcome to your paycheck calculator!")
print()
print("Please enter your last 5 paycheck totals and the calculator "
      "will average them out.")

totalPaycheck = 0
totalPaycheck = totalPaycheck + float(input("Enter amount: "))
totalPaycheck += float(input("Enter amount: "))
totalPaycheck += float(input("Enter amount: "))
totalPaycheck += float(input("Enter amount: "))
totalPaycheck += float(input("Enter amount: "))

averagePaycheck = round(totalPaycheck / 5)

print("Your total for your 5 paychecks is " + '${}'.format(totalPaycheck),
      "\nand your average take-home is " + '${}'.format(averagePaycheck) + ".")
print()
print("Good-bye!")