import random  # we need this for all the random stuff we're going to do

class person():  # create a class so we can create people objects with all the properties we need
    def __init__(self, name, hp, ac, attack, damage, initiative, str, dex, con, wis, int, cha):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.attack = attack
        self.damage = damage
        self.initiative = initiative
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha

    def __str__(self):
        return self.name


person1 = person("Goblin 1", 38, 14, 1, (1,4), 10, 10, 10, 10, 12, 5, 13)  # lets start creating some people :)
person2 = person("Goblin 2", 14, 16, 1, (1,4), 10, 10, 10, 10, 12, 5, 13)
person3 = person("Sherlock", 56, 17, 1, (1,4), 10, 10, 10, 10, 12, 5, 13)
person4 = person("Polydeuces", 76, 16, 1, (1,4), 10, 14, 10, 10, 12, 5, 13)
person5 = person("Alan", 3, 13, 1, (1,4), 10, 10, 10, 10, 12, 5, 13)
person6 = person("Raskas", 34, 16, 1, (1,4), 10, 10, 10, 10, 12, 5, 13)
person7 = person("Goblin 3", 14, 16, 1, (1,4), 10, 10, 10, 10, 12, 5, 13)
person8 = person("Goblin 4", 14, 16, 1, (1,4), 10, 10, 10, 10, 12, 5, 13)

persons = [person1, person2, person3, person4, person5, person6, person7, person8]  # put all the people in a list

person1.name = "Erik" # play around with changing the properties of some of the people
person1.hp = person1.hp - 10

def calc_modifier(ability_score):
    if ability_score >= 10:
        return int((ability_score - 10) / 2)
    else:
        dict = {"1": -5, "2": -4, "3": -4, "4": -3, "5": -3, "6": -2, "7": -2, "8": -1, "9": -1}  # had to fudge this as I couldn't find a good calculation
        return dict[str(ability_score)]


for ability in range(1,31):
    print(f"abilty {ability} gets you modifier {calc_modifier(ability)}")

person9 = person("Sildar", 40, 17, 1, (1,8), 0, 14, 15, 10, 12, 5, 13)  # create another person
persons.append(person7)  # add them to the list

for person in persons:  # loop over all the people in the list
    person.initiative = random.randint(1, 20)  # roll initiative for each one

persons.sort(key=lambda x: x.initiative, reverse=True)  # sort the list into revese initiative order (using a highly confusing lambda function)

for person in persons:  # loop over everything again to print out stuff
    print(f"Initiative = {person.initiative}".ljust(17), f"{person.name}".ljust(16), f"HP: {person.hp}, ".ljust(10), f"AC: {person.ac}".ljust(10))
