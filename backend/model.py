
import joblib
import numpy as np

# Load
model = joblib.load("sentiment_svm_model.joblib")
vectorizer = joblib.load("tfidf_vectorizer.joblib")

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

if __name__ == "__main__":
    print(predict("I am so Happy"))
    print(predict("This is the worst experience ever"))
