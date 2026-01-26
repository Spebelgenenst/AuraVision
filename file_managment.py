import json

class database():
    def __init__(self):
        with open("database.json", "r") as file:
            database = json.load(file)

    def get_entry(self, num):
        return database[num]["entry"]
    
    def get_url(self, num):
        return database[num]["url"]