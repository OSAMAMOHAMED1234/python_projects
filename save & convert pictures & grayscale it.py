from PIL import Image
img = Image.open(r"C:\Users\OSAMA\Desktop\hijab.png").convert('L') # pic distnation
img.show() # open pic
img.save('new_pic_name.png') # save pic as a new type & new name
