"""
Web app that helps first responders to classfify emergency messages in order to 
be able to distribute the work more efficiently in coordination with different 
organizations.
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] # !!! change 

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    children=[
        html.H1(
            children='Disaster Response Project',
            style={
                'textAlign': 'center'
            }
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)