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


    def get_embed(self, num):
        return
    
    def get_url(self, num):
        return