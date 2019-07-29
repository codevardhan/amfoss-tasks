from PIL import Image
import pytesseract

img = Image.open("test1.png")
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
result = pytesseract.image_to_string(Image.open('test1.png'))

with open('magic.txt', mode='w') as file:
    file.write("")
    file.write(result)
    print("success")
