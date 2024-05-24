from PIL import Image
#utiliser pour réduire les images

image_orig = Image.open("1663945.png")
image_resize = image_orig.resize((40, 40))
image_resize.save("12.png", format="png", optimize=True)