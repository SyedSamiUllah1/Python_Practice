import qrcode
from PIL import Image
# img=qr.make("Subscribe to My Channel")
# img.save("The_Fact_Finder.png")
qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=20,border=4)
qr.add_data("https://www.youtube.com")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("Hemlogggg.png")