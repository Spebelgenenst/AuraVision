import requests
import json
from PIL import Image
from io import BytesIO

with open("credentials.json", "r") as file:
    credentials = json.load(file)

ACCESS_KEY = credentials["Unsplash"]

random_url = f"https://api.unsplash.com/photos/random?client_id={ACCESS_KEY}"
response = requests.get(random_url)
photo = response.json()

payload = {"client_id": ACCESS_KEY}
status_code = requests.get(photo["links"]["download_location"], payload).status_code

if status_code == 200:
    download_endpoint = f"https://api.unsplash.com/photos/{photo["id"]}/download?client_id={ACCESS_KEY}"
    image_download_url = requests.get(download_endpoint).json()["url"]
    response = requests.get(image_download_url)
    image = Image.open(BytesIO(response.content))

else:
    print("ERROR: ", status_code)

print(image)