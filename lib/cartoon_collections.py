def roll_call_dwarves(dwarves):
    count = 0
    for dwarve in dwarves:
        count +=1
        print(f"{count}. {dwarve}")

def summon_captain_planet(planeteer):
    return([f"{plane.capitalize()}!"for plane in planeteer])

def long_planeteer_calls(words):
    for word in words:
        if len(word) > 4:
            return True
    return False

def find_the_cheese(ingredients):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for type in cheese_types:
        for ingredient in ingredients:
            if(type == ingredient):
                return ingredient
