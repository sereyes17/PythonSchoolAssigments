__author__ = 'Sharayah Reyes'

feet = int(input("Please enter your height in feet: "))
inch = int(input("...and inches: "))
weight = int(input("Please enter your weight in pounds: "))

calculateW = weight * 703
feetToInches = feet * 12 + inch
square = feetToInches * feetToInches

calculate = calculateW / square

print("Your BMI is", calculate)