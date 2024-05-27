"""Edit card v3 - Uses Easygui, and also confirms with user their edits """

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
    while True:
        selected_stat = easygui.buttonbox(f"Which attribute of monster "
                                          f"{selected_card} would you like to"
                                          f" change?\n\nPlease"
                                          f" select your choice: ",
                                          "Selected Stat",
                                          choices=["Strength", "Speed",
                                                   "Stealth", "Cunning"])
        new_value = easygui.integerbox(f"Please enter new value for "
                                       f"{selected_stat}(Number between 1-25):"
                                       f" ", f"Edit {selected_stat}",
                                       lowerbound=1, upperbound=25)
        cards[selected_card][selected_stat] = new_value  # Updates Value
        edit_list = []  # List to store the search_card details
        for card_name, card_info in cards.items():
            if selected_card == card_name:
                edit_list.append(f"Here is monster {card_name}'s "
                                 f"new updated details:\n\n")
                for key in card_info:
                    edit_list.append(f"{key}: {card_info[key]}\n")
        updated_card = "".join(edit_list)
        more_edit = easygui.buttonbox(f"{updated_card} Would you like"
                                      f" to continue editing? (y for yes,"
                                      f" n for no): ", "Edit more?",
                                      choices=["Keep editing", "Exit"])
        if more_edit == "Exit":
            easygui.msgbox(f"{selected_card}'s new details have been saved",
                           "saved")
            break


while True:
    # This would be the card from search or add function
    the_card = easygui.enterbox("Please enter card name you would like to "
                                "change: ", "Card to edit").title()
    if the_card in cards:
        edit(the_card)
    elif the_card is None:
        break
    else:
        easygui.msgbox("Card not found.")
