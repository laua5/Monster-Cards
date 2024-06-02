"""Monster card base v3 - connects edit function to search and add functions,
 also adds instructions (instructions optional at beginning), additional
  comments added throughout """

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


# Function to confirm cancellation if user presses cancel button
def confirm_cancel(yes_no_confirm, card_name):
    cancel_confirm = easygui.buttonbox(f"{yes_no_confirm}",
                                       "Confirm Cancel", choices=["Yes", "No"])
    if cancel_confirm == "Yes":
        del cards[card_name]  # Deletes card after cancellation
        return True
    return False


# Function to edit cards (from add or search function)
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
                                                   "Cunning", "Exit"])
        # Exit is used in case user accidentally continues editing instead
        # of exiting
        if selected_stat == "Exit":
            warning_exit = easygui.buttonbox("Exiting will save all details "
                                             "so far; it is only for if you "
                                             "wish to stop editing and exit."
                                             " Are you sure you wish to "
                                             "proceed?", "Warning",
                                             choices=["Yes", "No"])
            if warning_exit == "Yes":
                break
            else:
                continue
        elif selected_stat == "Name of card":
            while True:
                new_name = easygui.enterbox(f"Please enter new name for "
                                            f"{selected_card}(Add capitals "
                                            f"if needed): ", "New name")
                if new_name is None:
                    break
                elif new_name == "":
                    easygui.msgbox("Please enter a name(Can't be nothing).",
                                   "No name")
                    continue
                # Checks if name(lower and upper case) is already an
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
                                               f"{selected_stat}(Number "
                                               f"between 1-25):", f"Edit "
                                               f"{selected_stat}",
                                               lowerbound=1, upperbound=25)
                if new_value is None:
                    break
                else:
                    # Updates Value
                    cards[selected_card][selected_stat] = new_value
                    break
        edit_list = []  # List to store the search_card details
        for card_name, card_info in cards.items():
            if selected_card == card_name:
                edit_list.append(f"Here is monster {card_name}'s "
                                 f"new updated details(If cancel button was"
                                 f" pressed details remained the same):\n\n")
                for key in card_info:
                    edit_list.append(f"{key}: {card_info[key]}\n")
        updated_card = "".join(edit_list)
        more_edit = easygui.buttonbox(f"{updated_card} Would you like"
                                      f" to continue editing?: ", "Edit more?",
                                      choices=["Keep editing", "Save",
                                               "Cancel and Reset"])
        if more_edit == "Save":
            easygui.msgbox(f"{selected_card}'s new details have been saved",
                           "saved")
            break
        elif more_edit == "Cancel and Reset":
            # Revert to the original card details
            if selected_card != original_name:  # Checks if name has changed
                cards.pop(selected_card)
                cards[original_name] = original_card
            else:
                cards[selected_card] = original_card
            easygui.msgbox(f"Changes to {original_name} have been cancelled.",
                           "Changes cancelled")
            break


# Function to add cards
def add_card():
    # Message for when user presses cancel button
    yes_no_confirm = ("You pressed Cancel. All the details you have added thus"
                      " far will be deleted. Do you want to stop adding this "
                      "card and return to the card name input?")
    # Allows user to keep adding cards until x is entered
    while True:
        the_name = easygui.enterbox("Please enter name of new monster card"
                                    "(x to exit):\n\nAdd capitals if needed."
                                    " ", "New card name")
        if the_name == "x" or the_name is None:
            break
        elif the_name == "":
            easygui.msgbox("Please enter a name(Can't be nothing).", "No name")
            continue
        # Checks if name(lower and upper case) is already an existing card
        elif the_name.lower() in (name.lower() for name in cards):
            easygui.msgbox(f"Card name {the_name} has already been taken. "
                           f"Please enter another name, or exit the program.",
                           "Used name")
            continue
        else:
            while True:
                # Adds new monster card name to dictionary
                cards[the_name] = {}
                strength = easygui.integerbox(f"Please enter the strength "
                                              f"value of monster {the_name} "
                                              f"(Number 1-25): ",
                                              "strength", upperbound=25,
                                              lowerbound=1)
                if strength is None:
                    if confirm_cancel(yes_no_confirm, the_name):
                        break
                    else:
                        continue  # Asks user for strength value again
                cards[the_name]["Strength"] = strength
                speed = easygui.integerbox(f"Please enter the speed value of"
                                           f" monster {the_name}(Number 1-25):"
                                           f" ", "speed", upperbound=25,
                                           lowerbound=1)
                if speed is None:
                    if confirm_cancel(yes_no_confirm, the_name):
                        break
                    else:
                        continue  # Asks user for speed value again
                cards[the_name]["Speed"] = speed
                stealth = easygui.integerbox(f"Please enter the stealth value"
                                             f" of monster {the_name}"
                                             f"(Number 1-25): ",
                                             "stealth", upperbound=25,
                                             lowerbound=1)
                if stealth is None:
                    if confirm_cancel(yes_no_confirm, the_name):
                        break
                    else:
                        continue  # Asks user for stealth value again
                cards[the_name]["Stealth"] = stealth
                cunning = easygui.integerbox(f"Please enter the cunning value "
                                             f"of monster {the_name}"
                                             f"(Number 1-25): ", "cunning",
                                             upperbound=25, lowerbound=1)
                if cunning is None:
                    if confirm_cancel(yes_no_confirm, the_name):
                        break
                    else:
                        continue  # Asks user for cunning value again
                cards[the_name]["Cunning"] = cunning
                while True:
                    confirm_list = []  # List to store the new card details
                    for card_name, card_info in cards.items():
                        if card_name == the_name:
                            confirm_list.append(f"Here is {the_name}'s card "
                                                f"info:\n")
                            for key in card_info:
                                confirm_list.append(f"{key}: {card_info[key]}"
                                                    f"\n")
                    confirms = "".join(confirm_list)
                    confirm = easygui.buttonbox(f"\n{confirms}\nPlease confirm"
                                                f" these details. Select "
                                                f"confirm to confirm these "
                                                f"details and edit if you "
                                                f"would like to change: ",
                                                "confirmation",
                                                choices=["confirm", "edit",
                                                         "Cancel"])
                    if confirm == "confirm":
                        easygui.msgbox(f"{the_name} has been added to the "
                                       f"monster cards list.", "Confirmed")
                        break
                    elif confirm == "Cancel":
                        if confirm_cancel(yes_no_confirm, the_name):
                            break
                        else:
                            continue  # Returns to confirm
                    else:
                        edit(the_name)
                        break
                if confirm == "confirm" or confirm == "Cancel" or \
                        confirm == "edit":
                    break


# Function to search for cards and to edit if necessary
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
                edit(search_card)
                break


# Function to delete Monster cards
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


# Function to print out full list of cards
def print_list():
    decorator = "-" * 30  # Decoration used to separate each card
    easygui.msgbox("All cards and their details have been printed out to"
                   " Python console.", "List of cards")
    print("\n########## LIST OF MONSTER CARDS ##########")
    for card_name, card_info in cards.items():
        print(f"{decorator}\nMonster Name: {card_name}")
        for key in card_info:
            print(f"{key}: {card_info[key]}")


# Function used to show instructions to user (two-page instructions)
def instructions():
    easygui.msgbox("########## INSTRUCTIONS ########## \n\nPage 1:\n\n"
                   "This program is a catalogue containing several different"
                   " Monster cards. \nAfter viewing instructions you will"
                   " be allowed to either add, search, delete, or print cards."
                   "\n\n You will also be allowed to exit or view this message"
                   " again if necessary.\n\n* Add: This option will allow you"
                   " to add a card with attributes strength, speed, stealth"
                   " and cunning. After adding the card, you will be asked"
                   " to confirm your decision. If you wish to edit,"
                   " you will be directed to the edit function. "
                   "Confirming will add the card to the list, "
                   "while cancelling at any time will remove all "
                   "details you have just added.", "Instructions Page 1")
    easygui.msgbox("########## INSTRUCTIONS ########## \n\nPage 2:\n\n"
                   " * Search: This option allows you to search and view "
                   "any particular card and their stats. You can choose to"
                   " edit the card after searching.\n\n* Edit: This is an"
                   " option given from the add and search functions. You will"
                   " be allowed to change the name or stats of the card "
                   "you were viewing. Likewise, cancelling will undo all"
                   " changes you committed during the editing process.\n\n*"
                   " Delete:Allows you to delete a card.\n\n* Print: This"
                   " option will print out the full list of cards in the "
                   "python console.\n\n* View Instructions: You will be "
                   "redirected to this message.\n\n* Exit: This option"
                   " will exit the program. ", "Instructions Page 2")


# Welcome Message
easygui.msgbox("Welcome to Monster Cards!", "Welcome")
view_instructions = easygui.buttonbox("Would you like to view the"
                                      " instructions?", "View Instructions",
                                      choices=["Yes", "No"])
if view_instructions == "Yes":
    instructions()
while True:
    choice = easygui.buttonbox("\nWhat would you like to do?\n1: Add Monster "
                               "card\n2: Search for a Monster card\n3: Delete "
                               "a monster card\n4: Print full list of Monster "
                               "Cards\n5: View Instructions\n6: Exit\n\nPlease"
                               " select your choice: ", "Choices",
                               choices=["Add", "Search", "Delete", "Print",
                                        "View Instructions", "Exit"])
    if choice == "Add":
        add_card()
    elif choice == "Search":
        search()
    elif choice == "Delete":
        delete()
    elif choice == "Print":
        print_list()
    elif choice == "View Instructions":
        instructions()
    else:
        # Exit program
        easygui.msgbox("Goodbye, thanks for using this program!", "Exit")
        break
