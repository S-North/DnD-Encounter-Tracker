# Lets plan this application!
## Outline
What's it going to do?
## Features
We'll do it in stage
### Stage 1
* Feature 1
* Feature 2
* Feature 3
* Feature 4
  * Sub feature 1
  * Sub feature 2
  * Sub feature 3
  * Sub feature 4
## Data
What data will we need to work with e.g. variables, reference data like monster stat blocks, etc.
## Logic
How will the application actually work?

'''python
def roll_dice(times, sides, bonus):
  dice_results = []
  for roll in times:
    dice_results.append(random.randomint(1,sides))

  total = sum(dice_results) + bonus
  result = f"{times}d{sides} = {dice_results}" plus {bonus} = total"
  return result, total
'''

    def roll_dice(times, sides, bonus):
      dice_results = []
      for roll in times:
        dice_results.append(random.randomint(1,sides))

      total = sum(dice_results) + bonus
      result = f"{times}d{sides} = {dice_results}" plus {bonus} = total"
      return result, total
