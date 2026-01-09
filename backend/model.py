
import joblib
import numpy as np
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "sentiment_svm_model.joblib")
VECTORIZER_PATH = os.path.join(BASE_DIR, "tfidf_vectorizer.joblib")
# Load
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def predict(text: str) -> dict:
    # transform the text
    X = vectorizer.transform([text])
    sentiment = model.predict(X)[0]
    scores = model.decision_function(X)
    confidence = float(np.max(np.abs(scores))) # takes the absolute value (turns it positive)
    if sentiment == 0:
        sentiment = "Negative"
    else:
        sentiment = "Positive"
    return sentiment, confidence


