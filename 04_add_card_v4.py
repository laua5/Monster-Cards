"""Add card v4 - adds easygui to function and thus only allows user to enter
number between 1-25 for stat values, also allows user to cancel if cancel
 button is pressed."""

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


def add_card():
    # Allows user to keep adding cards until x is entered
    while True:
        the_name = easygui.enterbox("Please enter name of new monster card"
                                    "(x to exit): ", "New card name")
        if the_name == "x" or the_name is None:
            break
        elif the_name == "":
            break
        else:
            while True:
                yes_no_confirm = ("You pressed Cancel. Do you want to stop "
                                  "adding this card and return to the card "
                                  "name input?")  # Message for when user
                # presses cancel button
                # Adds new monster card name to dictionary
                cards[the_name] = {}
                strength = easygui.integerbox(f"Please enter strength of "
                                              f"monster {the_name} "
                                              f"(Number 1-25): ",
                                              "strength", upperbound=25,
                                              lowerbound=1)
                if strength is None:
                    cancel_confirm = easygui.buttonbox(f"{yes_no_confirm}",
                                                       "Confirm Cancel",
                                                       choices=["Yes", "No"])
                    if cancel_confirm == "Yes":
                        del cards[the_name]  # Deletes card after cancellation
                        break
                    else:
                        continue  # Asks user for strength value again
                cards[the_name]["strength"] = strength
                speed = easygui.integerbox(f"Please enter speed of monster "
                                           f"{the_name}(Number 1-25): ",
                                           "speed", upperbound=25,
                                           lowerbound=1)
                if speed is None:
                    cancel_confirm = easygui.buttonbox(f"{yes_no_confirm}",
                                                       "Confirm Cancel",
                                                       choices=["Yes", "No"])
                    if cancel_confirm == "Yes":
                        del cards[the_name]  # Deletes card after cancellation
                        break
                    else:
                        continue  # Asks user for speed value again
                cards[the_name]["speed"] = speed
                stealth = easygui.integerbox(f"Please enter stealth of monster"
                                             f" {the_name}(Number 1-25): ",
                                             "stealth", upperbound=25,
                                             lowerbound=1)
                if stealth is None:
                    cancel_confirm = easygui.buttonbox(f"{yes_no_confirm}",
                                                       "Confirm Cancel",
                                                       choices=["Yes", "No"])
                    if cancel_confirm == "Yes":
                        del cards[the_name]  # Deletes card after cancellation
                        break
                    else:
                        continue  # Asks user for stealth value again
                cards[the_name]["stealth"] = stealth
                cunning = easygui.integerbox(f"Please enter cunningness of "
                                             f"monster {the_name}"
                                             f"(Number 1-25): ", "cunning",
                                             upperbound=25, lowerbound=1)
                if cunning is None:
                    cancel_confirm = easygui.buttonbox(f"{yes_no_confirm}",
                                                       "Confirm Cancel",
                                                       choices=["Yes", "No"])
                    if cancel_confirm == "Yes":
                        del cards[the_name]  # Deletes card after cancellation
                        break
                    else:
                        continue  # Asks user for cunning value again
                cards[the_name]["cunning"] = cunning
                confirm_list = []  # List used to store the new card details
                for card_name, card_info in cards.items():
                    if card_name == the_name:
                        confirm_list.append(f"Here is {the_name}'s card "
                                            f"info:\n")
                        for key in card_info:
                            confirm_list.append(f"{key}: {card_info[key]}\n")
                confirms = "".join(confirm_list)
                confirm = easygui.buttonbox(f"\n{confirms}\nPlease confirm "
                                            f"these details. Select confirm "
                                            f"to confirm these details and "
                                            f"edit if you would like to "
                                            f"change: ", "confirmation",
                                            choices=["confirm", "edit"])
                if confirm == "confirm":
                    easygui.msgbox(f"{the_name} has been added to the "
                                   f"monster cards list.", "confirmed")
                    break
                else:
                    # Edit function will be added here in full component
                    easygui.msgbox("Edit function will go here", "edit")
                    break


add_card()
