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
        result = client.search(
            collection_name="embeds",
            data=embed,
            limit=count,
            output_fields=["url"],
        )

        return result

    def add_entry(self, embed, url): # add entry with url and embed
        self.last_id += 1

        data = [{"id": self.last_id, "vector": embed, "url": url}]

        return client.insert(collection_name="embeds", data=data)