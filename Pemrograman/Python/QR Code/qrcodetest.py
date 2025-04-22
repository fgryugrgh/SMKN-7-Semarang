import qrcode 
import PIL
from PIL import Image

img = qrcode.make('s.id/fardancs')

resize_code = img.resize((800,800))
logo_size = 145

width, height = resize_code.size

logo = Image.open('logo.png')

xmin = ymin = int((width / 2) - (logo_size / 2))
xmax = ymax = int((width / 2) + (logo_size / 2))

logo = logo.resize((xmax - xmin, ymax - ymin))

resize_code.paste(logo, (xmin, ymin, xmax, ymax), mask=logo)

resize_code.show()
resize_code.save('qrcode.png', 'PNG')
