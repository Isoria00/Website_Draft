# dateideas.py

import random

# List of date ideas
DATE_IDEAS_OUTDOOR = [
    "outdoor"
]

DATE_IDEAS_INDOOR = [
    "indoor"
]

DATE_IDEAS_ROMANTIC = [
    "romantic"
]

DATE_IDEAS_FOODANDDRINK = [
    "food"
]

DATE_IDEAS_FUN = [
    "fun"
]

DATE_IDEAS_CULTURAL_EDUCATIONAL = [
    "edu"
]

list_of_categories = [DATE_IDEAS_OUTDOOR,
                      DATE_IDEAS_INDOOR,
                      DATE_IDEAS_ROMANTIC,
                       DATE_IDEAS_FOODANDDRINK,
                      DATE_IDEAS_FUN,
                      DATE_IDEAS_CULTURAL_EDUCATIONAL
                      ]

def get_random_idea(index):
    return random.choice(list_of_categories[index])
