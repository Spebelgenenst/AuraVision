import requests
import torch
from PIL import Image
from transformers import AlignProcessor, AlignModel

class ai_embeds():

    def __init__(self):
        self.processor = AlignProcessor.from_pretrained("kakaobrain/align-base")
        self.model = AlignModel.from_pretrained("kakaobrain/align-base")

        print("ai_embeds loaded")


    def image_embed(self, image_url):
        image = Image.open(requests.get(image_url, stream=True).raw)

        inputs = self.processor(images=image, return_tensors="pt")

        with torch.no_grad():
            image_embeds = self.model.get_image_features(
                pixel_values=inputs['pixel_values'],
            )

        return image_embeds


    def text_embed(self, text):
        inputs = self.processor(text=text, return_tensors="pt")

        with torch.no_grad():
            text_embeds = self.model.get_text_features(
                input_ids=inputs['input_ids'],
                attention_mask=inputs['attention_mask'],
                token_type_ids=inputs['token_type_ids'],
            )

        return text_embeds