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

def edit(selected_card):
    # Store original card details
    original_card = cards[selected_card].copy()
    original_name = selected_card
    while True:
        selected_stat = easygui.buttonbox(f"Which attribute of monster "
                                          f"{selected_card} would you like to"
                                          f" change?\n\nPlease"
                                          f" select your choice: ",
                                          "Selected attribute to edit",
                                          choices=["Name of card", "Strength",
                                                   "Speed", "Stealth",
                                                   "Cunning", "Cancel"])
        if selected_stat == "Cancel":
            break
        elif selected_stat == "Name of card":
            while True:
                new_name = easygui.enterbox(f"Please enter new name for "
                                            f"{selected_card}(Add capitals "
                                            f"if needed): ")
                if new_name is None:
                    break
                elif new_name == "":
                    easygui.msgbox("Please enter a name (can't be empty).",
                                   "No name")
                    continue
                # Checks if name (lower and upper case) is already an
                # existing card
                elif new_name.lower() in (name.lower() for name in cards):
                    easygui.msgbox(f"Card name {new_name} has already been "
                                   f"taken. Please enter another name, or "
                                   f"exit the program.", "Used name")
                    continue
                else:
                    # Transfer attributes to the new card name
                    cards[new_name] = cards.pop(selected_card)
                    easygui.msgbox(f"Card name changed from {selected_card} to"
                                   f" {new_name}.", "Name changed")
                    selected_card = new_name
                    break
        else:
            while True:
                new_value = easygui.integerbox(f"Please enter new value for "
                                               f"{selected_stat} (Number "
                                               f"between 1-25):", f"Edit "
                                               f"{selected_stat}",
                                               lowerbound=1, upperbound=25)
                if new_value is None:
                    break
                else:
                    # Updates Value
                    cards[selected_card][selected_stat] = new_value
                    break
        edit_list = []  # List to store the card's details
        for card_name, card_info in cards.items():
            if selected_card == card_name:
                edit_list.append(f"Here is monster {card_name}'s "
                                 f"new updated details:\n\n")
                for key in card_info:
                    edit_list.append(f"{key}: {card_info[key]}\n")
        updated_card = "".join(edit_list)
        more_edit = easygui.buttonbox(f"{updated_card} Would you like"
                                      f" to continue editing?: ", "Edit more?",
                                      choices=["Keep editing", "Save", "Cancel and Reset"])
        if more_edit == "Save":
            easygui.msgbox(f"{selected_card}'s new details have been saved",
                           "Saved")
            break
        elif more_edit == "Cancel and Reset":
            # Revert to the original card details
            if selected_card != original_name:  # Checks if name has changed
                cards.pop(selected_card)
                cards[original_name] = original_card
            else:
                cards[selected_card] = original_card
            easygui.msgbox(f"Changes to {original_name} have been discarded.",
                           "Changes discarded")
            break

while True:
    # This would be the card from search or add function
    the_card = easygui.enterbox("Please enter card name you would like to "
                                "change: ", "Card to edit")
    if the_card is None:
        break
    else:
        the_card = the_card.title()
        if the_card in cards:
            edit(the_card)
        else:
            easygui.msgbox("Card not found.")

for card_names, card_information in cards.items():
    print(f"{card_names}:{card_information}")