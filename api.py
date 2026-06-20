from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load model
model = joblib.load("hotel_cancellation_model.pkl")


# Input schema
class BookingRequest(BaseModel):
    lead_time: int
    adr: float
    country: int


# Home route
@app.get("/")
def home():
    return {
        "message": "Hotel Booking Cancellation Prediction API"
    }


# Health check route
@app.get("/health")
def health():
    return {
        "status": "running"
    }


# Prediction route
@app.post("/predict")
def predict(data: BookingRequest):

    prediction = model.predict([
        [data.lead_time, data.adr, data.country]
    ])

    return {
        "prediction": int(prediction[0])
    }