import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=20,border=4,)
qr.add_data("https://www.youtube.com/playlist?list=PLu0W_9lII9agqZuv_XJen_BEHycIh-FmG")

qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("utube.png")