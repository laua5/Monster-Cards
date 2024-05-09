"""Store card v2 - using lists"""

cards = [["Stonelling", 7, 1, 25, 15],["Vexscream", 1, 6, 21, 19],
         ["Dawnmirage", 5, 15, 18, 22], ["Blazegolem", 15, 20, 23, 6],
         ["Websnake", 7,15, 10, 5], ["Moldvine",21, 18, 14, 5],
         ["Vortexwing", 19, 13, 19, 2], ["Rotthing", 16, 7, 4, 12],
         ["Froststep", 14, 14, 17, 4], ["Wispyghoul", 17, 19, 3, 2]]

for card in cards:
    print(f"\nCard name:{card[0]}")
    print(f"Strength:{card[1]}")
    print(f"Speed:{card[2]}")
    print(f"Stealth:{card[3]}")
    print(f"Cunning:{card[4]}")
