import os
import requests

API_KEY = os.getenv("API_KEY")

url = f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

temp = data["main"]["temp"]

with open("README.md", "w") as f:
    f.write(f"# Weather Update\n\nCurrent temp: {temp}°C\n")
