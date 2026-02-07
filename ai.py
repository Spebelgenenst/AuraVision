import requests
import torch
from PIL import Image
from transformers import AlignProcessor, AlignModel

class gen_embeds():

    def __init__(self):
        self.processor = AlignProcessor.from_pretrained("kakaobrain/align-base")
        self.model = AlignModel.from_pretrained("kakaobrain/align-base")


    def image_embed(self, image):
        image_inputs = self.processor(images=image.convert("RGB"), return_tensors="pt") #.to(self.model.device)

        with torch.no_grad():
            output = self.model.get_image_features(**image_inputs)

        image_embed = output.pooler_output

        return torch.nn.functional.normalize(image_embed, p=2, dim=1)


    def text_embed(self, text):
        text_inputs = self.processor(text=text, padding=True, return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            output = self.model.get_text_features(**text_inputs)

        text_embed = output.pooler_output

        return torch.nn.functional.normalize(text_embed, p=2, dim=1)

    #def get_similarity(self, text_embeds, image_embeds):
    #    return torch.matmul(text_embeds, image_embeds.T)67