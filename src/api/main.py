from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

import os

app = FastAPI()

# Caminhos
MODEL_PATH = "models/model.pkl"
VECTORIZER_PATH = "models/vectorizer.pkl"

# Carregar modelo e vetorizador
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# Definir entrada da API
class NewsInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Fake News Detector API funcionando."}

@app.post("/predict")
def predict_news(input_data: NewsInput):
    text = input_data.text
    vect_text = vectorizer.transform([text])
    prediction = model.predict(vect_text)[0]

    result = "Real" if prediction == 1 else "Fake"
    return {"prediction": result}
