__author__ = 'Sharayah Reyes'


def isValid(prompt):
    response = input(prompt).lower()
    while True:
        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            print("Please enter Y or N")
            response = input(prompt).lower()
