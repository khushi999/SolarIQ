import requests
import pandas as pd
import os

def fetch_nasa_power_data(lat, lon, start_date, end_date, output_path="data/raw/nasa_power.csv"):
    """
    Fetches solar and weather data from NASA POWER API for a given location and date range.

    Parameters:
        lat (float): Latitude of the location
        lon (float): Longitude of the location
        start_date (str): Start date in YYYYMMDD format
        end_date (str): End date in YYYYMMDD format
        output_path (str): Path to save the downloaded CSV
    """
    base_url = "https://power.larc.nasa.gov/api/temporal/daily/point"
    parameters = "ALLSKY_SFC_SW_DWN,T2M,RH2M"  # Solar irradiance, temp, humidity

    params = {
        "start": start_date,
        "end": end_date,
        "latitude": lat,
        "longitude": lon,
        "community": "RE",
        "parameters": parameters,
        "format": "JSON",
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()

        records = data["properties"]["parameter"]
        dates = list(data["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"].keys())

        df = pd.DataFrame({
            "date": dates,
            "solar_irradiance": [records["ALLSKY_SFC_SW_DWN"][d] for d in dates],
            "temperature": [records["T2M"][d] for d in dates],
            "humidity": [records["RH2M"][d] for d in dates]
        })

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"Saved NASA POWER data to {output_path}")
        return df

    except Exception as e:
        print("Error fetching data from NASA POWER API:")
        print(e)
        return None

# === Run this file directly to test ===
if __name__ == "__main__":
    from location_utils import get_user_location_from_ip

    lat, lon = get_user_location_from_ip()
    if lat and lon:
        fetch_nasa_power_data(
            lat=lat,
            lon=lon,
            start_date="20230101",
            end_date="20231231"
        )
