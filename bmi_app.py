# import libraries
import dash
from dash import dcc, html, Input, Output

# initialize the app
app = dash.Dash(__name__)
# create app layout
app.layout = html.Div([
    html.H1("BMI Calculator"),
    html.Div([
        html.Label("Height (m):"),
        dcc.Input(id='heigh-input' type='number',placeholder='Enter height in meters', step=0.01), 