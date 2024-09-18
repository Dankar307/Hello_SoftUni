import qrcode
img = qrcode.make('https://www.instagram.com/daniel.karadzhov/?hl=bg')
type(img)  # qrcode.image.pil.PilImage
img.save("qrcode1.png")