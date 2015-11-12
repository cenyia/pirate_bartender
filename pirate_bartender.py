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
    for keyword, question in questions.items(): 
        response = input(question)
        if response == "yes":
            choices[keyword] = True
        else:
            choices[keyword] = False
                
                
        print(choices)
    return choices

import random

def drinkconstruct(choices):
    drink = []
    for keyword, response in choices.items():
        if response == True:
            drink.append(random.choice(ingredients[keyword]))
        else: 
            response == False
            
    return drink
    
def main():
    choices = drinkquestion()
    drink = drinkconstruct(choices)
    print("I'm going to make you a drink that's out of this world and it's made out of: ", drink)

if __name__ == "__main__":
    main()
    