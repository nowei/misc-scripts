from PIL import Image, ImageOps
PATH='/c/Users/andre/Pictures/thisisfine_tp.jpg'
im = Image.open(PATH)

im_mirror = ImageOps.mirror(im)
im_mirror.save(PATH.split('.')[0] + '_reversed.jpg')
