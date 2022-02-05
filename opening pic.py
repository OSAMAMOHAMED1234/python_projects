import os
from PIL import Image

img = Image.open(os.path.join(os.path.dirname(__file__), '1.png')).show()
os.startfile(os.path.join(os.path.dirname(__file__), '1.png'))

img = Image.open(os.path.join(os.path.dirname(__file__), '1.png')).convert('L')
img.show()
img.save('2.jpg')

img = Image.open(os.path.join(os.path.dirname(__file__), '1.png'))#.convert('L')
new_img = img.resize((256,256))
new_img.save('2-256x256.png', 'png')