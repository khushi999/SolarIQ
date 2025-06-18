import requests

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
