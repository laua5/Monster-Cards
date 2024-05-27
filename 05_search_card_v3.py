"""Search card v3 - uses easygui and has enter-boxes for user to search"""

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


# Trialling v1 - Using enter-boxes to ask for search_card name
def search():
    while True:
        card_found = False
        search_card = easygui.enterbox("Please enter card you are searching"
                                       " for(x to exit): ",
                                       "search card")
        search_list = []  # List to store the search_card details
        if search_card == "x" or search_card is None:
            break
        search_card = search_card.title()
        for card_name, card_info in cards.items():
            if search_card == card_name:
                search_list.append(f"Here is monster {card_name}'s "
                                   f"info:\n\n")
                for key in card_info:
                    search_list.append(f"{key}: {card_info[key]}\n")
                    card_found = True
        if not card_found:
            easygui.msgbox("Card not found.", "Card not found")
            continue
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
