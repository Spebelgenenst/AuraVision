import requests
import torch
from PIL import Image
from transformers import AlignProcessor, AlignModel

class gen_embeds():

    def __init__(self):
        self.processor = AlignProcessor.from_pretrained("kakaobrain/align-base")
        self.model = AlignModel.from_pretrained("kakaobrain/align-base")


    def image_embed(self, image):
        image_inputs = self.processor(images=image, return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            image_embeds = self.model.get_image_features(**image_inputs)

        return image_embeds / image_embeds.norm(p=2, dim=-1, keepdim=True)


    def text_embed(self, text):
        text_inputs = self.processor(text=text, padding=True, return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            text_embeds = self.model.get_text_features(**text_inputs)

        return text_embeds  / text_embeds.norm(p=2, dim=-1, keepdim=True)

    #def get_similarity(self, text_embeds, image_embeds):
    #    return torch.matmul(text_embeds, image_embeds.T)