# BW image moving
import os.path
import shutil

from PIL import Image

# File path, warning: python will go into each folder inside each folder and modify each file
# Unless you want to change all the folders too make sure this is the only folder inside the folder

TK().withdraw() # hides ui since we only need the open folder ui
print("Source folder")
src = filedialog.askdirectory()
print("Destination folder")
dst = filedialog.askdirectory()

for file in os.listdir(src):
    f_img = src + "/" + file
    img = Image.open(f_img)
    # Gets the average color of a file
    img = img.resize((1, 1), Image.ANTIALIAS)
    imgcolor = img.getpixel((0, 0))
    print(imgcolor)

    print(src + file)
    print(dst + file)

    # On the color slider if all three values are equal then it is grayscale
    if imgcolor[0] == imgcolor[1] == imgcolor[2]:
        shutil.move(img, dst)
