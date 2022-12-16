import os.path

from moviepy.editor import *

root_dir = 'D:/program/Anansi/'

video_output_dir = os.path.join(root_dir, 'outputs')
image_output_frames_dir = os.path.join(video_output_dir, 'simple_dino_puzzle')
video_output_path = os.path.join(image_output_frames_dir, 'video.mp4')
source_audio_path = os.path.join(image_output_frames_dir, 'audio.mp3')
audio = AudioFileClip(source_audio_path)
frame_rate = 24

image_frames = os.listdir(image_output_frames_dir)
image_frames.sort()
image_frames_paths = [os.path.join(image_output_frames_dir, fname)
                      for fname in image_frames if fname.endswith("jpg")]

# clip_audio = AudioFileClip(audio_background_music_path)

clip = ImageSequenceClip(image_frames_paths, fps=frame_rate)
clip = clip.set_audio(audio)
clip.write_videofile(video_output_path, codec='libx264', audio_codec='aac')
# clip.write_videofile(video_output_path, codec='libx264')
