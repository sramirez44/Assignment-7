# import libraries
import dash
from dash import dcc, html, Input, Output

# initialize the app
app = dash.Dash(__name__)
# create app layout
app.layout = html.Div([
    html.H1("BMI Calculator"),
    # create input fields for height and weight
    html.Div([
        html.Label("Height:"),
        dcc.Input(id='height-input', type='number', placeholder='Enter height here', step=0.01),
        dcc.RadioItems(
            id='height-unit',
            options=[
                {'label': 'Meters (m)', 'value': 'm'},
                {'label': 'Feet (ft)', 'value': 'ft'}],
            value='m',
            inline=True)
    ], style={'padding': '10px'}),
    html.Div([
        html.Label("Weight:"),
        dcc.Input(id='weight-input', type='number', placeholder='Enter weight here', step=0.01),
        dcc.RadioItems(
            id='weight-unit',
            options=[
                {'label': 'Kilograms (kg)', 'value': 'kg'},
                {'label': 'Pounds (lb)', 'value': 'lb'}],
            value='kg',
            inline=True)
    ], style={'padding': '10px'}),

    html.Br(),
    html.H2(id='bmi-output', style={'color': 'blue'})
])

# app callback for calculating the bmi
@app.callback(
    Output('bmi-output', 'children'),
    [Input('height-input', 'value'),
     Input('height-unit', 'value'),
     Input('weight-input', 'value'),
     Input('weight-unit', 'value')])

def calculate_bmi(height, height_unit, weight, weight_unit):
    if height is None or weight is None:
        return "Please enter both height and weight."
    
    # convert height to m if in ft
    if height_unit == 'ft':
        height = height * 0.3048 
    
    # convert weight to kg if in lbs
    if weight_unit == 'lb':
        weight = weight * 0.453592  
    
    # calculate bmi
    bmi = weight / (height ** 2)
    
    return f"Your BMI is: {bmi:.2f}"

# run app
if __name__ == '__main__':
    app.run_server(debug=True)
