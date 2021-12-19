import os
from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import crop


SAMPLE_INPUTS = os.path.join(os.path.join(os.path.dirname(__file__), 'data'), 'inputs')
SAMPLE_OUTPUTS = os.path.join(os.path.join(os.path.dirname(__file__), 'data'), 'outputs')
source_path = os.path.join(SAMPLE_INPUTS, '1.mp4')
output_path = os.path.join(SAMPLE_OUTPUTS, '1.gif')


clip = VideoFileClip(source_path)
fps = clip.reader.fps
w, h = clip.size
subclip = clip.subclip(10, 20) # from second, to second
cropped_clip = crop(subclip, width=480, height=480, x_center=w/2, y_center=h/2)
# cropped_clip = crop(subclip, height=480, y_center=h/2)
# cropped_clip = crop(subclip, width=480, x_center=w/2)
cropped_clip.write_gif(output_path, fps=fps, program='ffmpeg')



# # another way
# clip = VideoFileClip(source_path)
# fps = clip.reader.fps
# subclip = clip.subclip(10, 20) # from second, to second
# subclip = subclip.resize(width=480)
# subclip.write_gif(output_path, fps=fps, program='ffmpeg')