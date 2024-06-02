"""Delete card v2 - asks user for card to search for and deletes card
 if found"""

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

while True:
    delete_card = input("Please enter card you are searching "
                        "for(x to exit): ").title()
    if delete_card == "X":
        break
    else:
        if delete_card in cards:
            # Deletes Card
            del cards[delete_card]
            print("Card deleted.\n")
for card_names, card_information in cards.items():
    print(f"{card_names}:{card_information}")
