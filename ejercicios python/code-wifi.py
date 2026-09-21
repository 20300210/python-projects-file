from PIL import Image
from wifi_qrcode_generator.generator import wifi_qrcode

ssid = "CLCODING_WIFI"
password = "1234secret"
security = "WPA"

qr = wifi_qrcode(ssid, False, security, password)
qr.make_image().save("wifi_qr.png")

img = Image.open("wifi_qr.png")
img.show()
