import random

appearance = []
personality = ["Aloof", "Apathetic", "Argumentative", "Sympathetic", "Aimless", "Aggressive", "Tolerant", "Trusting", "Undogmatic", "Youthful", "Vivacious", "Meddlesome", "Melancholic", "Messy", "Miserable", "Moody", "Neurotic", "Nihilistic", "Obsessive", "Obvious", "Opinionated", "Accessible", "Optimistic", "Pessimistic", "Methodical", "Cheerful", "Dignified", "Dramatic", "Earnest", "Elegant", "Eloquent", "Enthusiastic", "Firm", "Forceful", "Forthright", "Fun-loving", "Generous", "Gentle", "Hardworking", "Honest", "Humble", "Honorable", "Idealistic", "Imaginative", "Kind", "Leisurely", "Logical", "Meticulous", "Observant", "Perfectionist", "Playful", "Practical", "Protective", "Realistic", "Relaxed", "Resourceful", "Responsible", "Scholarly", "Selfless", "Self-critical", "Sentimental", "Serious", "Sociable", "Sophisticated", "Spontaneous", "Stoic", "Suave", "Sympathetic", "Tolerant", "Trusting", "Undogmatic", "Urbane", "Vivacious", "Witty", "Youthful", "Abrupt", "Aggressive", "Aimless", "Aloof", "Apathetic", "Argumentative", "Arrogant", "Bewildered", "Blunt", "Boisterous", "Calculating", "Callous" "Cantankerous", "Careless", "Childish", "Clumsy", "Coarse", "Cold", "Complaining", "Compulsive", "Confused", "Cowardly", "Critical", "Cynical", "Decadent", "Deceitful", "Demanding", "Disconcerting", "Disorganized", "Dogmatic", "Domineering", "Dull", "Egocentric", "Extravagant", "Fatalistic", "Fawning", "Fearful", "Flamboyant", "Foolish", "Forgetful", "Frightening", "Frivolous", "Gloomy", "Greedy", "Gullible", "Hedonistic", "Hesitant", "Ignorant", "Impatient", "Inconsiderate", "Indecisive", "Insincere", "Insulting", "Intolerant", "Irrational", "Lazy", "Urban", "Witty", "Abrupt", "Paranoid", "Pedantic", "Petty", "Pompous", "Pretentious", "Puritanical", "Rigid", "Secretive", "Selfish", "Shortsighted", "Slow", "Stupid", "Superstitious", "Suspicious", "Timid", "Unfriendly", "Unhealthy", "Unrealistic", "Vague", "Vindictive"]
quirk = []
celebrity = ["Elijah Wood", "Ben Affleck", "Javier Bardem", "Albert Finney", "Christian Bale", "Brad Pitt", "Harrison Ford", "Mark Ruffalo", "Demi Moore", "Madonna", "Victoria Beckham", "David Beckham", "Hulk Hogan", "Dwaine 'The Rock' Johnson"]

def roll_npc(quirks):
    print(random.choice(celebrity))
    for i in range(quirks):
        print (random.choice(personality))

while True:
    quirks = int(input("How many quirks do you want? "))
    roll_npc(quirks)
