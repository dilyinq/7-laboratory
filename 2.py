from PIL import Image
image = Image.open(r"C:\Users\1\Pictures\горы.jpg")

image2= image.resize((image.width // 3, image.height // 3))
image2.save (r"C:\Users\1\Pictures\уменьшение в 3 раза.jpg") # необработанная строка

horizontal_image = image.transpose(Image.FLIP_LEFT_RIGHT)
horizontal_image.save(r"C:\Users\1\Pictures\по горизонтали.jpg")

vertical_image = image.transpose(Image.FLIP_TOP_BOTTOM)
vertical_image.save(r"C:\Users\1\Pictures\зеркальное по вертикали.jpg")



