import os
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, concatenate_videoclips, CompositeVideoClip


SAMPLE_INPUTS = os.path.join(os.path.join(os.path.dirname(__file__), 'data'), 'inputs')
SAMPLE_OUTPUTS = os.path.join(os.path.join(os.path.dirname(__file__), 'data'), 'outputs')
source_path = os.path.join(SAMPLE_INPUTS, '1.mp4')
source_audio_path = os.path.join(SAMPLE_INPUTS, '1.mp3')
final_video_path = os.path.join(SAMPLE_OUTPUTS, '1.mp4')

video_clip = VideoFileClip(source_path)
original_audio = video_clip.audio
w, h = video_clip.size
fps = video_clip.fps

# intro video
intro_duration = 5 # seconds
intro_text = TextClip('Hello OSAMA!', fontsize=70, color='white', size=video_clip.size)
intro_text = intro_text.set_fps(fps)
intro_text = intro_text.set_duration(intro_duration)
intro_text = intro_text.set_pos('center')
background_audio_clip = AudioFileClip(source_audio_path)
intro_music = background_audio_clip.subclip(0, intro_duration)
intro_text = intro_text.set_audio(intro_music)
intro_text.write_videofile(final_video_path)

# watermark 
watermark_size = 60
watermark_text = TextClip('OSAMA!', fontsize=watermark_size, color='white', align='East', size=(w, watermark_size)) # align => East, West
watermark_text = watermark_text.set_fps(fps)
watermark_text = watermark_text.set_duration(video_clip.duration)
watermark_text = watermark_text.set_pos(('bottom'))
watermark_text = watermark_text.margin(left=10, right=10, bottom=10, opacity=1, color=(255, 23, 0)) # opacity=1 color will show

# combine main video & watermark
overlay_clip = CompositeVideoClip([video_clip, watermark_text], size=video_clip.size) # order important, main video then water mark
overlay_clip = overlay_clip.set_duration(video_clip.duration)
overlay_clip = overlay_clip.set_fps(fps)
overlay_clip = overlay_clip.set_audio(None)
overlay_clip = overlay_clip.set_audio(original_audio)

# final video => intro & overlay
final_clip = concatenate_videoclips([intro_text, overlay_clip])
final_clip.write_videofile(final_video_path)