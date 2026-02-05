from ai import gen_embeds
from file_managment import database
from pictures import unsplash

db = database()
embeds = gen_embeds()
pic = unsplash()