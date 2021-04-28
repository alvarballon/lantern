# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
#Importing all the things I need
app = dash.Dash(external_stylesheets=[dbc.themes.SUPERHERO])

dict={}
#layout of the app, uses bootstrap to organize in rowns and colums
app.layout = html.Div(
	[
		dbc.Row(dbc.Col(html.H3("Choose your toppings"))),
		dbc.Row([dbc.Col(html.Div("Coconut"),width=2,style={"height":"100%"}), daq.ToggleSwitch(
        id='coconut_switch',
        value=False, color="green")],className='h-25'),
        dbc.Row([dbc.Col(html.Div("Chocolate"),width=2), daq.ToggleSwitch(
        id='chocolate_switch',
        value=False, color="green")]),
        dbc.Row([dbc.Col(html.Div("Mango"),width=2), daq.ToggleSwitch(
        id='mango_switch',
        value=False, color="green")]),
        dbc.Row([dbc.Col(html.Div("Oreos"),width=2), daq.ToggleSwitch(
        id='oreo_switch',
        value=False, color="green")]),
        dbc.Row([dbc.Col(dcc.Input(id='input_box_1', placeholder='Enter an item...', type='text',value=''), width=2),
        	     dbc.Col(html.Button('Show the Status', id='button_1',n_clicks=0),width=2),
        	     dbc.Col(html.Div(id='switch_status'))]),
        dbc.Row([dbc.Col(dcc.Input(id='input_box_2', placeholder='Enter an item...', type='text',value=''), width=2),
        	     dbc.Col(html.Button('Change the Status', id='button_2',n_clicks=0),width=2)
        	     ])

    ]
)
#First callback takes all toggle switches as inputs and returns ON or OFF as output if they match the text input
@app.callback(
	Output('switch_status', 'children'),
	Input('button_1','n_clicks'),
    State('coconut_switch', 'value'),
    State('chocolate_switch', 'value'),
    State('mango_switch', 'value'),
    State('oreo_switch', 'value'),
    State('input_box_1', 'value'),
    )
def update_status(n_clicks,coconut_switch,chocolate_switch,mango_switch,oreo_switch,input_box_1):
	dict={'coconut':coconut_switch, 'chocolate':chocolate_switch, 'mango':mango_switch, 'oreos':oreo_switch}
	return dict.get(input_box_1.lower(), 0)*'ON'+(1-dict.get(input_box_1.lower(),1))*'OFF'
#Here we have multiplied strings by zero or one instead of an if (faster), function returns empty string if input doesn't match categories
#Second callback toggles the switches, it has switches values as outputs and inputs. Changes switch if  it matches the input.
@app.callback(
	Output('coconut_switch', 'value'),
    Output('chocolate_switch', 'value'),
    Output('mango_switch', 'value'),
    Output('oreo_switch', 'value'),
    Input('button_2', 'n_clicks'),
    State('coconut_switch', 'value'),
    State('chocolate_switch', 'value'),
    State('mango_switch', 'value'),
    State('oreo_switch', 'value'),
    State('input_box_2', 'value'),
	)
def change_status(n_clicks,coconut_switch,chocolate_switch,mango_switch,oreo_switch,input_box_2):
	dict={'coconut':coconut_switch, 'chocolate':chocolate_switch, 'mango':mango_switch, 'oreos':oreo_switch}
	for elem in dict:
		dict[elem]=(input_box_2.lower()==elem) ^ dict[elem]
	return dict['coconut'], dict['chocolate'], dict['mango'], dict['oreos']

if __name__ == '__main__':
    app.run_server(debug=True)
