from ai import gen_embeds
from database import database
#from pictures import unsplash
from pictures_fake import unsplash
import hashlib

db = database()
embeds = gen_embeds()
pic = unsplash()

class search():
    pass

class collect_data():
    def __init__(self):
        return

    def unsplash(self):
        photo = pic.get_random()
        if photo:
            image = pic.download_image(photo=photo)
        else:
            return True #returns if rate limit is reached

        embed = embeds.image_embed(image=image)

        db.add_entry(embed=embed, url=photo["urls"]["raw"], link=photo["links"]["html"], credit=[ photo["user"]["name"] , photo["user"]["username"] ], source="unsplash")

data = collect_data()