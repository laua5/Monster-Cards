"""Add card v3 - confirms detail with user"""

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


# Allows user to keep adding cards until x is entered
while True:
    the_name = input("Please enter name of new monster card(x to exit): ")
    cards[the_name] = {}
    if the_name == "x":
        break
    else:
        # Adds new monster card name to dictionary
        cards[the_name] = {}
        strength = int(input(f"Please enter strength of monster {the_name}"
                             f"(Number 1-25): "))
        cards[the_name]["strength"] = strength
        speed = int(input(f"Please enter speed of monster {the_name}"
                          f"(Number 1-25): "))
        cards[the_name]["speed"] = speed
        stealth = int(input(f"Please enter stealth of monster {the_name}"
                            f"(Number 1-25): "))
        cards[the_name]["stealth"] = stealth
        cunning = int(input(f"Please enter cunning of monster {the_name}"
                            f"(Number 1-25): "))
        cards[the_name]["cunning"] = cunning
        confirm_list = []  # List used to store the new card details
        for card_name, card_info in cards.items():
            if card_name == the_name:
                confirm_list.append(f"Here is {the_name}'s card info:\n")
                for key in card_info:
                    confirm_list.append(f"{key}: {card_info[key]}\n")
        confirms = "".join(confirm_list)
        confirm = input(f"\n{confirms}\nPlease confirm these details. Enter "
                        f"yes to confirm these details and no if you would "
                        f"like to change: ")
        if confirm == "yes":
            print(f"{the_name} has been added to the monster cards list.")
        else:
            # Edit function will be added here in full component
            print("Edit function will go here")
