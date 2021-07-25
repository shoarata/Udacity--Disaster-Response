"""
File that represents the main layout of the app, had to make a separate file
in order to be able to separate callbacks into another file, got the idea
from https://community.plotly.com/t/dash-callback-in-a-separate-file/14122/22
"""
from os import path
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import layouts
import callbacks
from app import app
import dash

app.layout = html.Div([
    dcc.Location(id="url"),
    html.Div(id="content")
])

@app.callback(
    dash.dependencies.Output("content", "children"),
    dash.dependencies.Input("url", "pathname")
)
def change_page(pathname):
    if pathname in ["/predict", "/"]:
        return layouts.prediction_page
    elif pathname =="/data":
        return layouts.data_page
    else:
        return layouts.not_found_page

if __name__ == '__main__':
    app.run_server(debug=False)