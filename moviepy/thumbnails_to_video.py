import os
from moviepy.editor import ImageSequenceClip, ImageClip


SAMPLE_OUTPUTS = os.path.join(os.path.join(os.path.dirname(__file__), 'data'), 'outputs')
thumbnails_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-duration')
fps_in_output_video = 30
output_video = os.path.join(SAMPLE_OUTPUTS, 'video.mp4')



this_dir = sorted(os.listdir(thumbnails_dir), key=len)
filepaths = [os.path.join(thumbnails_dir, fname) for fname in this_dir if fname.endswith('.jpg')]
# clip = ImageSequenceClip(filepaths, fps=fps_in_output_video)
# clip.write_videofile(output_video)
my_clips = [ImageClip(path).img for path in filepaths]
clip = ImageSequenceClip(my_clips, fps=fps_in_output_video)
clip.write_videofile(output_video)


# filepaths = [os.path.join(thumbnails_dir, fname) for fname in this_dir if fname.endswith('.jpg')]
# filepaths = []
# for fname in this_dir:
#   if fname.endswith('.jpg'):
#     path = os.path.join(thumbnails_dir, fname)
#     filepaths.append(path)



# # another way
# directory = {}
# for root, dirs, files in os.walk(thumbnails_dir):
#   for fname in files:
#     filepath = os.path.join(root, fname)
#     try:
#       key = int(fname.replace('.jpg', ''))
#     except:
#       key = None
#     if key != None:
#       directory[key] = filepath
# new_paths = []
# for k in sorted(directory.keys()):
#   newfilepath = directory[k]
#   new_paths.append(newfilepath)
# # clip = ImageSequenceClip(new_paths, fps=fps_in_output_video)
# # clip.write_videofile(output_video)
# my_clips = []
# for path in new_paths:
#   frame = ImageClip(path)
#   my_clips.append(frame.img)
# clip = ImageSequenceClip(my_clips, fps=fps_in_output_video)
# clip.write_videofile(output_video)