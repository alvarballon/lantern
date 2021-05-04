import unittest

from shop_list import ingredients

fr={"Rice", "Chicken", "Bell Peppers", "Green Onions", "Eggs", "Garlic", "Ginger"}
bf={"Tomatoes", "Cucumbers", "Fish", "Spinach", "Oil", "Lemons", "Cheese"}
bc={"Onions", "Curry", "Ginger","Garlic", "Milk", "Butter", "Chicken", "Rice", "Tomatoes", "Chilli", "Sugar"}
ls={"Onions", "Garlic", "Lentils", "Chicken Stock", "Steaks"}
nd={"Tomatoes", "Noodles", "Cheese", "Basil", "Sugar"}
ch={"Steak", "Onions", "Tomatoes", "Chilli", "Garlic", "Curry", "Beans", "Sugar"}

dic={"fr":fr,"bf":bf,"bc":bc, "ls":ls, "nd":nd, "ch":ch}

def test_fried_rice():
    lst={"Rice", "Chicken", "Bell Peppers"}
    assert {"Green Onions", "Eggs", "Garlic", "Ginger"}==ingredients.grocery_list("fr", lst)

def test_empty():
    lst={"Rice", "Chicken", "Bell Peppers", "Green Onions", "Eggs", "Garlic", "Ginger","Onions"}
    assert set()==ingredients.grocery_list("fr",lst)