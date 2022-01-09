
import face_recognition
from PIL import Image, ImageDraw

img = face_recognition.load_image_file('1.jpg')
face_location = face_recognition.face_locations(img)
top, right, bottom, left = face_location[0]

image = Image.fromarray(img)
draw = ImageDraw.Draw(image)
draw.rectangle(((left, top), (right, bottom)), width=20, outline=(0, 0, 255))
del draw
image.show()


# recognize person in image contains group of people
import numpy as np
person = face_recognition.load_image_file('1.jpg')
group = face_recognition.load_image_file('group.jpg')

person_encoding = face_recognition.face_encodings(person)[0]
group_location = face_recognition.face_locations(group)
group_encoding = face_recognition.face_encodings(group, group_location)

images = Image.fromarray(group)
draw = ImageDraw.Draw(images)
for (top, right, bottom, left), face_encoding in zip(group_location, group_encoding):
  matches = face_recognition.compare_faces([person_encoding], face_encoding)
  distance = face_recognition.face_distance([person_encoding], face_encoding)
  match_index = np.argmin(distance)
  if matches[match_index]:
    draw.rectangle(((left, top), (right, bottom)), width=20, outline=(0, 0, 255))
del draw
images.show()