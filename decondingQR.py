from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/Utente/Desktop/encodingDecodingQR/qrImage/myqrcode.png')

result = decode(img)

print(result)