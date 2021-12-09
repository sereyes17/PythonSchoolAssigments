__author__ = 'Sharayah Reyes'

boyAvg = 0
girlAvg = 0
numB = 0
numG = 0
totalB = 0
totalG = 0
countB = 0
countG = 0

choice = input("Please enter 'b' for boy, 'g' for girl, or 'q' to quit: ")

while (choice != "q"):
        if (choice == "b"):
            numB = int(input("Please enter boys score: "))
            totalB += numB
            countB += 1
        elif (choice == "g"):
            numG = int(input("Please enter girls score: "))
            totalG += numG
            countG += 1
        else:
            print("Something went wrong please try again!")
        choice = input("Please enter 'b' for boy, 'g' for girl, or 'q' to quit: ")


if (countB > 0 and countG > 0):
    girlAvg = totalG / countG
    boyAvg = totalB / countB
else:
    print("Cannot divide by zero.")

print("Boy average:", boyAvg)
print("Girl average:", girlAvg)









