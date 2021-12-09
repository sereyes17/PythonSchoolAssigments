__author__ = 'Sharayah Reyes'

# This program runs through ten randomly selected math questions

# Input: userAnswer, again
# Output: score, correctAnswer

import random
import Validation


def main():
    print("Welcome to the math test program! This program takes you through 10 "
          "randomly selected math problems and calculates your score at the end.")
    again = True

    while again:
        score = displayProblem()
        outputScore(score)
        again = Validation.playAgain()

    print("Bye!")


def displayProblem():
    score = 0

    for questionNum in range(1, 11):

        operands = ['+', '-', '*']
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(operands)
        correctAnswer = eval(str(num1) + operation + str(num2))
        print('\nQuestion number: {}'.format(questionNum))
        print("The question is", num1, operation, num2)
        userAnswer = Validation.getAnswer("What is your answer: ")
        if userAnswer == correctAnswer:
            print("Correct")
            score += 1
        else:
            print("Incorrect. The actual answer is", correctAnswer)
    return score


def outputScore(score):
    print("Score: " + str(score) + " out of 10.")


main()
