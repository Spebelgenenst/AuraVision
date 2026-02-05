# this is made by ai and untested

import requests
import os
import random

# Beispiel: Unsplash API (kostenlos, aber Anmeldung nötig)
API_KEY = "DEIN_API_KEY"
URL = "https://api.unsplash.com/photos/random"

headers = {
    "Authorization": f"Client-ID {API_KEY}"
}

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Bild gespeichert als {filename}")
    else:
        print("Fehler beim Herunterladen")

response = requests.get(URL, headers=headers)
if response.status_code == 200:
    data = response.json()
    image_url = data['urls']['regular']
    filename = f"bild_{random.randint(1, 1000)}.jpg"
    download_image(image_url, filename)
else:
    print("Fehler bei der API-Anfrage")
