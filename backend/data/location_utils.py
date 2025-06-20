import requests
from typing import Tuple, Optional

def get_user_location_from_ip() -> Tuple[str, float, float]:
    """
    Gets approximate location (latitude, longitude) using user's IP address.
    Uses ipinfo.io's free public API.
    """
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        
        loc = data.get("loc")
        if not loc:
            raise ValueError("Location data not found in response.")
        
        lat_str, lon_str = loc.split(",")
        lat, lon = float(lat_str), float(lon_str)
        
        city = data.get("city", "Unknown")
        region = data.get("region", "Unknown")
        
        print(f"Detected Location: {city}, {region}, ({lat}, {lon})")
        return f"{city}", lat, lon
    
    except Exception as e:
        print(f"Could not determine location from IP. Please enter manually. Error: {e}")
        return "Unknown", 28.6139, 77.2090

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
            headers = {'User-Agent': 'SolarIQ/1.0'}
            response = requests.get(
                f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json",
                headers=headers
            )
            response.raise_for_status()  # Raise an exception for bad status codes
            data = response.json()
            address = data.get("address", {})
            
            # Try to find a suitable location name from a list of keys
            location_keys = ["city", "town", "village", "suburb", "county", "state"]
            city = "Unknown"
            for key in location_keys:
                if key in address:
                    city = address[key]
                    break
            
            return city, lat, lon
        except requests.exceptions.RequestException as e:
            print(f"Error making request to Nominatim: {e}")
            return "Unknown", lat, lon
        except Exception as e:
            print(f"Error processing Nominatim response: {e}")
            return "Unknown", lat, lon
    
    # Fallback to IP-based location
    return get_user_location_from_ip()
