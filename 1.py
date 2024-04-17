from PIL import Image
image = Image.open(r"C:\Users\1\Pictures\горы.jpg")

width, height = image.size
print(f'Размер изображения: {width}x{height} пикселей')

image_format = image.format
print(f'Формат изображения: {image_format}')

color_mode = image.mode
print(f'Цветовая модель изображения: {color_mode}')

image. show ()


