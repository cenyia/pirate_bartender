questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}


ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def drinkquestion ():
    choices = {}
    for question in questions.values(): 
        print (question)
        input("""yes" or "no""") == 'yes' or 'y' 
        questions.update(choices)
            
    return choices

import random

def drinkconstruct (choices):
    drink = []
    for picks in choices.values:
        drink.append(random.choice(ingredients[picks]))
    return drink
    
def main():
    choices = drinkquestion()
    drink = drinkconstruct (choices)
    print("I'm going to make you a drink that's out of this world and it's made out of: ", drink)

if __name__ == "__main__":
    main()
    