from datetime import date
import random

# my_text = "Alex said \"Your're looking well\""
# print(my_text)
# my_text = 'my_text is great'
# print(my_text)
#
# apple = "apple"
# print(apple[0])
# print(apple[4])
#
# my_string = "jeff said \"you're never gonna guess what happened\""
# print(dir(str()))
#
# print(my_string.islower())
# print(my_string.title())
#
# print("Today is", date.today(), "\n")

player_roll = random.randint(1, 20)
player_modifier = 1
player_attack = player_roll + player_modifier
enemy_ac = 15
player = "Sherlock"
enemy = "Goblin 1"
damage = random.randint(1, 10)

if player_attack >= enemy_ac:
    print(player, "successfully hits", enemy, "for", damage, "points of damage", "\n")
else:
    print(player, "misses", enemy, "\n")
