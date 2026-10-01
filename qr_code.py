import qrcode

url = input("Enter the URL: ").strip()
file_path = "qrcode.png"

code = qrcode.QRCode()
code.add_data(url)

image = code.make_image()
image.save(file_path)

print("QR Code successfully generated :)")