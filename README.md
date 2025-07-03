🧠 Fake News Detector — End-to-End MLOps Project
This is a fictional but fully functional project built to demonstrate a complete MLOps workflow, from data exploration and model training to real API serving and functional testing with pytest + requests.

📌 Objective
Classify whether a news article is Fake or Real using NLP and machine learning techniques.

🚀 Tech Stack
Python 3.10

scikit-learn, pandas, joblib

FastAPI — to serve the model via API

Docker — containerization

pytest + requests — real-world testing

(Optional and planned): MLflow, DVC, GitHub Actions

📁 Project Structure
bash
Copiar
Editar
mlops-fake-news-detector/
├── data/                  # Raw and processed data (optionally tracked with DVC)
├── models/                # Trained model and vectorizer
├── notebooks/             # EDA and modeling notebooks
├── src/
│   ├── api/               # FastAPI app (main.py)
│   └── train/             # Training script (train_model.py)
├── tests/                 # Functional tests with pytest + requests
├── Dockerfile             # Dockerized app
├── requirements.txt       # Pinned dependencies
├── README.md              # You are here
└── .github/workflows/     # (Optional) CI configuration
⚙️ How to Run the Project (Step-by-step)
1. Clone the repository
bash
Copiar
Editar
git clone https://github.com/viniciosfernandess/mlops-fake-news-detector.git
cd mlops-fake-news-detector
2. Create and activate the virtual environment (only once)
bash
Copiar
Editar
python -m venv venv
source venv/Scripts/activate  # On Windows
# or
source venv/bin/activate      # On Linux / macOS
3. Install dependencies
nginx
Copiar
Editar
pip install -r requirements.txt
4. Train the model
bash
Copiar
Editar
python src/train/train_model.py
5. Run the API
css
Copiar
Editar
uvicorn src.api.main:app --reload
🔍 API Testing (Swagger)
Open: http://localhost:8000/docs

Try POST /predict with a news sample like:

json
Copiar
Editar
{
  "text": "Breaking: New study reveals shocking truth about vaccines."
}
Expected response:

json
Copiar
Editar
{
  "prediction": "Fake"
}
🧪 Run Tests
Make sure the API is running locally, then in another terminal:

nginx
Copiar
Editar
pytest tests
Tests include:
API response

Model output logic

🐳 Docker (Optional)
Build the image
nginx
Copiar
Editar
docker build -t fake-news-api .
Run the container
arduino
Copiar
Editar
docker run -p 8000:8000 fake-news-api
📊 MLflow UI (Optional)
To visualize training metrics:

nginx
Copiar
Editar
mlflow ui
Access at: http://localhost:5000

💾 DVC (Optional)
To track data with DVC:

csharp
Copiar
Editar
dvc init
dvc add data/raw
dvc add data/processed
git commit -m "Track data with DVC"
📈 Future Improvements
 CI/CD with GitHub Actions

 API deployment with Railway or Render

 Integration with a real database (PostgreSQL, etc.)

 Minimal web frontend

 MLflow experiment tracking

 Full DVC integration

👤 Author
Created by Vinicios Fernandes as part of an MLOps portfolio project.

