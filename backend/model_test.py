import pytest
from backend import model

#basic test to see if function is callable
def test_sentiment():
    positive_text = "This is the best day of my life"
    positive_text2 = "absolutely amazing"
    negative_text = "It was horrible"
    negative_text2 = "this is the worst day of my life"

    positive_text,_ = model.predict(positive_text)
    positive_text2,_ = model.predict(positive_text2)
    negative_text,_ = model.predict(negative_text)
    negative_text2,_ = model.predict(negative_text2)

    assert positive_text == 'Positive'
    assert negative_text == 'Negative'
    assert positive_text2 == 'Positive'
    assert negative_text2 == 'Negative'
