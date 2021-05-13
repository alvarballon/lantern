# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from shop_list import ingredients

# Importing all the things I need

fr = {"Rice", "Chicken", "Bell Peppers", "Green Onions", "Eggs", "Garlic", "Ginger"}  # noqa
bf = {"Tomatoes", "Cucumbers", "Fish", "Spinach", "Oil", "Lemons", "Cheese"}  # noqa
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

app = dash.Dash(external_stylesheets=[dbc.themes.SUPERHERO])

app.layout = html.Div(
    [
        dbc.Row(html.H3("What ingredients do you have?")),
        dbc.Row(
            [
                dbc.Col(html.Div("Protein"), width=2),
                dbc.Col(
                    dcc.Checklist(
                        id="prot_list",
                        options=[
                            {"label": "Chicken", "value": "Chicken"},
                            {"label": "Steaks", "value": "Steaks"},
                            {"label": "Fish", "value": "Fish"},
                            {"label": "Eggs", "value": "Eggs"},
                        ],
                        inputStyle={"margin-left": "20px"},
                    )
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.Div("Carbohydrates"), width=2),
                dbc.Col(
                    dcc.Checklist(
                        id="carb_list",
                        options=[
                            {"label": "Rice", "value": "Rice"},
                            {"label": "Lentils", "value": "Lentils"},
                            {"label": "Noodles", "value": "Noodles"},
                            {"label": "Beans", "value": "Beans"},
                        ],
                        inputStyle={"margin-left": "20px"},
                    )
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.Div("Veggies"), width=2),
                dbc.Col(
                    dcc.Checklist(
                        id="veg_list",
                        options=[
                            {"label": "Bell Peppers", "value": "Bell Peppers"},
                            {"label": "Green Onions", "value": "Green Onions"},
                            {"label": "Spinach", "value": "Spinach"},
                            {"label": "Onions", "value": "Onions"},
                            {"label": "Tomatoes", "value": "Tomatoes"},
                            {"label": "Lemons", "value": "Lemons"},
                            {"label": "Basil", "value": "Basil"},
                            {"label": "Cucumbers", "value": "Cucumbers"},
                        ],
                        inputStyle={"margin-left": "20px"},
                    )
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.Div("Spices"), width=2),
                dbc.Col(
                    dcc.Checklist(
                        id="spice_list",
                        options=[
                            {"label": "Garlic", "value": "Garlic"},
                            {"label": "Ginger", "value": "Ginger"},
                            {"label": "Chilli", "value": "Chilli"},
                            {"label": "Curry", "value": "Curry"},
                        ],
                        inputStyle={"margin-left": "20px"},
                    )
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.Div("Others"), width=2),
                dbc.Col(
                    dcc.Checklist(
                        id="other_list",
                        options=[
                            {"label": "Milk", "value": "Milk"},
                            {"label": "Butter", "value": "Butter"},
                            {"label": "Sugar", "value": "Sugar"},
                            {"label": "Cheese", "value": "Cheese"},
                            {"label": "Oil", "value": "Oil"},
                            {"label": "Chicken Stock", "value": "Chicken Stock"},  # noqa
                        ],
                        inputStyle={"margin-left": "20px"},
                    )
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.H3("What do you want to make?"), width=4),
                dbc.Col(
                    dcc.Dropdown(
                        id="dish",
                        options=[
                            {"label": "Fried Rice", "value": "fr"},
                            {"label": "Baked Fish", "value": "bf"},
                            {"label": "Butter Chicken", "value": "bc"},
                            {"label": "Lentils and Steak", "value": "ls"},
                            {"label": "Napolitano Noodles", "value": "nd"},
                            {"label": "Beef Chilli", "value": "ch"},
                        ],
                        value="fr",
                        style={"width": "50%"},
                    )
                ),
            ]
        ),
        dbc.Row(html.Div(id="my_shop_list", style={"margin-left": "20px"})),
    ]
)


@app.callback(
    Output("my_shop_list", "children"),
    [
        Input("prot_list", "value"),
        Input("carb_list", "value"),
        Input("veg_list", "value"),
        Input("spice_list", "value"),
        Input("other_list", "value"),
        Input("dish", "value"),
    ],
)
def print_ing(prot, carb, veg, spice, other, dish):
    if prot is None:
        prot = []
    if carb is None:
        carb = []
    if veg is None:
        veg = []
    if spice is None:
        spice = []
    if other is None:
        other = []
    ing = set(prot + carb + veg + spice + other)
    lst = ingredients.grocery_list(dish, ing)
    strlist = ", ".join(lst)
    return "You need to buy: " + strlist + "."


if __name__ == "__main__":
    app.run_server(debug=False,host='0.0.0.0', port=8050)
