from PIL import Image
from pathlib import Path

# Path
img_dir = "images"

overlay_img_path = Path(img_dir, "1.png")
background_img_path = Path(img_dir, "2.jpg")
output_path = Path(img_dir, "final.jpg")

background_img = Image.open(background_img_path)
overlay_img = Image.open(overlay_img_path)
overlay_img = overlay_img.convert(mode='RGBA')
background_img.paste(overlay_img, (0, 0), mask=overlay_img)

background_img.save(output_path)
