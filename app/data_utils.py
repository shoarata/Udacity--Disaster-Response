import pandas as pd
import sqlalchemy as sa
import constants

con = sa.create_engine("sqlite:///{}".format(constants.db_file_path))

def load_categories():
    # load list with categories available on db
    return list(pd.read_sql("PRAGMA table_info(classified_messages_training)", con)["name"])[4:]

def load_table(table_name):
    "Loads data for training from the specified db and returns X, Y, categoy names"

    con = sa.create_engine("sqlite:///{}".format(constants.db_file_path))
    df = pd.read_sql_table(table_name, con=con)
    return df