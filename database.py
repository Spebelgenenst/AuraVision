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

    def search(self, embed, count):
        result = client.search(
            collection_name="embeds",
            data=embed,
            limit=count,
            output_fields=["url", "credit"],
        )

        return result

    def add_entry(self, embed, url, link, credit, source): # add entry with url and embed

        data = [{"auto_id": True, "vector": embed, "url": url, "link": link, "credit": credit, "source": source}]

        return client.insert(collection_name="embeds", data=data)