import qrcode


def encode(url):
    img = qrcode.make(url)
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color='red', back_color='white')
    img.save('C:/Users/Utente/Desktop/encodingDecodingQR/qrImage/myqrcode.png')
