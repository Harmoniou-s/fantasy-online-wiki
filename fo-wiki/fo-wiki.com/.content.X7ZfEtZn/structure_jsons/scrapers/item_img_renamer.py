import os
import json
import io
from PIL import Image

def loop_json():
    json_file = open("C:/Users/Nick/Unity/Fantasy Online/Wiki/fo-wiki/fo-wiki.com/.content.X7ZfEtZn/structure_jsons/edited/item_images_edited.json")
    img_json = json.load(json_file)
    path = "C:/Users/Nick/Unity/Fantasy Online/Wiki/fo-wiki/fo-wiki.com/.content.X7ZfEtZn/binary/"

    for img in img_json["images"]:
        raw = open(path + img["filename"], "rb").read()
        img_file = Image.open(io.BytesIO(raw))
        img_file.save("C:/Users/Nick/Unity/Fantasy Online/Wiki/fo-wiki/fo-wiki.com/.content.X7ZfEtZn/images/item/" + img["name"] + ".png")
        

if __name__ == "__main__":
    loop_json()
