import os
import requests
from tqdm import tqdm

url_base = "https://data.pmel.noaa.gov/pmel/erddap/tabledap/AIS2024_AIS.csv"
folder_path = r'C:\Users\Vikas\Documents\ProMain1\Data'

months = [
    ("2024", "01"), ("2024", "02"), ("2024", "03"), ("2024", "04"),
    ("2024", "05"), ("2024", "06"), ("2024", "07"), ("2024", "08"),
    ("2024", "09"), ("2024", "10"), ("2024", "11"), ("2024", "12"),
    ("2025", "01"), ("2025", "02"), ("2025", "03"), ("2025", "04"),
    ("2025", "05"), ("2025", "06"), ("2025", "07"), ("2025", "08"),
    ("2025", "09"), ("2025", "10"), ("2025", "11"), ("2025", "12")
]

days_in_month = {
    ("2024", "01"): "31", ("2024", "02"): "29", ("2024", "03"): "31", ("2024", "04"): "30",
    ("2024", "05"): "31", ("2024", "06"): "30", ("2024", "07"): "31", ("2024", "08"): "31",
    ("2024", "09"): "30", ("2024", "10"): "31", ("2024", "11"): "30", ("2024", "12"): "31",
    ("2025", "01"): "31", ("2025", "02"): "28", ("2025", "03"): "31", ("2025", "04"): "30",
    ("2025", "05"): "31", ("2025", "06"): "30", ("2025", "07"): "31", ("2025", "08"): "31",
    ("2025", "09"): "30", ("2025", "10"): "31", ("2025", "11"): "30", ("2025", "12"): "31"
}

for year, month in tqdm(months, desc="Downloading distinct ship data files"):
    last_day = days_in_month[(year, month)]
    start_date = f"{year}-{month}-01T00:00:00Z"
    end_date = f"{year}-{month}-{last_day}T23:59:59Z"
    
    query = f"?MMSI%2Ctime%2CLat%2CLon%2CSOG%2CCOG%2CHeading%2CVesselType%2CStatus%2CLength%2CWidth%2CDraft%2CCargo&time%3E={start_date}&time%3C={end_date}"
    full_url = url_base + query
    
    file_name = f"ships_movement_{year}_{month}.csv"
    file_path = os.path.join(folder_path, file_name)
    
    response = requests.get(full_url)
    
    if response.status_code == 200:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response.text)