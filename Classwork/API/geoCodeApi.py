import requests

cn = "London"
url = f"https://nominatim.openstreetmap.org/search?city={cn}&format=json&limit=1"

headers = {
    "User-Agent": "my-app"   # Required by Nominatim
}

response = requests.get(url, headers=headers)
data = response.json()

print(data[0]["lat"], data[0]["lon"])