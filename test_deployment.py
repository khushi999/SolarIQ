#!/usr/bin/env python3
"""
Simple test script to verify deployment environment
"""
import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    try:
        import streamlit as st
        print("✅ Streamlit imported successfully")
    except ImportError as e:
        print(f"❌ Streamlit import failed: {e}")
        return False
    
    try:
        import torch
        print("✅ PyTorch imported successfully")
    except ImportError as e:
        print(f"❌ PyTorch import failed: {e}")
        return False
    
    try:
        import pandas as pd
        print("✅ Pandas imported successfully")
    except ImportError as e:
        print(f"❌ Pandas import failed: {e}")
        return False
    
    try:
        import numpy as np
        print("✅ NumPy imported successfully")
    except ImportError as e:
        print(f"❌ NumPy import failed: {e}")
        return False
    
    return True

def test_backend_imports():
    """Test if backend modules can be imported"""
    try:
        from backend.data.fetch_nasa_power import fetch_nasa_power_data
        print("✅ NASA Power module imported successfully")
    except ImportError as e:
        print(f"❌ NASA Power module import failed: {e}")
        return False
    
    try:
        from backend.data.location_utils import get_user_location_from_browser
        print("✅ Location utils imported successfully")
    except ImportError as e:
        print(f"❌ Location utils import failed: {e}")
        return False
    
    try:
        from backend.model_training.model import SolarLSTM
        print("✅ SolarLSTM model imported successfully")
    except ImportError as e:
        print(f"❌ SolarLSTM model import failed: {e}")
        return False
    
    return True

def test_model_file():
    """Test if model file exists"""
    model_path = "models/solar_lstm.pth"
    if os.path.exists(model_path):
        print(f"✅ Model file found: {model_path}")
        return True
    else:
        print(f"❌ Model file not found: {model_path}")
        return False

if __name__ == "__main__":
    print("🔍 Testing SolarIQ deployment environment...")
    print("=" * 50)
    
    success = True
    
    # Test basic imports
    if not test_imports():
        success = False
    
    print()
    
    # Test backend imports
    if not test_backend_imports():
        success = False
    
    print()
    
    # Test model file
    if not test_model_file():
        success = False
    
    print("=" * 50)
    if success:
        print("🎉 All tests passed! Deployment should work.")
    else:
        print("❌ Some tests failed. Check the issues above.") 