import os
from moviepy.editor import VideoFileClip
from PIL import Image


SAMPLE_INPUTS = os.path.join(os.path.join(os.path.dirname(__file__), 'data'), 'inputs')
SAMPLE_OUTPUTS = os.path.join(os.path.join(os.path.dirname(__file__), 'data'), 'outputs')
source_path = os.path.join(SAMPLE_INPUTS, '1.mp4')
clip = VideoFileClip(source_path)
fps = clip.reader.fps


# thumbnails per every 1 second
thumbnail_per_duration_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-duration')
os.makedirs(thumbnail_per_duration_dir, exist_ok=True)
duration = clip.duration # clip.reader.duration
max_duration = int(duration) + 1
for i in range(0, max_duration): # frame every 1 second
  frame = clip.get_frame(i)
  new_img_filepath = os.path.join(thumbnail_per_duration_dir, f'{i}.jpg')
  new_img = Image.fromarray(frame)
  new_img.save(new_img_filepath)
  print(f'frame at {i} duration saved at {new_img_filepath}')



# thumbnails per milli second
thumbnail_per_milli_second_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-milli-second')
os.makedirs(thumbnail_per_milli_second_dir, exist_ok=True)
for i, frame in enumerate(clip.iter_frames()):
  if i % fps == 0:
    current_ms = int((i / fps) * 1000)
    new_img_filepath = os.path.join(thumbnail_per_milli_second_dir, f'{current_ms}.jpg')
    new_img = Image.fromarray(frame)
    new_img.save(new_img_filepath)
    print(f'frame at {i} milli second saved at {new_img_filepath}')



# thumbnails per 1 second
thumbnail_per_second_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-second')
os.makedirs(thumbnail_per_second_dir, exist_ok=True)
for i, frame in enumerate(clip.iter_frames()):
  if i % fps == 0:
    current_seconds = int(i / fps)
    new_img_filepath = os.path.join(thumbnail_per_second_dir, f'{current_seconds}.jpg')
    new_img = Image.fromarray(frame)
    new_img.save(new_img_filepath)
    print(f'frame at {i} second saved at {new_img_filepath}')



# thumbnails per 0.5 second
thumbnail_per_half_second_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-half-second')
os.makedirs(thumbnail_per_half_second_dir, exist_ok=True)
for i, frame in enumerate(clip.iter_frames()):
  fphs = int(fps / 2.0)
  if i % fphs == 0:
    current_hs = int((i / fps) * 1000)
    new_img_filepath = os.path.join(thumbnail_per_half_second_dir, f'{current_hs}.jpg')
    new_img = Image.fromarray(frame)
    new_img.save(new_img_filepath)
    print(f'frame at {i} half second saved at {new_img_filepath}')



# thumbnails per 0.1 second
thumbnail_per_decisecond_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-decisecond')
os.makedirs(thumbnail_per_decisecond_dir, exist_ok=True)
for i, frame in enumerate(clip.iter_frames()):
  fphs = int(fps / 10.0)
  if i % fphs == 0:
    current_ds = int((i / fps) * 1000)
    new_img_filepath = os.path.join(thumbnail_per_decisecond_dir, f'{current_ds}.jpg')
    new_img = Image.fromarray(frame)
    new_img.save(new_img_filepath)
    print(f'frame at {i} decisecond saved at {new_img_filepath}')



# thumbnails per frames 
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-frame')
os.makedirs(thumbnail_per_frame_dir, exist_ok=True)
for i, frame in enumerate(clip.iter_frames()):
  new_img_filepath = os.path.join(thumbnail_per_frame_dir, f'{i}.jpg')
  new_img = Image.fromarray(frame)
  new_img.save(new_img_filepath)
  print(f'frame at {i} per frame saved at {new_img_filepath}')