"""Edit card v2 - asks user what value they would like the stat changed to,
 and returns the changed details """


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

selected_card = "Websnake"  # This would be a user input

while True:
    selected_stat = input(f"Which attribute of monster {selected_card} "
                          f"would you like to change?\n1:Strength\n2:Speed\n"
                          f"3:Stealth\n4:Cunning\nPlease"
                          f" enter your choice: ").title()
    # Checks if stat is found
    if selected_stat in cards[selected_card]:
        new_value = int(input(f"Please enter new value for {selected_stat}"
                              f"(Number between 1-25): "))
        cards[selected_card][selected_stat] = new_value  # Updates Value
        print(f"Here are {selected_card}'s details:\n\n{cards[selected_card]}")
        more_edit = input("Would you like to continue editing?"
                          "(y for yes, n for no): ")
        if more_edit == "n":
            break
