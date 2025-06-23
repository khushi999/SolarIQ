from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import sys
import os
import torch
import pandas as pd
from datetime import datetime, timedelta
from typing import Optional

# Add the backend modules to path
sys.path.append(os.path.abspath('.'))

from backend.data.fetch_nasa_power import fetch_nasa_power_data
from backend.data.location_utils import get_user_location_from_browser
from backend.model_training.model import SolarLSTM
from backend.model_training.config import INPUT_SIZE, HIDDEN_SIZE, NUM_LAYERS

app = FastAPI(title="SolarIQ", description="ML-Powered Solar Forecasting App")

# --- CORS Middleware ---
# This allows your frontend on Vercel to communicate with this backend on Render.
origins = [
    "https://solariq.onrender.com", # The frontend itself
    "https://*.vercel.app",        # Allow any Vercel deployment
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods
    allow_headers=["*"], # Allows all headers
)

# Mount static files (no longer needed for the primary frontend)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates (no longer needed for the primary frontend)
# templates = Jinja2Templates(directory="templates")

# Model path - adjust for Vercel deployment
MODEL_SAVE_PATH = os.path.join(os.path.dirname(__file__), "models", "solar_lstm.pth")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return {"message": "SolarIQ Backend is running. Frontend is hosted separately."}

@app.post("/predict")
async def predict_solar_irradiance(
    lat: float = Form(...),
    lon: float = Form(...),
    system_size: float = Form(3.0),
    efficiency: float = Form(80.0),
    electricity_rate: float = Form(6.0)
):
    try:
        # Fetch weather data
        end_date = datetime.today().strftime("%Y%m%d")
        start_date = (datetime.today() - timedelta(days=365)).strftime("%Y%m%d")
        df = fetch_nasa_power_data(lat, lon, start_date, end_date)
        
        if df is None or df.empty:
            return {"error": "Failed to fetch weather data"}
        
        # Clean data
        df = df[
            (df['solar_irradiance'] != -999) &
            (df['temperature'] != -999) &
            (df['humidity'] != -999)
        ]
        
        if df.empty:
            return {"error": "No valid data points found"}
        
        # Get last 7 days for prediction
        last_7_days = df.tail(7)[['solar_irradiance', 'temperature', 'humidity']].values
        
        if last_7_days.shape != (7, 3):
            return {"error": "Insufficient data for prediction"}
        
        # Load model and predict
        sequence = torch.tensor(last_7_days, dtype=torch.float32).unsqueeze(0)
        model = SolarLSTM(input_size=INPUT_SIZE, hidden_size=HIDDEN_SIZE, num_layers=NUM_LAYERS)
        
        # Load model weights with error handling
        try:
            model.load_state_dict(torch.load(MODEL_SAVE_PATH, map_location=torch.device('cpu')))
        except FileNotFoundError:
            return {"error": "Model file not found. Please ensure the model is properly deployed."}
        except Exception as e:
            return {"error": f"Error loading model: {str(e)}"}
        
        model.eval()
        
        with torch.no_grad():
            prediction = model(sequence).item()
        
        # Calculate savings
        daily_energy_kwh = prediction * system_size * (efficiency / 100)
        estimated_savings = daily_energy_kwh * electricity_rate
        
        return {
            "prediction": round(prediction, 3),
            "daily_energy": round(daily_energy_kwh, 2),
            "daily_savings": round(estimated_savings, 2),
            "historical_data": df.tail(30)['solar_irradiance'].tolist()
        }
        
    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "SolarIQ API is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 