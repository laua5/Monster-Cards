"""Search card v5 - uses easygui and has choice boxes for user to search"""

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


# Trialling v3 - Using choice-boxes to ask for search_card name
def search():
    while True:
        # Get all card names as a list
        card_names = list(cards.keys())
        search_card = easygui.choicebox("Please select card you are searching"
                                        " for(cancel to exit): ",
                                        "search card", choices=card_names)
        if search_card is None:
            break
        search_list = []  # List to store the search_card details
        for card_name, card_info in cards.items():
            if search_card == card_name:
                search_list.append(f"Here is monster {card_name}'s "
                                   f"info:\n\n")
                for key in card_info:
                    search_list.append(f"{key}: {card_info[key]}\n")
        search1 = "".join(search_list)
        # Allows user to either exit or edit the program
        while True:
            exit_edit = easygui.buttonbox(f"{search1}\n Would you like to"
                                          f" edit this card?", "Exit or edit",
                                          choices=["Exit", "Edit"])
            if exit_edit == "Exit":
                break
            else:
                easygui.msgbox("Edit function will go here", "Edit")
                break


search()
