"""Store card v2 - using lists"""

# Existing cards
cards = {"Stonelling": [["Strength", 7], ["Speed", 1], ["Stealth", 25],
                        ["Cunning", 15]],
         "Vexscream": [["Strength", 1], ["Speed", 6], ["Stealth", 21],
                       ["Cunning", 19]],
         "Dawnmirage": [["Strength", 5], ["Speed", 15], ["Stealth", 18],
                        ["Cunning", 22]],
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

# Trialling 2 - changing a stat (both stat name and value)
# from a specific card using lists
selected_card = "Websnake"  # Would be a user input
selected_stat = "Strength"  # Would be a user input

for item, stat in enumerate(cards[selected_card]):
    if stat[0] == selected_stat:
        new_stat_name = "test stat"
        cards[selected_card][item][0] = new_stat_name
        cards[selected_card][item][1] = 8  # Update the value

print(f"Card name: {selected_card}")
print(f"Card statistics: {cards[selected_card]}")
