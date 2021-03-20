import random, pprint
pp = pprint.PrettyPrinter(indent=4)  # this just prints out data in a nicely formatted way


def ability_modifier(ability_score):  # pass this function an ability score and it will return the correct modifier
    if ability_score >= 10:
        return int((ability_score - 10) / 2)
    else:
        # dict = {"1": -5, "2": -4, "3": -4, "4": -3, "5": -3, "6": -2, "7": -2, "8": -1, "9": -1}  # had to fudge this as I couldn't find a good calculation
        # return dict[str(ability_score)]
        return - int(abs((ability_score -11) / 2))  #  haha, found a calculation for this after all :) -11 turns [1:9] into [-10:-2], abs() converts to positive numbers [10:2], divide by 2, int() rounds down, minus sign (-) turns the positive numbers back into negative ones


person1 = {"name": "Polydeuces", "class": "Ranger", "level": 3, "str": 13, "dex": 16, "con": 14, "int": 8, "wis": 15, "cha": 8, "hp": 32, "ac": 15, "initiative": None}
person2 = {"name": "Sherlock", "str": 8, "dex": 17, "con": 14, "int": 16, "wis": 8, "cha": 9, "hp": 20, "ac": 13, "initiative": None}
person3 = {"name": "Alan", "str": 10, "dex": 16, "con": 14, "int": 13, "wis": 10, "cha": 14, "hp": 26, "ac": 15, "initiative": None}
person4 = {"name": "Goblin 1", "str": 8, "dex": 8, "con": 10, "int": 10, "wis": 8, "cha": 8, "hp": 7, "ac": 15, "initiative": None}
person5 = {"name": "Goblin 2", "str": 8, "dex": 6, "con": 10, "int": 10, "wis": 8, "cha": 8, "hp": 7, "ac": 15, "initiative": None}
person6 = {"name": "Goblin 3", "str": 8, "dex": 1, "con": 10, "int": 10, "wis": 8, "cha": 8, "hp": 7, "ac": 15, "initiative": None}

combat = [person1, person2, person3, person4, person5, person6]

for person in combat:
    initiative_roll = random.randint(1,20)
    modifier = ability_modifier(person["dex"])
    person["initiative"] = initiative_roll + modifier
    print (f"{person['name']:10} rolled", f"{initiative_roll:3} + {modifier:>2} = {person['initiative']}")

combat.sort(key=lambda x: x["initiative"], reverse=True)  # sort the list using a list comprehension. don't worry if this looks like gibberish, i'll explain

pp.pprint(combat)
