from pytesseract import *
from PIL import Image

img = Image.open('captcha.jpg')
text = image_to_string(img)
print(text)