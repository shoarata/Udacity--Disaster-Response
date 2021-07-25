from app import app
import dash
import pickle
import constants
import data_utils
import dash_bootstrap_components as dbc

# load list with categories available on db
categories = data_utils.load_categories()

# load model
with open(constants.model_file_path,"rb") as file:
    model = pickle.load(file)


@app.callback(
    dash.dependencies.Output("classification_results_list", "children"),
    dash.dependencies.Input("classify_button", "n_clicks"),
    dash.dependencies.State("input_message", "value")
)
def classify_message(n_clicks, message):
   "Classfigy message and output classfication results"
   if n_clicks:
       if message == "":
           return [dbc.ListGroupItem("Please enter a valir message", color="danger")]
       y_pred = model.predict([message])[0]
       return [dbc.ListGroupItem(cat, color=("primary" if col == 1 else "")) for cat, col in zip(categories, y_pred)]