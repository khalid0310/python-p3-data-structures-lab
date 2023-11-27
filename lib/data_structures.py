spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    """Return a list of strings with the names of each spicy food."""
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    """Return a list of dictionaries where the heat level of the food is greater than 5."""
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    """Output to the terminal each spicy food in a formatted way."""
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Return a single dictionary for the spicy food whose cuisine matches the input."""
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # Return None if no matching cuisine is found

def print_spiciest_foods(spicy_foods):
    """Output to the terminal ONLY the spicy foods that have a heat level greater than 5."""
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)
    
def get_average_heat_level(spicy_foods):
    """Return an integer representing the average heat level of all the spicy foods."""
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    num_foods = len(spicy_foods)
    if num_foods > 0:
        return total_heat_level // num_foods
    else:
        return 0  # Return 0 if there are no spicy foods

def create_spicy_food(spicy_foods, spicy_food):
    """Add a new spicy food to the list of spicy foods."""
    spicy_foods.append(spicy_food)
    return spicy_foods