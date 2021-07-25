from re import M
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import constants

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

_navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Predict", href="/")),
        dbc.NavItem(dbc.NavLink("Data", href="/data")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Linkedin", href=constants.linkedin_url),
                dbc.DropdownMenuItem("Twitter", href=constants.twitter_url),
                dbc.DropdownMenuItem(constants.email, header=True),
            ],
            nav=True,
            in_navbar=True,
            label="Contact me",
        ),
    ],
    brand=constants.project_title,
    brand_href=constants.project_url,
    color="dark",
    dark=True,
)

prediction_page = html.Div([
        _navbar,
        dbc.Container(
            [
                dbc.Row(dbc.Col(
                        dbc.Input(id="input_message", placeholder="Insert message to be classified...", type="text", value=""),
                        className="mt-5 mb-2 col-6 offset-3"
                )),
                dbc.Row(dbc.Col(
                        dbc.Button("Classify Message", id="classify_button", className="mb-3 offset-3", color="dark")
                ))
            ], fluid=True, className="bg-light"
        ),
        dbc.Container(
            [
                dbc.Row(dbc.Col(
                        dbc.ListGroup(
                            [], id="classification_results_list"
                        ),
                        className="mt-5 mb-2 col-6 offset-3"
                ))
            ], fluid=True
        )
    ]
)

not_found_page = html.Div([
    html.H3("404 Page not found :(", className="font-monospace")
], className="container text-center")