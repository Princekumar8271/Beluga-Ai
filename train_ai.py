import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

class AIModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = MultinomialNB()
        self.model_path = os.path.join(os.path.dirname(__file__), 'beluga_ai_model.pkl')
        
    def train(self, X, y):
        """
        Train the AI model with given data
        Args:
            X: List of text samples
            y: List of corresponding labels
        """
        X_vec = self.vectorizer.fit_transform(X)
        self.model.fit(X_vec, y)
        
    def predict(self, text):
        """
        Make prediction on new text
        Args:
            text: Input text to classify
        Returns:
            Predicted label
        """
        if not hasattr(self.model, 'classes_'):
            raise Exception("Model not trained yet")
            
        vec = self.vectorizer.transform([text])
        return self.model.predict(vec)[0]
    
    def save_model(self):
        """Save the trained model to disk"""
        with open(self.model_path, 'wb') as f:
            pickle.dump({
                'vectorizer': self.vectorizer,
                'model': self.model
            }, f)
    
    def load_model(self):
        """Load the trained model from disk"""
        if not os.path.exists(self.model_path):
            return False
            
        with open(self.model_path, 'rb') as f:
            data = pickle.load(f)
            self.vectorizer = data['vectorizer']
            self.model = data['model']
        return True

# Example training data (English and Hindi)
TRAINING_DATA = {
    'texts': [
        # English commands
        'open youtube',
        'play music',
        'what time is it',
        'search wikipedia for python',
        'stop',
        # Hindi commands
        'यूट्यूब खोलो',
        'संगीत चलाओ',
        'क्या समय हुआ है',
        'विकिपीडिया पर पायथन खोजें',
        'रुको'
    ],
    'labels': [
        # English labels
        'open_youtube',
        'play_music',
        'get_time',
        'wikipedia_search',
        'stop_program',
        # Hindi labels (same as English since commands do same things)
        'open_youtube',
        'play_music',
        'get_time',
        'wikipedia_search',
        'stop_program'
    ]
}

if __name__ == '__main__':
    # Initialize and train the model
    ai_model = AIModel()
    ai_model.train(TRAINING_DATA['texts'], TRAINING_DATA['labels'])
    ai_model.save_model()
    
    # Test prediction
    test_query = "play some songs"
    print(f"Prediction for '{test_query}':", ai_model.predict(test_query))