import qrcode
import os

img = qrcode.make('https://github.com/osama-mohamed')
img.save('github.jpg')

os.system('github.jpg') # to open img