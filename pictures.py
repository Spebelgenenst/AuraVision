import requests
import json
from PIL import Image
from io import BytesIO

with open("credentials.json", "r") as file:
    credentials = json.load(file)

class unsplash():
    def __init__(self):
        self.access_key = credentials["Unsplash"]
        self.random_url = f"https://api.unsplash.com/photos/random?client_id={self.access_key}"

    def get_random(self):
        response = requests.get(self.random_url)
        photo = response.json()

        return photo

    def download_image(self, photo):
        payload = {"client_id": self.access_key}
        status_code = requests.get(photo["links"]["download_location"], payload).status_code

        if status_code == 200:
            download_endpoint = f"https://api.unsplash.com/photos/{photo["id"]}/download?client_id={self.access_key}"
            image_download_url = requests.get(download_endpoint).json()["url"]
            response = requests.get(image_download_url)
            image = Image.open(BytesIO(response.content)).convert("RGB")
            #image = Image.open(requests.get(image_download_url).raw).convert("RGB")

            return image

        else:
            print("unsplash error: ", status_code)
            return None