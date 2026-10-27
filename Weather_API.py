import pandas as pd
import numpy as np
import os
from tqdm import tqdm

folder_path = r'C:\Users\Vikas\Documents\ProMain1\Data'
months = [f"{m:02d}" for m in range(1, 13)]

def generate_weather_profile(mmsi_val):
    if pd.isna(mmsi_val):
        seed_val = 42
    else:
        try:
            seed_val = int(str(mmsi_val).split('.')[0][-4:])
        except:
            seed_val = 42
    np.random.seed(seed_val)
    
    weather_type = np.random.choice(['clear', 'rainy', 'stormy', 'snowy'], p=[0.5, 0.3, 0.15, 0.05])
    
    if weather_type == 'clear':
        temp = np.round(np.random.uniform(15.0, 30.0), 2)
        humidity = np.round(np.random.uniform(40.0, 70.0), 2)
        rain = 0.0
        snow = 0.0
        pressure = np.round(np.random.uniform(1015.0, 1025.0), 2)
        clouds = np.round(np.random.uniform(0.0, 30.0), 2)
        wind_speed = np.round(np.random.uniform(2.0, 10.0), 2)
        wind_dir = np.random.randint(0, 360)
        soil_temp = np.round(np.random.uniform(3.5, 7.0), 2)
    elif weather_type == 'rainy':
        temp = np.round(np.random.uniform(10.0, 20.0), 2)
        humidity = np.round(np.random.uniform(80.0, 99.0), 2)
        rain = np.round(np.random.exponential(scale=5.0), 2)
        snow = 0.0
        pressure = np.round(np.random.uniform(995.0, 1010.0), 2)
        clouds = np.round(np.random.uniform(70.0, 100.0), 2)
        wind_speed = np.round(np.random.uniform(10.0, 30.0), 2)
        wind_dir = np.random.randint(0, 360)
        soil_temp = np.round(np.random.uniform(1.0, 5.0), 2)
    elif weather_type == 'stormy':
        temp = np.round(np.random.uniform(12.0, 25.0), 2)
        humidity = np.round(np.random.uniform(60.0, 90.0), 2)
        rain = np.round(np.random.exponential(scale=10.0), 2)
        snow = 0.0
        pressure = np.round(np.random.uniform(980.0, 1000.0), 2)
        clouds = 100.0
        wind_speed = np.round(np.random.uniform(30.0, 60.0), 2)
        wind_dir = np.random.randint(0, 360)
        soil_temp = np.round(np.random.uniform(2.0, 6.0), 2)
    else:
        temp = np.round(np.random.uniform(-5.0, 5.0), 2)
        humidity = np.round(np.random.uniform(70.0, 90.0), 2)
        rain = 0.0
        snow = np.round(np.random.exponential(scale=3.0), 2)
        pressure = np.round(np.random.uniform(1000.0, 1020.0), 2)
        clouds = np.round(np.random.uniform(80.0, 100.0), 2)
        wind_speed = np.round(np.random.uniform(5.0, 25.0), 2)
        wind_dir = np.random.randint(0, 360)
        soil_temp = np.round(np.random.uniform(0.0, 3.0), 2)
        
    return [temp, humidity, rain, snow, pressure, clouds, wind_speed, wind_dir, soil_temp]

columns = [
    'temperature_2m', 'relative_humidity', 'rain', 'snowfall',
    'sea_level_pressure', 'total_cloud_cover',
    'wind_speed_10m', 'wind_direction_10m', 'soil_temperature_0_to_7cm'
]

for month in tqdm(months, desc="Generating weather files with timestamps"):
    ship_file = f"ships_movement_2024_{month}.csv"
    ship_path = os.path.join(folder_path, ship_file)
    
    if os.path.exists(ship_path):
        df_ship = pd.read_csv(ship_path)
        
        weather_data = list(df_ship['MMSI'].apply(generate_weather_profile))
        weather_df = pd.DataFrame(weather_data, columns=columns)
        
        weather_df.insert(0, 'time', df_ship['time'])
        
        weather_output_file = f"weather_raw_data_2024_{month}.csv"
        weather_path = os.path.join(folder_path, weather_output_file)
        weather_df.to_csv(weather_path, index=False)