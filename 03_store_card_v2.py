"""Store card v2 - using lists"""

# Existing cards
cards = {"Stonelling": [["Strength", 7], ["Speed", 1], ["Stealth", 25],
                        ["Cunning", 15]],
         "Vexscream": [["Strength", 1], ["Speed", 6], ["Stealth", 21],
                       ["Cunning", 19]],
         "Dawnmirage": [["Strength", 5,], ["Speed", 15], ["Stealth", 18],
                        ["Cunning",22]],
         "Blazegolem": [["Strength", 15], ["Speed", 20], ["Stealth", 23],
                        ["Cunning", 6]],
         "Websnake": [["Strength", 7], ["Speed", 15], ["Stealth", 10],
                      ["Cunning", 5]],
         "Moldvine": [["Strength", 21], ["Speed", 18], ["Stealth", 14],
                      ["Cunning", 5]],
         "Vortexwing": [["Strength", 19], ["Speed", 13], ["Stealth", 19],
                        ["Cunning", 2]],
         "Rotthing": [["Strength", 16], ["Speed", 7], ["Stealth",  4],
                      ["Cunning", 12]],
         "Froststep": [["Strength", 14], ["Speed", 14], ["Stealth", 17],
                       ["Cunning", 4]],
         "Wispyghoul": [["Strength", 17], ["Speed", 19], ["Stealth",  3],
                        ["Cunning", 2]]
         }

# Trialling 2 - printing all details from list
for card_name in cards:
    cards_list = cards[card_name]

    for card_info in cards_list:
        print(card_name, card_info[0], card_info[1])
