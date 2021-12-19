import os
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
from moviepy.audio.fx.all import volumex


SAMPLE_INPUTS = os.path.join(os.path.join(os.path.dirname(__file__), 'data'), 'inputs')
SAMPLE_OUTPUTS = os.path.join(os.path.join(os.path.dirname(__file__), 'data'), 'outputs')
source_path = os.path.join(SAMPLE_INPUTS, '1.mp4')
source_audio_path = os.path.join(SAMPLE_INPUTS, '1.mp3')
original_audio_path = os.path.join(SAMPLE_OUTPUTS, 'original.mp3')
background_audio_path = os.path.join(SAMPLE_OUTPUTS, 'background-audio.mp3')
final_audio_path = os.path.join(SAMPLE_OUTPUTS, 'final-audio.mp3')
final_video_path = os.path.join(SAMPLE_OUTPUTS, 'final-video.mp4')


video_clip = VideoFileClip(source_path)
original_audio = video_clip.audio
original_audio = original_audio.volumex(0.10)
# original_audio = original_audio.fx(volumex, 0.10) # adjust volume, 0.5 half audio, 2.0 doubles audio => (0.1, 2.0)
original_audio.write_audiofile(original_audio_path)


background_audio_clip = AudioFileClip(source_audio_path)
background_audio = background_audio_clip.subclip(0, video_clip.duration) # cut audio as original video duration
background_audio = background_audio.volumex(0.10)
# background_audio = background_audio.fx(volumex, 0.10)
background_audio.write_audiofile(background_audio_path)


final_audio = CompositeAudioClip([original_audio, background_audio])
final_audio.write_audiofile(final_audio_path, fps=original_audio.fps)

# # fix if final audio has errors
# new_audio = AudioFileClip(final_audio_path)
# final_video = video_clip.set_audio(new_audio)

final_video = video_clip.set_audio(final_audio)
final_video.write_videofile(final_video_path)

# # fix if final video has coding error
# final_video.write_videofile(final_video_path, codec='libx264', audio_codec='aac')