__author__ = 'Sharayah Reyes'

students = ["John", "Joseph", "James", "Sarah", "Haley", "Damon", "Jason", "Amy", "Clay",
"Tessa", "Peter", "Parker", "Gwen", "Stacey", "Mary", "Jane", "Harry", "Bruce", "Ken", "Wayne"]

scores = [89,90,91,95,96,92,88,79,85,100,99,97,93,90,50,62,77,100,98,92]
scoreOutput = input("Please enter a student's name: ")


while scoreOutput != 'q':
        for x in range(20):
            if students[x] == scoreOutput:
                print("Student:", students[x], '', "Score:", scores[x])
            elif scoreOutput not in students:
                print("Name not in list.")
                break
        scoreOutput = input("Please enter a student's name: ")



