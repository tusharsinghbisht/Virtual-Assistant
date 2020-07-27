# import win10toast

# toaster = win10toast.ToastNotifier()

# toaster.show_toast('Python', 'Hello World', duration=10)

# import datetime
# curr_time = datetime.datetime.now().strftime('%H:%M:%S')
# # print(type(curr_time))
# print(curr_time)

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open('./img/bg.jpg')

print(pytesseract.image_to_string(img))
