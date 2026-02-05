from pymilvus import MilvusClient

class database():
    def __init__(self):
        client = MilvusClient("embeds.db")

        if client.has_collection(collection_name="embeds"):
            client.drop_collection(collection_name="embeds")
        client.create_collection(
            collection_name="embeds",
            dimension=2,  # The vectors we will use in this demo has 768 dimensions
        )

        self.last_id = client.query(collection_name="embeds", expr="id >= 0", limit=1, sort_by=["id DESC"])
        print(self.last_id)

    def search(self, embed, count):
        return

    def add_entry(self, embed, url): # add entry with url and embed
        return

    def add_url(self, url): # add an url with a blank embed
        return

    def add_embed(self, id, embed): # insert something (blank embed)
        return