"""
Machine learning pipeline that:
- Loads data from the SQLite database
- Splits the dataset into training and test sets
- Builds a text processing and machine learning pipeline
- Trains and tunes a model using GridSearchCV
- Outputs results on the test set
- Exports the final model as a pickle file
"""
import sys
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, f1_score, accuracy_score, precision_score, recall_score
import pandas as pd
import sqlalchemy as sa
import pickle
from utils import tokenize

def load_data(database_filepath):
    "Loads data for training from the specified db and returns X, Y, categoy names"

    con = sa.create_engine("sqlite:///{}".format(database_filepath))
    df = pd.read_sql_table("classified_messages_training", con=con)
    # define x and y
    X = df.loc[:, "message"]
    Y = df.iloc[:, 4:]

    return X, Y, list(Y.columns)

def build_model():
    """Builds ML pipeline using gradient boosting classifier
    
        Returns: Classification model        
    """
    pipeline = Pipeline([
        ("tfidfvectorize", TfidfVectorizer(tokenizer=tokenize)),
        ("clf", MultiOutputClassifier(GradientBoostingClassifier()))
    ])
    parameters = {
        "clf__estimator__n_estimators": [100, 180]
    }

    model = GridSearchCV(pipeline, parameters, n_jobs=-1, scoring='recall_micro')
    
    return model

def evaluate_model(model, X_test, Y_test, category_names):
    "Prints evaluation metrics for the given model"
    # use model to predict on X_test
    Y_pred = model.predict(X_test)
    print("Overall Model Metrics:")
    print("----------------------")
    metrics = {
        "Accuracy": accuracy_score,
        "f1-score": f1_score,
        "Precision": precision_score,
        "Recall": recall_score
    }
    metrics_df = pd.DataFrame({
        metric: [
            metrics[metric](Y_test, Y_pred, average="macro") if metric != "Accuracy" else
            metrics[metric](Y_test, Y_pred) 
        ] for metric in metrics})
    print(metrics_df.to_markdown())
    print()
    for i, col in enumerate(category_names):
        print("Results on label: {}".format(col))
        print('-----------------------------')
        print(classification_report(Y_test[col], Y_pred[:, i]))


def save_model(model, model_filepath):
    "Saves the given model to a pickle file"
    with open(model_filepath, "wb") as file:
        pickle.dump(model, file)
    print("Model saved ...")


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        # train model from scratch
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)

        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument, the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db model.pkl')


if __name__ == '__main__':
    main()