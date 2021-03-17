import random  # we need this for all the random stuff we're going to do

class participant():  # create a class so we can create people objects with all the properties we need
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


participant1 = participant("Bob", 38, 14, 1, (1,4), 10, 10, 10, 10, 12, 5, 13)  # lets start creating some people :)
participant2 = participant("Jerry", 14, 16, 1, (1,4), 10, 10, 10, 10, 12, 5, 13)
participant3 = participant("Micky Mouse", 56, 17, 1, (1,4), 10, 10, 10, 10, 12, 5, 13)
participant4 = participant("Alex", 76, 16, 1, (1,4), 10, 10, 10, 10, 12, 5, 13)
participant5 = participant("Stuart", 3, 13, 1, (1,4), 10, 10, 10, 10, 12, 5, 13)
participant6 = participant("Glastaff", 34, 16, 1, (1,4), 10, 10, 10, 10, 12, 5, 13)

participants = [participant1, participant2, participant3, participant4, participant5, participant6]  # put all the people in a list

participant1.name = "Erik" # play around with changing the properties of some of the people
participant1.hp = participant1.hp - 10

participant7 = participant("Sildar", 40, 17, 1, (1,8), 0, 14, 15, 10, 12, 5, 13)  # create another person
participants.append(participant7)  # add them to the list

for participant in participants:  # loop over all the people in the list
    participant.initiative = random.randint(1, 20)  # roll initiative for each one

participants.sort(key=lambda x: x.initiative, reverse=True)  # sort the list into revese initiative order (using a highly confusing lambda function)

for participant in participants:  # loop over everything again to print out stuff
    print(f"Initiative = {participant.initiative}".ljust(17), f"{participant.name}".ljust(16), f"HP: {participant.hp}, ".ljust(10), f"AC: {participant.ac}".ljust(10))
