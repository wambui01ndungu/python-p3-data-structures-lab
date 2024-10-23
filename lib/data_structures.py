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
       return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
       return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
       for food in spicy_foods:
          heat_level= food['heat_level']

          print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶'*heat_level}")    


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
       for food in spicy_foods:
          if food ['cuisine'] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
       for food in spicy_foods:
          if food['heat_level'] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶'* food['heat_level'] }")

           
    
def get_average_heat_level(spicy_foods):
       total_heat = sum(food['heat_level'] for food in spicy_foods)
       return total_heat/len(spicy_foods)


def create_spicy_food(spicy_foods, new_food):
       spicy_foods.append(new_food)
       return spicy_foods
       updated_foods = create_spicy_food( SPICY_FOODS, new_food)
       print(updated_foods)