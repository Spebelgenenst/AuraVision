import requests
import json
from PIL import Image
from io import BytesIO

class unsplash():
    def get_random(self):
        photo = {
            "links": {
                "html": "https://github.com/Spebelgenenst/ImAura-Search/blob/main/meme(for_testing).jpg"
            },
            "urls": {
                "raw": "https://github.com/Spebelgenenst/ImAura-Search/blob/main/meme(for_testing).jpg?raw=true"
            },
            "user": {
                "name": "Spebell",
                "username": "Spebelgenenst"
            }
        }

        return photo

    def download_image(self, photo):
        url = "https://github.com/Spebelgenenst/ImAura-Search/blob/main/meme(for_testing).jpg?raw=true"
        image = Image.open(requests.get(url, stream=True).raw)

        return image