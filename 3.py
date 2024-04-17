from PIL import Image, ImageFilter
a = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
for name in a:
    image = Image.open(name)
    image_f = image.filter(ImageFilter.EMBOSS)
    n = name.replace(".", "new.")
    image_f.save(n)
    image_f.show()