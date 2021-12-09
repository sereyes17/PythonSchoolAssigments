__author__ = 'Sharayah Reyes'

# This program uses a dictionary to store to do lists for a day of the week
# starting with Mon-Fri

# Input: day, walk, bake, dinner, dishes, thing, command
# Output: day, walk, bake, dinner, dishes, thing

import ValidationToDo as v


def toDo():
    print("TO DO")
    print("list - List days of the week")
    print("show - Show things to do for specific day ")
    print("add -  Add something to do")
    print("edit - Edit the to do list")
    print("del -  Delete something to do")
    print("exit - Exit")
    print()


def listToDo(things):
    if len(things) == 0:
        print("There is nothing in the to do list.\n")
        return
    else:
        i = 1
        for thing in things:
            print(str(i) + ". " + thing)
            i += 1
        print()


def addEditDay(things, mode):
    day = input("Day: ")
    if mode == "add" and day in things:
        print(day + " this day is in already in the to do list.")
        response = v.isValid("Would you like to edit it? (y/n): ")
        if not response:
            return
    elif mode == "edit" and day not in things:
        print(day + " you don't have this day in the to do list yet.")
        response = v.isValid("Would you like to add it? (y/n): ")
        if not response:
            return

    walk = input("Walk dogs: ")
    bake = input("Bake: ")
    dinner = input("Dinner: ")
    dishes = input("Dishes: ")

    thing = {"Walk dogs": walk, "Bake": bake, "Dinner": dinner, "Dishes": dishes}

    things[day] = thing

    if mode == "add":
        print("Your new day has been added")
    elif mode == "edit":
        print("Your day has been updated.")
    else:
        print("Something went wrong, please try again.")


def deleteDay(things):
    day = input("Day: ")
    if day in things:
        del things[day]
        print(day + " was removed from the to do list.")
    else:
        print(day + " doesn't exist in the to do list.")


def showDay(things):
    thing = input("Enter a day:")
    if thing in things:
        day = things[thing]
        print("Day: " + thing)
        print("Walk dog(s): " + day["Walk dog(s)"])
        print("Bake: " + day["Bake"])
        print("Dinner: " + day["Dinner"])
        print("Dishes: " + day["Dishes"])
    else:
        print("Sorry, " + thing + " is not in the to do list.")


def main():
    toDo()

    things = {
        "Monday":
            {"Walk dog(s)": "Mojo & Sam", "Bake": "Lemon bars", "Dinner": "Margherita Pizza", "Dishes": "Sharayah"
             },
        "Tuesday":
            {"Walk dog(s)": "Bear & Lily", "Bake": "Brownies", "Dinner": "Chili", "Dishes": "Joe"
             },
        "Wednesday":
            {"Walk dog(s)": "Mojo & Sam", "Bake": "Sugar cookies", "Dinner": "Leftovers", "Dishes": "Joe & Sharayah"
             },
        "Thursday":
            {"Walk dog(s)": "Bear & Lily", "Bake": "Pumpkin pie", "Dinner": "Breakfast for dinner", "Dishes": "Joe"
             },
        "Friday":
            {"Walk dog(s)": "Mojo & Sam", "Bake": "Snickerdoodles", "Dinner": "Take-out", "Dishes": "Sharayah"
             },
    }

    while True:
        command = input("Command: ")
        if command == "show":
            showDay(things)
        elif command == "list":
            listToDo(things)
        elif command == "add":
            addEditDay(things, mode="add")
        elif command == "edit":
            addEditDay(things, mode="edit")
        elif command == "del":
            deleteDay(things)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Thanks, bye!")


main()
