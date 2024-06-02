"""Delete card v4 - uses Easygui, and uses
choice-box instead of enter-box"""

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


def delete():
    while True:
        # Get all card names as a list
        card_names = list(cards.keys())
        delete_card = easygui.choicebox("Please select card you are searching "
                                        "for(cancel to exit): ",
                                        "Card to delete", choices=card_names)
        if delete_card is None:
            break
        delete_card = delete_card.title()
        # Checks if card is found
        if delete_card in cards:
            while True:
                confirm_delete = easygui.buttonbox(f"Please confirm delete"
                                                   f" for {delete_card}: ",
                                                   f"Confirm delete",
                                                   choices=["Yes", "No"])
                if confirm_delete == "Yes":
                    # Deletes card
                    del cards[delete_card]
                    easygui.msgbox(f"Card {delete_card} has been deleted.",
                                   "Deleted Card")
                    break
                else:
                    break


delete()


for card_name, card_information in cards.items():
    print(f"{card_name}:{card_information}")
