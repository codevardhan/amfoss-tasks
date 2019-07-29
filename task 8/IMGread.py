from PIL import Image
import pytesseract

img = Image.open("test1.png")
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
txt = pytesseract.image_to_string(Image.open('test1.png'))
lis = list(txt)
a = int(lis[0])
b = int(lis[2])
if "+" in txt:
    ans = a + b
if "-" in txt:
    ans = a - b
if "*" in txt:
    ans = a * b
if "/" in txt:
    ans = a / b
print(ans)
