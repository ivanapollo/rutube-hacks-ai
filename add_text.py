from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# добавляет текст на фото
def add_text(img_path, text, font, color_font):
    img = Image.open(img_path)
    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype(font, 65)
    I1.text((10, 10), text, font=myFont, fill=color_font)
    img.show()
    img.save(img_path)
