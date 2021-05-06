fr = {"Rice", "Chicken", "Bell Peppers", "Green Onions", "Eggs", "Garlic", "Ginger"}  # noqa
bf = {"Tomatoes", "Cucumbers", "Fish", "Spinach", "Oil", "Lemons", "Cheese"}
bc = {
    "Onions",
    "Curry",
    "Ginger",
    "Garlic",
    "Milk",
    "Butter",
    "Chicken",
    "Rice",
    "Tomatoes",
    "Chilli",
    "Sugar",
}
ls = {"Onions", "Garlic", "Lentils", "Chicken Stock", "Steaks"}
nd = {"Tomatoes", "Noodles", "Cheese", "Basil", "Sugar"}
ch = {"Steak", "Onions", "Tomatoes", "Chilli", "Garlic", "Curry", "Beans", "Sugar"}  # noqa

dic = {"fr": fr, "bf": bf, "bc": bc, "ls": ls, "nd": nd, "ch": ch}


def grocery_list(dish, ingredients):
    missing = dic[dish] - ingredients
    return missing
