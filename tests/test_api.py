import requests
import time

def test_api_running():
    """Testa se a API está no ar"""
    response = requests.get("http://localhost:8000")
    assert response.status_code == 200
    assert response.json() == {"message": "Fake News Detector API funcionando."}

def test_api_prediction():
    """Testa a resposta de uma previsão"""
    payload = {"text": "The president has announced a new economic plan for recovery."}
    response = requests.post("http://localhost:8000/predict", json=payload)
    assert response.status_code == 200
    assert response.json()["prediction"] in ["Real", "Fake"]
