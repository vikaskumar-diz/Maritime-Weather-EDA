import pandas as pd
import numpy as np
import os
from tqdm import tqdm

folder_path = r'C:\Users\Vikas\Documents\ProMain1\Data'
months = [f"{m:02d}" for m in range(1, 13)]

ship_dfs = []
weather_dfs = []

for month in tqdm(months, desc="Loading files"):
    ship_file = f"ships_movement_2024_{month}.csv"
    weather_file = f"weather_raw_data_2024_{month}.csv"
    
    ship_path = os.path.join(folder_path, ship_file)
    weather_path = os.path.join(folder_path, weather_file)
    
    if os.path.exists(ship_path) and os.path.exists(weather_path):
        df_ship = pd.read_csv(ship_path)
        df_weather = pd.read_csv(weather_path)
        
        ship_dfs.append(df_ship)
        weather_dfs.append(df_weather)

master_ship = pd.concat(ship_dfs, ignore_index=True)
master_weather = pd.concat(weather_dfs, ignore_index=True)

print("Merging datasets by timestamp...")
merged_df = pd.merge(master_ship, master_weather, on='time', how='inner')

print("Cleaning data...")

clean_df = merged_df.drop_duplicates()

critical_cols = ['MMSI', 'time', 'temperature_2m']
clean_df = clean_df.dropna(subset=critical_cols)

if 'wind_speed_10m' in clean_df.columns:
    clean_df = clean_df[clean_df['wind_speed_10m'] >= 0]

# फाइनल फाइल सेव करना
output_path = os.path.join(folder_path, 'final_clean_data.csv')
clean_df.to_csv(output_path, index=False)

print(f"Process complete. Final clean data saved at: {output_path}")