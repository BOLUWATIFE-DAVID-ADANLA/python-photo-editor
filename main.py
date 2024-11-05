from PIL import Image, ImageFilter
import os

pathin = './images'
pathout = './edited-images'

os.makedirs(pathout, exist_ok=True)

for filename in os.listdir(pathin):
    # checks if file is an image 
    if filename.endswith(('.jpg', '.jpeg', '.png','.bmp', '.gif' )):
        img = Image.open(f'{pathin}/{filename}')
        
        # apply sharpen filter 
        edit = img.filter(ImageFilter.SHARPEN)
        
        # create an edited filename 
        clean_name = os.path.splitext(filename)[0]
        edit.save(f'{pathout}/{clean_name}_editied.{img.format.lower()}', img.format)