__author__ = 'Sharayah Reyes'

import random

# This program runs through a random, ten multiple choice questions relevant to information from Lord of the Rings.

# Input: user_answer, again
# Output: score, questions, answers

# Module main()
#   Declare Integer score
#   Declare String again
#
#   Display "Welcome to the Lord of the Rings trivia game. We will test your your knowledge with ten questions!"
#   Display "Let the game begin!"
#   Display ""
#   Set again = True

#   While again
#       Set score = run_test()
#       Call output_score(score)
#       Set again = play_again("Would you like to play again? (Y/N) ")
#   End While
#   Display "Thanks for playing!"


def main():

    print("Welcome to the Lord of the Rings trivia game. We will test your your knowledge with ten questions!")
    print("Let the game begin!")
    print()
    again = True

    while again:
        score = run_test()
        output_score(score)
        again = play_again("Would you like to play again? (Y/N) ")
    print("Thanks for playing!")

# Function String run_test()
#   Declare Integer Score
#   Set Score = 0
#
#   question = random.sample(range(1, len(questions) + 1), len(questions))
#   For num in question
#       Set user_answer = get_answer(questions[num - 1] + "What is your answer: ")
#       If user_answer == answers[num - 1] Then
#           Display "Correct!"
#           Display ""
#           score += 1
#       Else
#           Display "Incorrect!"
#           Display ""
#       End If
#     End For
#   Return Score
# End Function

def run_test():
    score = 0

    question = random.sample(range(1, len(questions) + 1), len(questions))
    for num in question:
        user_answer = get_answer(questions[num - 1] + "What is your answer: ")
        if user_answer == answers[num - 1]:
            print("Correct!")
            print()
            score += 1
        else:
            print("Incorrect!")
            print()
    return score


# Module String output_score(Integer score)
#   Display ""Your final score is " + str(score) + " out of " + str(len(questions))
# End Module

def output_score(score):
    print("Your final score is " + str(score) + " out of " + str(len(questions)))


# Function Boolean play_again(String prompt)
#   Declare String value
#
#   Display prompt
#   Input value
#   While True
#       If value == "y" Then
#           Return True
#       Else If value == "n" Then
#           Return False
#       Else
#           Display "Please enter Y or N"
#           Display prompt
#           Input value
#       End If
#    End While
# End Function

def play_again(prompt):
    value = input(prompt).strip().lower()
    while True:
        if value == "y":
            return True
        elif value == "n":
            return False
        else:
            print("Please enter Y or N")
            value = input(prompt)

# Function Boolean get_answer(String prompt)
#   Declare String answer

#   While True
#       Display prompt
#       Input answer
#       If answer in ("a", "b", "c") Then
#           Return answer
#       End If
#       Display "Please enter 'a', 'b', or 'c'."
#       Display ""
#   End While
# End Function

def get_answer(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("a", "b", "c"):
            return answer
        print("Please enter 'a', 'b', or 'c'.")
        print()

# Declare String questions = [
#   "How many rings rule them all?\n(a) Six-thousand\n(b) One\n(c) I don't know\n\n",
#     """What is the Elvish word for "friend?"\n(a) Melon\n(b) Amigo\n(c) I don't know\n\n""",
#     "Who wrote the Lord of the Rings trilogy?\n(a) J.R.R. Tolkien\n(b) Santa Claus\n(c) I don't know\n\n",
#     "Where must Frodo journey in order to destroy the ring?\n(a) Who-ville\n(b) Mt. Doom\n(c) I don't know\n\n",
#     "Before Bilbo acquired the ring, who possessed it?\n(a) Peregrin Took\n(b) Smeagol\n(c) I don't know\n\n",
#     "Who did Gandalf the Grey become after defeating the Balrog in Moria?\n(a) Gandalf the White\n(b) Morgoth\n(c) I don't know\n\n",
#     "Who was the only dwarf in the Fellowship?\n(a) Gimli\n(b) Grumpy\n(c) I don't know\n\n",
#     "The Nazgul, who are immortal wraiths, used to be of what race?\n(a) Elves\n(b) Men\n(c) I don't know\n\n",
#     "Who accompanied Frodo on his entire journey to destroy the ring?\n(a) Samwise Gamgee\n(b) Meriadoc Brandybuck \n(c) I don't know\n\n",
#     "Gandalf befriended what Eagle after healing his arrow-wound?\n(a) Thorin\n(b) Gwaihir \n(c) I don't know\n\n"

questions = [
    "How many rings rule them all?\n(a) Six-thousand\n(b) One\n(c) I don't know\n\n",
    """What is the Elvish word for "friend?"\n(a) Melon\n(b) Amigo\n(c) I don't know\n\n""",
    "Who wrote the Lord of the Rings trilogy?\n(a) J.R.R. Tolkien\n(b) Santa Claus\n(c) I don't know\n\n",
    "Where must Frodo journey in order to destroy the ring?\n(a) Who-ville\n(b) Mt. Doom\n(c) I don't know\n\n",
    "Before Bilbo acquired the ring, who possessed it?\n(a) Peregrin Took\n(b) Smeagol\n(c) I don't know\n\n",
    "Who did Gandalf the Grey become after defeating the Balrog in Moria?\n(a) Gandalf the White\n(b) Morgoth\n(c) I don't know\n\n",
    "Who was the only dwarf in the Fellowship?\n(a) Gimli\n(b) Grumpy\n(c) I don't know\n\n",
    "The Nazgul, who are immortal wraiths, used to be of what race?\n(a) Elves\n(b) Men\n(c) I don't know\n\n",
    "Who accompanied Frodo on his entire journey to destroy the ring?\n(a) Samwise Gamgee\n(b) Meriadoc Brandybuck \n(c) I don't know\n\n",
    "Gandalf befriended what Eagle after healing his arrow-wound?\n(a) Thorin\n(b) Gwaihir \n(c) I don't know\n\n"
]

# Declare String answers = ["b", "a", "a", "b", "b", "a", "a", "b", "a", "b"]

answers = ["b", "a", "a", "b", "b", "a", "a", "b", "a", "b"]

main()

# End Module