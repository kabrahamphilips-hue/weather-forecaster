import os
import requests

API_KEY = os.getenv("API_KEY")
city = "Toronto"  # change your city here

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

# Debug: print response if action fails
print(data)

# Safety check: make sure 'main' exists
if "main" in data:
    temp = data["main"]["temp"]
    with open("README.md", "w") as f:
        f.write(f"# Weather Update\n\n{city}: {temp}°C\n")
else:
    print("Error fetching weather:", data)
    exit(1)
