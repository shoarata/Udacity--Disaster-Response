"""
Web app that helps first responders to classfify emergency messages in order to 
be able to distribute the work more efficiently in coordination with different 
organizations.
"""
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


