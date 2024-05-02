"""Welcome page v2 - adds while loop and allows user to select options"""


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


print("Welcome to Monster Cards!")
print("Instructions will go here")
while True:
    choice = input("\nWhat would you like to do?\n1: Add Monster card"
                   "\n2: Search for a Monster card\n3: Delete a monster card\n"
                   "4: Print full list of Monster Cards\n5: View Instructions"
                   "\n6: Exit\n\nPlease enter your choice(Number 1-6): ")
    if choice == "1":
        print("Add card")
    elif choice == "2":
        print("Search for card")
    elif choice == "3":
        print("Delete card")
    elif choice == "4":
        print("Print list of cards")
    elif choice == "5":
        print("View Instructions")
    else:
        print("Exiting program")
        break
