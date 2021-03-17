import random, sys

# partipant1hp = 45
# partipant1ac = 2
# partipant1attack1 = 1
# partipant1damage = (1,6,2)


class participant():
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

    # def __repr__(self):
    #     return "Test()"

    def __str__(self):
        return self.name

participant1 = participant("Bob", 38, 14, 1, (1,4), 10, 10, 10, 10, 12, 5, 13)
participant2 = participant("Jerry", 14, 16, 1, (1,4), 10, 10, 10, 10, 12, 5, 13)
participant3 = participant("Micky Mouse", 56, 17, 1, (1,4), 10, 10, 10, 10, 12, 5, 13)
participant4 = participant("Alex", 76, 16, 1, (1,4), 10, 10, 10, 10, 12, 5, 13)
participant5 = participant("Stuart", 3, 13, 1, (1,4), 10, 10, 10, 10, 12, 5, 13)
participant6 = participant("Glastaff", 34, 16, 1, (1,4), 10, 10, 10, 10, 12, 5, 13)

participants = [participant1, participant2, participant3, participant4, participant5, participant6]
participant1.name = "Erik"
participant1.hp = participant1.hp - 10

for participant in participants:
    participant.initiative = random.randint(1, 20)

participants.sort(key=lambda x: x.initiative, reverse=True)

for participant in participants:
    print(f"Initiative = {participant.initiative}".ljust(17), f"{participant.name}".ljust(16), f"HP: {participant.hp}, ".ljust(10), f"AC: {participant.ac}".ljust(10))
