"""
Data preprocessing pipeline:
- Loads the messages and categories datasets
- Merges the two datasets
- Cleans the data
- Stores it in a SQLite database
"""
import sys
import pandas as pd
import sqlalchemy as sa

def load_data(messages_filepath, categories_filepath):
    "reads messages and the corresponding categories from the specified files"
    # read csv files
    messages = pd.read_csv( "disaster_messages.csv" )
    categories = pd.read_csv( "disaster_categories.csv" )

    # merge both dataframes by message id
    return messages.merge( categories, on="id")


def clean_data( df ):
    "prepares data to be stored in a database"

    # drop duplicatesm by id because there exists more non-identical rows on the 
    # category df that correspond to the same message, so they do not drop using
    # drop_duplicates by all columns
    df.drop_duplicates(["id"], inplace=True)

    # create representation of categories to one-hot encoding
    categories = df["categories"].str.split(";", expand=True)  
    categories.columns = [ col[:-2] for col in categories.iloc[0] ]
    categories = categories.apply(lambda col: pd.to_numeric(col.str[-1]))

    # concat to original df and drop 'categories' column 
    df = pd.concat([ df, categories ], axis=1).drop("categories", axis=1)

    return df


def save_data(df, database_filename):
    "save df to a sqlite db"
    # create conexion to db file
    con = sa.create_engine( "sqlite:///{}".format(database_filename))
    
    # save data to db
    df.to_sql("classified_messages_training", con=con, index=False, if_exists="replace")


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Data saved to database')
    
    else:
        print("""Please provide the filepaths of the messages and categories 
              datasets as the first and second argument respectively, as 
              well as the filepath of the database to save the cleaned data 
              to as the third argument. Example: 
              python process_data.py 
              disaster_messages.csv disaster_categories.csv 
              DisasterResponse.db""")


if __name__ == '__main__':
    main()