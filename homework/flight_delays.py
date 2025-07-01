import pandas as pd
import matplotlib.pyplot as plt
import os

# Asegura que exista la carpeta de salida
os.makedirs("files/images", exist_ok=True)

# Simulando un dataframe de ejemplo:
# (en la práctica debes cargar tu CSV real con pd.read_csv)
# Aquí va un ejemplo de estructura mínima
data = pd.DataFrame({
    "carrier": ["AA", "AA", "UA", "UA", "DL", "DL"],
    "day_of_week": [1, 2, 3, 4, 5, 6],
    "hour": [8, 9, 10, 11, 12, 13],
    "delay": [15, 20, 35, 10, 5, 60],
})

# 1. delays_by_carrier
carrier_delay = data.groupby("carrier")["delay"].mean()
carrier_delay.plot(kind="bar", title="Average Delay by Carrier")
plt.ylabel("Minutes")
plt.savefig("files/images/delays_by_carrier.png")
plt.close()

# 2. delays_by_day_of_week
day_delay = data.groupby("day_of_week")["delay"].mean()
day_delay.plot(kind="bar", title="Average Delay by Day of Week")
plt.ylabel("Minutes")
plt.savefig("files/images/delays_by_day_of_week.png")
plt.close()

# 3. delays_by_hour_of_day
hour_delay = data.groupby("hour")["delay"].mean()
hour_delay.plot(kind="bar", title="Average Delay by Hour of Day")
plt.ylabel("Minutes")
plt.savefig("files/images/delays_by_hour_of_day.png")
plt.close()