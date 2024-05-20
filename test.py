import easygui

# Existing cards
cards = {
    "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}
}

# Allows user to keep adding cards until x is entered
while True:
    the_name = easygui.enterbox(
        "Please enter name of new monster card (x to exit): ", "New card name")
    if the_name == "x" or the_name is None:
        break
    else:
        while True:
            cancel_flag = False

            # Adds new monster card name to dictionary
            cards[the_name] = {}

            strength = easygui.integerbox(
                f"Please enter strength of monster {the_name} (Number 1-25): ",
                "strength", upperbound=25, lowerbound=1)
            if strength is None:
                cancel_confirm = easygui.buttonbox(
                    "You pressed Cancel. Do you want to stop adding this card and return to the card name input?",
                    "Confirm Cancel", choices=["Yes", "No"])
                if cancel_confirm == "Yes":
                    cancel_flag = True
                    break
            else:
                cards[the_name]["Strength"] = strength

            if not cancel_flag:
                speed = easygui.integerbox(
                    f"Please enter speed of monster {the_name} (Number 1-25): ",
                    "speed", upperbound=25, lowerbound=1)
                if speed is None:
                    cancel_confirm = easygui.buttonbox(
                        "You pressed Cancel. Do you want to stop adding this card and return to the card name input?",
                        "Confirm Cancel", choices=["Yes", "No"])
                    if cancel_confirm == "Yes":
                        cancel_flag = True
                        break
                else:
                    cards[the_name]["Speed"] = speed

            if not cancel_flag:
                stealth = easygui.integerbox(
                    f"Please enter stealth of monster {the_name} (Number 1-25): ",
                    "stealth", upperbound=25, lowerbound=1)
                if stealth is None:
                    cancel_confirm = easygui.buttonbox(
                        "You pressed Cancel. Do you want to stop adding this card and return to the card name input?",
                        "Confirm Cancel", choices=["Yes", "No"])
                    if cancel_flag == "Yes":
                        cancel_flag = True
                        break
                else:
                    cards[the_name]["Stealth"] = stealth

            if not cancel_flag:
                cunning = easygui.integerbox(
                    f"Please enter cunning of monster {the_name} (Number 1-25): ",
                    "cunning", upperbound=25, lowerbound=1)
                if cunning is None:
                    cancel_confirm = easygui.buttonbox(
                        "You pressed Cancel. Do you want to stop adding this card and return to the card name input?",
                        "Confirm Cancel", choices=["Yes", "No"])
                    if cancel_confirm == "Yes":
                        cancel_flag = True
                        break
                else:
                    cards[the_name]["Cunning"] = cunning

            if cancel_flag:
                continue

            confirm_list = []  # List used to store the new card details
            for card_name, card_info in cards.items():
                if card_name == the_name:
                    confirm_list.append(f"Here is {the_name}'s card info:\n")
                    for key in card_info:
                        confirm_list.append(f"{key}: {card_info[key]}\n")
            confirms = "".join(confirm_list)
            confirm = easygui.buttonbox(
                f"\n{confirms}\nPlease confirm these details. Select confirm to confirm these details and edit if you would like to change: ",
                "confirmation", choices=["confirm", "edit"])
            if confirm == "confirm":
                easygui.msgbox(
                    f"{the_name} has been added to the monster cards list.",
                    "confirmed")
                break
            else:
                # Edit function will be added here in full component
                easygui.msgbox("Edit function will go here", "edit")
                break
