__author__ = 'Sharayah Reyes'


def playAgain():
    value = input("Would you like to play again? (Y/N): ").strip().lower()
    while True:
        if value == "y":
            return True
        elif value == "n":
            return False
        else:
            print("Please enter Y or N")
            value = input("Would you like to play again? (Y/N): ")


def getAnswer(prompt):
    while True:
        try:
            answer = float(input(prompt))
            if answer.is_integer():
                return answer
        except:
            print("Please enter a valid integer.")
