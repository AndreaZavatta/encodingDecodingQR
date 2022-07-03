import webbrowser
import zxing as zxing


def decode():
    reader = zxing.BarCodeReader()
    url = reader.decode("C:/Users/Utente/Desktop/encodingDecodingQR/qrImage/myqrcode.png").raw
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser(
                            "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)
