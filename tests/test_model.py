import joblib
import os

def test_model_and_vectorizer_loading():
    assert os.path.exists("models/model.pkl"), "Model file not found."
    assert os.path.exists("models/vectorizer.pkl"), "Vectorizer file not found."

    model = joblib.load("models/model.pkl")
    vectorizer = joblib.load("models/vectorizer.pkl")

    assert model is not None
    assert vectorizer is not None

def test_model_prediction():
    model = joblib.load("models/model.pkl")
    vectorizer = joblib.load("models/vectorizer.pkl")

    # Simulate input
    sample_text = ["NASA confirms water discovered on the moon."]
    vect = vectorizer.transform(sample_text)
    pred = model.predict(vect)

    assert pred[0] in [0, 1], "Prediction must be 0 (Fake) or 1 (Real)"
