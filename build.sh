#!/usr/bin/env bash
# Build script for Render deployment

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Starting Streamlit app..."
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 