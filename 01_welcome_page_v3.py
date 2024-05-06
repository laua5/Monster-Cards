"""Welcome page v1 - welcomes user to program"""
import easygui


# Existing cards
cards = {
     "Stoneling": {"Strength": 7, "Speed": 1,
                   "Stealth": 25, "Cunning": 15},
     "Vexscream": {"Strength": 1, "Speed": 6,
                   "Stealth": 21, "Cunning": 19},
     "Dawnmirage": {"Strength": 5, "Speed": 15,
                    "Stealth": 18, "Cunning": 22},
     "Blazegolem": {"Strength": 15, "Speed": 20,
                    "Stealth": 23, "Cunning": 6},
     "Websnake": {"Strength": 7, "Speed": 15,
                  "Stealth": 10, "Cunning": 5},
     "Moldvine": {"Strength": 21, "Speed": 18,
                  "Stealth": 14, "Cunning": 5},
     "Vortexwing": {"Strength": 19, "Speed": 13,
                    "Stealth": 19, "Cunning": 2},
     "Rotthing": {"Strength": 16, "Speed": 7,
                  "Stealth": 4, "Cunning": 12},
     "Froststep": {"Strength": 14, "Speed": 14,
                   "Stealth": 17, "Cunning": 4},
     "Wispghoul": {"Strength": 17, "Speed": 19,
                   "Stealth": 3, "Cunning": 2}
}


easygui.msgbox("Welcome to Monster Cards!", "Welcome")
easygui.msgbox("Instructions will go here", "Instructions")
while True:
    choice = easygui.buttonbox("\nWhat would you like to do?\n1: Add Monster "
                               "card\n2: Search for a Monster card\n3: Delete "
                               "a monster card\n4: Print full list of Monster "
                               "Cards\n5: View Instructions\n6: Exit\n\nPlease"
                               " select your choice: ", "Choices",
                               choices=["Add", "Search", "Delete", "Print",
                                        "View Instructions", "Exit"])
    if choice == "Add":
        easygui.msgbox("Add card", )
    elif choice == "Search":
        easygui.msgbox("Search for card", "Search")
    elif choice == "Delete":
        easygui.msgbox("Delete card", "Delete")
    elif choice == "Print":
        easygui.msgbox("Print list of cards", "Print")
    elif choice == "View Instructions":
        easygui.msgbox("View Instructions", "View Instructions")
    else:
        easygui.msgbox("Exiting program", "Exit")
        break
