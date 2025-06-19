import requests
from typing import Tuple, Optional

def get_user_location_from_browser(browser_location: dict) -> Tuple[str, float, float]:
    """
    Gets precise location from browser geolocation API
    
    Args:
        browser_location (dict): Dictionary containing lat and lon from browser
    
    Returns:
        Tuple[str, float, float]: (city, latitude, longitude)
    """
    if browser_location and "lat" in browser_location and "lon" in browser_location:
        lat, lon = browser_location["lat"], browser_location["lon"]
        
        # Reverse geocode to get city name
        try:
            response = requests.get(f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json")
            data = response.json()
            city = data.get("address", {}).get("city", "Unknown")
            if city == "Unknown":
                city = data.get("address", {}).get("town", "Unknown")
            return city, lat, lon
        except Exception as e:
            print(f"Error getting city name: {e}")
            return "Unknown", lat, lon
    
    # Fallback to IP-based location
    return get_user_location_from_ip()

def get_user_location_from_ip():
    """
    Gets approximate location (latitude, longitude) using user's IP address.
    Uses ipinfo.io's free public API.
    
    """
    
    try:
        response = requests.get ('https://ipinfo.io/json')
        data = response.json()
        
        loc = data.get("loc")
        if not loc:
            raise ValueError("Location data not found in response.")
        
        lat_str, lon_str = loc.split(",")
        lat, lon = float(lat_str), float(lon_str)
        
        
        city = data.get("city", "Unknown")
        region = data.get("region", "Unknown")
        
        print(f"Datected Location: {city}, {region}, ({lat}, {lon})")
        return f"{city}", lat, lon
    
    except Exception as e:
        print(f"Could not determine location from IP. Please enter manually.Error: {e}")
        return "Unknown", 28.6139, 77.2090
