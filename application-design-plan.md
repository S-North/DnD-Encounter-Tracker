# Lets plan this application!
## Outline
As first, just what is necessary to track a single encounter e.g. add allies and enemies to a combat. Roll initiative, keep track of turns and rounds, roll for attack, keep track of damage/hp.
## Features
### Stage 1
* a terminal based application that can run on Windows, MacOS and Linux
* Create 1 or more encounters/combats
* Add enemies and allies to the combat
* roll initiative
* Keep track of rounds and turns
* Roll attacks
* Keep track of HP

### Stage 2
* Turn it into a GUI app (web/desktop)

### Stage 3
* character generation
* condition tracking
## Data
What data will we need to work with e.g. variables, reference data like monster stat blocks, etc.
## Logic
How will the application actually work?

    def roll_dice(times, sides, bonus):
      dice_results = []
      for roll in times:
        dice_results.append(random.randomint(1,sides))

      total = sum(dice_results) + bonus
      result = f"{times}d{sides} = {dice_results}" plus {bonus} = total"
      return result, total
