from fastapi import FastAPI
from pathlib import Path
import pickle

app = FastAPI(
    title="House Price Prediction API",
    description="An API for predicting house prices",
    version="1.0.0",
)

MODEL_PATH = Path(__file__).resolve().parent / "models" / "bengaluru_house_price_linear_regression_model.pickle"

try:
    with open(MODEL_PATH, "rb") as file:
        model_package = pickle.load(file)

        model = model_package["model"]
        feature_columns = model_package["feature_columns"]

except FileNotFoundError:
    raise RuntimeError(f"The pickel file was not found at the specified path: {MODEL_PATH}") 

except KeyError:
    raise RuntimeError("The pickel file does not contain the expected keys: 'model' and 'feature_columns'") 

except Exception as e:
    raise RuntimeError (f"An unexpected error occurred: {e}")



@app.get("/")
def read_root():
    return {"message":"this is the root of house price prediction API"}

@app.get("/health")
def read_health():
    return {"status":"ok"}