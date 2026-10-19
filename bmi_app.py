# import libraries
import dash
from dash import dcc, html, Input, Output

# initialize the app
app = dash.Dash(__name__)
# create app layout
app.layout = html.Div([
    html.H1("BMI Calculator"),
    html.Div([
        html.Label("Height:"),
        dcc.Input(id='height-input', type='number', placeholder='Enter height here', step=0.01),
        dcc.RadioItems(
            id='height-unit',
            options=[
                {'label': 'Meters (m)', 'value': 'm'},
                {'label': 'Feet (ft)', 'value': 'ft'}]),
                value='m'
                inlineq=True)],
                style={'padding': '10px'}),
    html.Div([