import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
import mlflow
import mlflow.sklearn

# Configurar MLflow
mlflow.set_experiment("fake-news-detector")

with mlflow.start_run():
    # 1. Carregar dados
    df = pd.read_csv("data/processed/clean_fake_news.csv")
    X = df["text"]
    y = df["label"]

    # 2. Pré-processamento
    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    X_vect = vectorizer.fit_transform(X)

    # 3. Split
    X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)

    # 4. Modelo
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # 5. Métricas
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # 6. Log com MLflow
    mlflow.log_param("model_type", "LogisticRegression")
    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("f1_score", f1)
    mlflow.sklearn.log_model(model, "model")
    mlflow.log_artifact("data/processed/clean_fake_news.csv")

    print(f"Accuracy: {acc:.4f}")
    print(f"F1 Score: {f1:.4f}")

# 7. Salvar modelo e vetorizador localmente
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")
