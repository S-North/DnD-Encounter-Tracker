import random  # we need this for all the random stuff we're going to do

class person():  # create a class so we can create people objects with all the properties we need
    def __init__(self, name, str, dex, con, wis, int, cha, hp, ac, attack, damage, cr=None, initiative=None):
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
        self.cr = cr

    def __str__(self):
        return self.name

def ability_modifier(ability_score):
    if ability_score >= 10:
        return int((ability_score - 10) / 2)
    else:
        return - int(abs((ability_score -11) / 2))

person1 = person("Goblin 1",    8, 10, 10, 10, 8, 8,        7, 15,  0, (1,6), 0.5)  # lets start creating some people :)
person2 = person("Goblin 2",    8, 10, 10, 10, 8, 8,        7, 15,  0, (1,6), 0.5)
person3 = person("Sherlock",    8, 17, 14, 16, 8, 9,        20, 13, 0, (1,10))
person4 = person("Polydeuces",  13, 16, 14, 8, 15, 8,       32, 15, 1, (1,8))
person5 = person("Stealth",     10, 16, 14, 13, 10, 14,     26, 15, 1, (1,6))
person6 = person("Goblin 3",    8, 10, 10, 10, 8, 8,        7, 15, 0, (1,6), 0.5)
person7 = person("Goblin 4",    8, 10, 10, 10, 8, 8,        7, 15, 0, (1,6), 0.5)

persons = [person1, person2, person3, person4, person5, person6, person7]  # put all the people in a list

person5.name = "Alan" # play around with changing the properties of some of the people
person4.hp = person4.hp - 10
person8 = person("Raskas",      16, 14, 16, 10, 10, 11,    31, 19, 1, (1,10))  # create another person
persons.append(person8)  # add them to the list

for person in persons:  # loop over all the people in the list
    init_roll = random.randint(1, 20)  # roll initiative for each one
    modifier = ability_modifier(person.dex)
    person.initiative = init_roll + modifier
    print (f"{person.name:12} rolled", f"{init_roll:3} + {modifier:>2} = {person.initiative}")

persons.sort(key=lambda x: x.initiative, reverse=True)  # sort the list into revese initiative order (using a highly confusing lambda function)

for person in persons:  # loop over everything again to print out stuff
    print(f"Initiative = {person.initiative}".ljust(17), f"{person.name}".ljust(16), f"HP: {person.hp}, ".ljust(10), f"AC: {person.ac}".ljust(10), f"Challenge = {person.cr}")
