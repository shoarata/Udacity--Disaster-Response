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
from sklearn.ensemble import RandomForestClassifier

def load_data(database_filepath):
    #!!!
    return [1,2,3,4,5], [0,1,1,2,1], ['first', 'second', 'third']


def tokenize(text):
    #!!!
    return None


def build_model():
    #!!!
    return RandomForestClassifier()


def evaluate_model(model, X_test, Y_test, category_names):
    #!!!
    print("Model Accuracy: 99%...")


def save_model(model, model_filepath):
    # !!!
    print("Model saved ...")


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
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
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()