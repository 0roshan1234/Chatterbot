import pyqrcode
content="jai shri krishna radhe"
url = pyqrcode.create(content)
url.png("chatterbot.png", scale=8)
print("successfully executed")
