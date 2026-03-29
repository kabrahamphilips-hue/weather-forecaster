import os
import requests

API_KEY = os.getenv("API_KEY")

city = "Toronto"  # safer than random cities

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print(data)  # debug

temp = data["main"]["temp"]

with open("README.md", "w") as f:
    f.write(f"# Weather Update\n\n{city}: {temp}°C\n")
