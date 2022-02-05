from pytube import YouTube, Playlist
import os

url = input('Paste Youtube Video URL: ')
video = YouTube(url)
video.streams.get_highest_resolution().download(output_path=os.path.dirname(os.path.abspath(__file__)))

def downloading():
  print('Download In Progress!')
video.register_on_progress_callback(downloading())

def finish():
  print('Download Completed Successfully!')
video.register_on_complete_callback(finish())


playlist_url = input('Paste Youtube Playlist URL: ')
playlist = Playlist(playlist_url)
print(f'Playlist title : {playlist.title}, List has {len(playlist)} Video.')

for video in playlist.videos:
  video.streams.get_highest_resolution().download(output_path=os.path.dirname(os.path.abspath(__file__)))
  # print(f'Video Title: {video.title}, Length is: {video.length/60:.3} Minutes, Video URL: {video.watch_url}, Channel URL: {video.channel_url}')