import requests
import json
from PIL import Image
from io import BytesIO

with open("credentials.json", "r") as file:
    credentials = json.load(file)

class unsplash():
    def __init__(self):
        access_key = credentials["Unsplash"]
        random_url = f"https://api.unsplash.com/photos/random?client_id={access_key}"

    def get_random(self):
        response = requests.get(random_url)
        photo = response.json()

        payload = {"client_id": access_key}
        status_code = requests.get(photo["links"]["download_location"], payload).status_code

        if status_code == 200:
            download_endpoint = f"https://api.unsplash.com/photos/{photo["id"]}/download?client_id={access_key}"
            print(download_endpoint)
            image_download_url = requests.get(download_endpoint).json()["url"]
            print(image_download_url)
            #response = requests.get(image_download_url)
            #image = Image.open(BytesIO(response.content))

            return image_download_url

        else:
            print("unsplash error: ", status_code)
            return None