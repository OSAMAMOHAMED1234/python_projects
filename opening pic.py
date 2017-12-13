import os
from PIL import Image

img = Image.open(r"C:\Users\OSAMA\Desktop\hijab.png").show()
##img.show()
os.startfile(r"C:\Users\OSAMA\Desktop\hijab.png")

from PIL import Image
img = Image.open(r"C:\Users\OSAMA\Desktop\hijab.png").convert('L')
img.show()
img.save('newh.jpg')


from PIL import Image
img = Image.open(r"C:\Users\OSAMA\Desktop\hijab.png")#.convert('L')
new_img = img.resize((256,256))
new_img.save('brick-house-256x256.png','png')

