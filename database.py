from pymilvus import MilvusClient

class database():
    def __init__(self):
        self.client = MilvusClient("embeds.db")

        if self.client.has_collection(collection_name="embeds"):
            self.client.drop_collection(collection_name="embeds")
        self.client.create_collection(
            collection_name="embeds",
            dimension=640,  # The vectors we will use in this demo has 768 dimensions
            auto_id=True
        )

    def search(self, embed, count):
        result = self.client.search(
            collection_name="embeds",
            data=embed,
            limit=count,
            output_fields=["url", "credit"],
        )

        return result

    def add_entry(self, embed, url, link, credit, source): # add entry with url and embed
        #print(embed)
        list_embed = embed.tolist()[0] # convertsd it to a list and removes the outer Brackets [[content]] -> [content]
        print(list_embed)
        print(len(list_embed))

        data = [{"vector": list_embed, "url": url, "link": link, "credit": credit, "source": source}]

        return self.client.insert(collection_name="embeds", data=data)