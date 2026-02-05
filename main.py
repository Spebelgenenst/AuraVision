from ai import gen_embeds
from database import database
from pictures import unsplash

db = database()
embeds = gen_embeds()
pic = unsplash()

class main():
    pass

class search():
    pass

class new_data():
    def unsplash(self):
        photo = pic.get_random()
        image = pic.download_image(photo=photo)

        embed = embeds.image_embed(image=image)

        database.add_entry(embed=embed, url=photo["links"]["html"], link=photo["urls"]["raw"], credit=[ photo["user"]["name"] , photo["user"]["username"] ], source="unsplash")

