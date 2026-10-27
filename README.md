Maritime Weather & Traffic EDA Analysis
​An exploratory data analysis (EDA) project investigating the complex relationships between marine weather conditions, vessel traffic distribution, Speed Over Ground (SOG), and port arrival patterns.

​🚀 Project Overview
​Understanding maritime telemetry and environmental conditions is critical for optimizing shipping efficiency, predicting port congestion, and ensuring navigational safety. This project analyzes a comprehensive maritime dataset using Python, extracting key insights through advanced data visualization techniques.
​Key aspects analyzed in this project include:
​Traffic Volume Trends: Monthly and seasonal distribution of vessel traffic.
​Vessel Speed Dynamics: Examining the relationship between Speed Over Ground (SOG) and days of the week.
​Weather Impact Analysis: Assessing how wind categories, snowfall, and sea-level pressure influence ship velocity and operations.
​Port Arrival Distribution: Evaluating monthly percentages of ship arrivals to forecast congestion and transit efficiency.

​🧰 Libraries & Tech Stack
​The analysis is built using Python and relies on the following core data science and visualization libraries:
import numpy as np
import pandas as pd
from scipy import stats
import os
import matplotlib.pyplot as plt
import seaborn as sns

📊 Key Findings & Visualizations
​1. Daily & Monthly Traffic Distribution
​Trend: Maritime activity starts at a lower baseline in January (~0.61 million vessels) and experiences a steady upward trend through spring.
​Peak: Traffic peaks significantly during mid-year, reaching over 1.1 million vessels in July and August before gradually declining through autumn and winter.

​2. Speed Over Ground (SOG) by Day of Week
​Anomaly Detection: Average SOG peaks sharply on Mondays at approximately 2.5 knots, before dropping and remaining minimal (\sim 0.0 knots) from Tuesday through Sunday. This highlights unique weekly telemetry concentrations or reporting schedules.

​3. Weather Impact Index (Wind, Snowfall, and Pressure)
​Wind & Snow: Multi-panel analytical grids compare vessel SOG across wind categories (Stormy, Strong, Calm, Moderate) and snowfall presence, illustrating median speed variations and outlier telemetry points.
​Barometric Pressure: Sea-level pressure trends mirror seasonal temperature progressions, transitioning smoothly from cooler winter months to warmer summer months.
​Correlation: Statistical correlation matrices examine linear dependencies between sea-level pressure and vessel SOG.

4. Impact On Speed by (SOG)
This correlation heatmap examines the statistical relationship between sea level pressure and vessel Speed Over Ground (SOG). The analytical visualization evaluates potential linear dependencies between atmospheric barometric metrics and maritime transit velocity. The diagonal values in the matrix show a perfect self-correlation of 1.00 for both analyzed variables as expected. Meanwhile, the off-diagonal correlation coefficient registers precisely at 0.00, indicating an absence of direct linear dependency. This finding demonstrates that sea level pressure variations alone do not exhibit a linear impact on vessel speed within this dataset.

​5. Port Arrival Delays & Monthly Share
​Arrival Breakdown: Pie chart analysis shows the percentage distribution of ship arrivals across months, peaking in August (10.8\%) and September (9.6\%), offering actionable benchmarks for port management and logistics planning.

📈 Future Enhancements
​Build predictive machine learning models to forecast port arrival delays based on live weather telemetry.
​Apply non-linear regression modeling to study combined weather factor impacts on vessel transit times.
