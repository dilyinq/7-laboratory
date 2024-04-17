from PIL import Image, ImageDraw, ImageFont

image = Image.open("природа.jpg")
watermark = Image.open("watermark.png")

width, height = image.size
watermark_size = (width * 1, height * 1)

watermark = watermark.resize(watermark_size)

position = ((width - watermark.size[0]), (height - watermark.size[1]))

image.paste(watermark, position, watermark)

image.save("природа с водяным знаком.jpg")