from ai import gen_embeds
from database import database
#from pictures import unsplash
from pictures_fake import unsplash
import hashlib

db = database()
embeds = gen_embeds()
pic = unsplash()

class search_engine():
    def for_text(self, text, count):
        embed = embeds.text_embed(text)
        return db.search(embed=embed, count=count)

class collect_data():
    #def __init__(self):
    #    return

    def unsplash_random(self):
        photo = pic.get_random()
        if photo:
            image = pic.download_image(photo=photo)
        else:
            return True #returns if rate limit is reached

        embed = embeds.image_embed(image=image)

        db.add_entry(embed=embed, url=photo["urls"]["raw"], link=photo["links"]["html"], credit=[ photo["user"]["name"] , photo["user"]["username"] ], source="unsplash")


data = collect_data()
search = search_engine()


data.unsplash_random()

result = search.for_text(text="meme doge", count=1)

print(result)