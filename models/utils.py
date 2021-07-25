"""
Utils module created in order to be usable by the model, this due to pickle serializing references to custom functions
https://stackoverflow.com/questions/27732354/unable-to-load-files-using-pickle-and-multiple-modules
"""

import nltk
from nltk.corpus import stopwords
import re

nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger', "stopwords"])
stop_words = set(stopwords.words('english'))

def tokenize(text, remove_stop_words=True):
    """Tokenize text applying:
        Case normalization
        Lemmatization
        Removal of stop words (opcional)
        Replacement of urls with placeholder
        
        Returns: list of tokens-words
    """
    url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    # replace urls in text with placeholder
    text = re.sub(url_regex, "urlplaceholder", text)
    
    # tokenize words
    words = nltk.word_tokenize(text)

    # case normalization and remove punctuation
    words = [ word.lower().strip() for word in words if word.isalnum() ]

    if remove_stop_words:
        # removing stopwords
        words= [ word for word in words if word not in stop_words ]

    # Apply lemmatization
    lemmatizer = nltk.WordNetLemmatizer()
    words = [ lemmatizer.lemmatize(word) for word in words ]
    
    return words