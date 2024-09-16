# # # Directory containing the MP4 files
# # video_dir = f'{data_dir}/vids/'

# # # Path to the output file
# # output_file = f'{data_dir}/vids/{case_name}.mp4'

# # from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ColorClip, concatenate_videoclips
# # import os
# # import re
# # import json

# # # Load the JSON file
# # with open(f'{data_dir}/{case_name}.json', 'r') as file:
# #     data = json.load(file)

# # justices = {
# #     "JUSTICE ROBERTS": ("CHIEF JUSTICE JOHN G. ROBERTS, JR.", "Appointed by President George W. Bush (2005)"),
# #     "JUSTICE THOMAS": ("ASSOCIATE JUSTICE CLARENCE THOMAS", "Appointed by President George H.W. Bush (1991)"),
# #     "JUSTICE ALITO": ("ASSOCIATE JUSTICE SAMUEL A. ALITO, JR.", "Appointed by President George W. Bush (2006)"),
# #     "JUSTICE SOTOMAYOR": ("ASSOCIATE JUSTICE SONIA SOTOMAYOR", "Appointed by President Barack Obama (2009)"),
# #     "JUSTICE KAGAN": ("ASSOCIATE JUSTICE ELENA KAGAN", "Appointed by President Barack Obama (2010)"),
# #     "JUSTICE GORSUCH": ("ASSOCIATE JUSTICE NEIL M. GORSUCH", "Appointed by President Donald Trump (2017)"),
# #     "JUSTICE KAVANAUGH": ("ASSOCIATE JUSTICE BRETT M. KAVANAUGH", "Appointed by President Donald Trump (2018)"),
# #     "JUSTICE BARRETT": ("ASSOCIATE JUSTICE AMY CONEY BARRETT", "Appointed by President Donald Trump (2020)"),
# #     "JUSTICE JACKSON": ("ASSOCIATE JUSTICE KETANJI BROWN JACKSON", "Appointed by President Joe Biden (2022)"),
# #     "JUSTICE BREYER": ("ASSOCIATE JUSTICE STEPHEN G. BREYER", "Appointed by President Bill Clinton (1994)"),
# #     "JUSTICE SCALIA": ("ASSOCIATE JUSTICE ANTONIN SCALIA", "Appointed by President Ronald Reagan (1986)"),
# #     "JUSTICE KENNEDY": ("ASSOCIATE JUSTICE ANTHONY M. KENNEDY", "Appointed by President Ronald Reagan (1988)"),
# #     "JUSTICE SANDRA DAY O'CONNOR": ("ASSOCIATE JUSTICE SANDRA DAY O'CONNOR", "Appointed by President Ronald Reagan (1981)"),
# #     "JUSTICE RUTH BADER GINSBURG": ("ASSOCIATE JUSTICE RUTH BADER GINSBURG", "Appointed by President Bill Clinton (1993)")
# # }

# # def add_text_overlay(clip, line1, line2, position=('center', 'bottom'), fontsize1=50, fontsize2=30, color='white', bg_color='black', bg_opacity=0.5, display_duration=5):
# #     if clip.duration >= display_duration:
# #         text_clip1 = TextClip(line1, fontsize=fontsize1, color=color, font='Arial-Bold').set_duration(display_duration)
# #         text_clip2 = TextClip(line2, fontsize=fontsize2, color=color, font='Arial-Bold').set_duration(display_duration)

# #         text_w1, text_h1 = text_clip1.size
# #         text_w2, text_h2 = text_clip2.size
# #         bg_width = clip.w
# #         bg_height = text_h1 + text_h2 + 30
# #         bg_clip = ColorClip(size=(bg_width, bg_height), color=(0, 0, 0)).set_opacity(bg_opacity).set_duration(display_duration)

# #         if position[1] == 'bottom':
# #             text_y = clip.h - bg_height - 10
# #         else:
# #             text_y = position[1]

# #         text_clip1 = text_clip1.set_position(('center', text_y + 10))
# #         text_clip2 = text_clip2.set_position(('center', text_y + text_h1 + 20))
# #         bg_clip = bg_clip.set_position((0, text_y))

# #         composite_clip = CompositeVideoClip([clip, bg_clip.set_start(0), text_clip1.set_start(0), text_clip2.set_start(0)])
# #         return composite_clip
# #     else:
# #         return clip

# # import cv2
# # import numpy as np
# # from moviepy.editor import VideoFileClip, ImageSequenceClip

# # background_image = f"{data_dir}/../src/images/bg.png"

# # # Read the background image
# # background = cv2.imread(background_image)
# # if background is None:
# #     raise FileNotFoundError(f"Background image at '{background_image}' not found or cannot be loaded.")

# # # Function to replace the green background
# # def replace_frame_background(frame):
# #     # Convert frame to HSV
# #     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
# #     # Define the range for the green color
# #     lower_green = np.array([35, 100, 100])
# #     upper_green = np.array([85, 255, 255])
    
# #     # Create a mask for the green color
# #     mask = cv2.inRange(hsv, lower_green, upper_green)
    
# #     # Invert the mask
# #     mask_inv = cv2.bitwise_not(mask)
    
# #     # Resize the background to match the frame
# #     bg_resized = cv2.resize(background, (frame.shape[1], frame.shape[0]))
    
# #     # Extract the foreground (subject)
# #     fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
# #     # Extract the background where the green is detected
# #     bg = cv2.bitwise_and(bg_resized, bg_resized, mask=mask)
    
# #     # Combine foreground and new background
# #     combined = cv2.add(fg, bg)
    
# #     return combined

# # def replace_video_background(input_video, output_video):
# #     # Process video frames
# #     clip = VideoFileClip(input_video)
# #     frames = []

# #     for frame in clip.iter_frames():
# #         # Convert the frame from MoviePy to OpenCV format
# #         frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
# #         # Replace the background
# #         frame_with_new_bg = replace_frame_background(frame)
# #         # Convert back to RGB format for MoviePy
# #         frame_with_new_bg = cv2.cvtColor(frame_with_new_bg, cv2.COLOR_BGR2RGB)
# #         frames.append(frame_with_new_bg)

# #     # Create a new video clip with the processed frames
# #     new_clip = ImageSequenceClip(frames, fps=clip.fps)
# #     new_clip.write_videofile(output_video, codec='libx264')


# # def merge_videos_with_transition(video_files, data, transition_duration=1):
# #     clips = []
# #     for file in video_files:
# #         try:
# #             clip = VideoFileClip(os.path.join(video_dir, file))
# #         except OSError as e:
# #             print(f"Error reading {file}: {e}")
# #             continue
# #         #clip = VideoFileClip(os.path.join(video_dir,os.path.join(video_dir,file)))
# #         match = re.search(r'(\d+)', file)
# #         if match:
# #             i = int(match.group(1))
# #         else:
# #             raise ValueError(f"Filename {file} does not contain a valid index")
# #         speaker = data[i]["speaker"]
# #         line1 = speaker

# #         if speaker.startswith("JUSTICE"):
# #             line2 = justices[speaker][1]
# #         else:
# #             line2 = "Lawyer"  # or any appropriate description

# #         print(i)
# #         print(line1)
# #         print(line2)

# #         # If the speaker is not a justice, replace background with Court bg
# #         if speaker.startswith("JUSTICE"):
# #             print("Justice")
# #         else:
# #             replace_video_background(os.path.join(video_dir, file), os.path.join(video_dir, file))

# #         if clip.duration > 10:
# #             clip = add_text_overlay(clip, line1, line2, position=('center', 'bottom'), fontsize1=24, fontsize2=16, color='white', bg_color='black', bg_opacity=0.5, display_duration=8)

# # #        if i > 0:
# # #            gap = float(data[i-1]['gap'])
# # #
# # #            if gap > 2 and len(clips) != 0:
# # #                prev_clip = clips[-1]
# # #                if prev_clip.duration > transition_duration:
# # #                    transition = prev_clip.subclip(prev_clip.duration - transition_duration).crossfadeout(transition_duration)
# # #                    clips[-1] = prev_clip.set_end(prev_clip.duration - transition_duration)
# # #                    clip = transition.set_start(0).crossfadein(transition_duration).set_duration(clip.duration)

# #         clips.append(clip)

# #     final_clip = concatenate_videoclips(clips, method="compose")
# #     return final_clip

# # # Get all video files in the directory and sort them
# # video_files = sorted([f for f in os.listdir(video_dir) if f.endswith('.mp4')],
# #                      key=lambda x: int(re.search(r'(\d+)', os.path.basename(x)).group()))
# # print(video_files)
# # # Merge videos with conditions and transitions
# # final_clip = merge_videos_with_transition(video_files, data['sentences'], transition_duration=1)

# # # Write the final video to a file
# # final_clip.write_videofile(f"{video_dir}/{case_name}_final.mp4", codec="libx264")

# # print("Final video with overlays and transitions created successfully.")

# # -*- coding: utf-8 -*-


# # import os
# # """Supreme Court TV"""

# # case_name = 'case3'
# # data_dir = f'/home/akathpalia/data/{case_name}'

# # # Directory containing the MP4 files
# # video_dir = f'{data_dir}/vids/'

# # if not os.path.exists(data_dir):
# #     raise FileNotFoundError(f"Data directory not found: {data_dir}")

# # if not os.access(data_dir, os.W_OK):
# #     raise PermissionError(f"No write permission for directory: {data_dir}")

# # # Path to the output file
# # output_file = f'{data_dir}/vids/{case_name}_first20.mp4'

# # from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ColorClip, concatenate_videoclips

# # import re
# # import json
# # import cv2
# # import numpy as np
# # from moviepy.editor import VideoFileClip, ImageSequenceClip

# # # Load the JSON file
# # with open(f'{data_dir}/{case_name}.json', 'r') as file:
# #     data = json.load(file)

# # # Limit data to first 20 sentences
# # data['sentences'] = data['sentences'][:20]

# # justices = {
# #     "JUSTICE ROBERTS": ("CHIEF JUSTICE JOHN G. ROBERTS, JR.", "Appointed by President George W. Bush (2005)"),
# #     "JUSTICE THOMAS": ("ASSOCIATE JUSTICE CLARENCE THOMAS", "Appointed by President George H.W. Bush (1991)"),
# #     "JUSTICE ALITO": ("ASSOCIATE JUSTICE SAMUEL A. ALITO, JR.", "Appointed by President George W. Bush (2006)"),
# #     "JUSTICE SOTOMAYOR": ("ASSOCIATE JUSTICE SONIA SOTOMAYOR", "Appointed by President Barack Obama (2009)"),
# #     "JUSTICE KAGAN": ("ASSOCIATE JUSTICE ELENA KAGAN", "Appointed by President Barack Obama (2010)"),
# #     "JUSTICE GORSUCH": ("ASSOCIATE JUSTICE NEIL M. GORSUCH", "Appointed by President Donald Trump (2017)"),
# #     "JUSTICE KAVANAUGH": ("ASSOCIATE JUSTICE BRETT M. KAVANAUGH", "Appointed by President Donald Trump (2018)"),
# #     "JUSTICE BARRETT": ("ASSOCIATE JUSTICE AMY CONEY BARRETT", "Appointed by President Donald Trump (2020)"),
# #     "JUSTICE JACKSON": ("ASSOCIATE JUSTICE KETANJI BROWN JACKSON", "Appointed by President Joe Biden (2022)"),
# #     "JUSTICE BREYER": ("ASSOCIATE JUSTICE STEPHEN G. BREYER", "Appointed by President Bill Clinton (1994)"),
# #     "JUSTICE SCALIA": ("ASSOCIATE JUSTICE ANTONIN SCALIA", "Appointed by President Ronald Reagan (1986)"),
# #     "JUSTICE KENNEDY": ("ASSOCIATE JUSTICE ANTHONY M. KENNEDY", "Appointed by President Ronald Reagan (1988)"),
# #     "JUSTICE SANDRA DAY O'CONNOR": ("ASSOCIATE JUSTICE SANDRA DAY O'CONNOR", "Appointed by President Ronald Reagan (1981)"),
# #     "JUSTICE RUTH BADER GINSBURG": ("ASSOCIATE JUSTICE RUTH BADER GINSBURG", "Appointed by President Bill Clinton (1993)")
# # }

# # def add_text_overlay(clip, line1, line2, position=('center', 'bottom'), fontsize1=50, fontsize2=30, color='white', bg_color='black', bg_opacity=0.5, display_duration=5):
# #     if clip.duration >= display_duration:
# #         text_clip1 = TextClip(line1, fontsize=fontsize1, color=color, font='Arial-Bold').set_duration(display_duration)
# #         text_clip2 = TextClip(line2, fontsize=fontsize2, color=color, font='Arial-Bold').set_duration(display_duration)

# #         text_w1, text_h1 = text_clip1.size
# #         text_w2, text_h2 = text_clip2.size
# #         bg_width = clip.w
# #         bg_height = text_h1 + text_h2 + 30
# #         bg_clip = ColorClip(size=(bg_width, bg_height), color=(0, 0, 0)).set_opacity(bg_opacity).set_duration(display_duration)

# #         if position[1] == 'bottom':
# #             text_y = clip.h - bg_height - 10
# #         else:
# #             text_y = position[1]

# #         text_clip1 = text_clip1.set_position(('center', text_y + 10))
# #         text_clip2 = text_clip2.set_position(('center', text_y + text_h1 + 20))
# #         bg_clip = bg_clip.set_position((0, text_y))

# #         composite_clip = CompositeVideoClip([clip, bg_clip.set_start(0), text_clip1.set_start(0), text_clip2.set_start(0)])
# #         return composite_clip
# #     else:
# #         return clip

# # background_image = f"{data_dir}/../src/images/bg.png"

# # # Read the background image
# # background = cv2.imread(background_image)
# # if background is None:
# #     raise FileNotFoundError(f"Background image at '{background_image}' not found or cannot be loaded.")

# # # Function to replace the green background
# # def replace_frame_background(frame):
# #     # Convert frame to HSV
# #     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
# #     # Define the range for the green color
# #     lower_green = np.array([35, 100, 100])
# #     upper_green = np.array([85, 255, 255])
    
# #     # Create a mask for the green color
# #     mask = cv2.inRange(hsv, lower_green, upper_green)
    
# #     # Invert the mask
# #     mask_inv = cv2.bitwise_not(mask)
    
# #     # Resize the background to match the frame
# #     bg_resized = cv2.resize(background, (frame.shape[1], frame.shape[0]))
    
# #     # Extract the foreground (subject)
# #     fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
# #     # Extract the background where the green is detected
# #     bg = cv2.bitwise_and(bg_resized, bg_resized, mask=mask)
    
# #     # Combine foreground and new background
# #     combined = cv2.add(fg, bg)
    
# #     return combined

# # def replace_video_background(input_video, output_video):
# #     # Process video frames
# #     clip = VideoFileClip(input_video)
# #     frames = []

# #     for frame in clip.iter_frames():
# #         # Convert the frame from MoviePy to OpenCV format
# #         frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
# #         # Replace the background
# #         frame_with_new_bg = replace_frame_background(frame)
# #         # Convert back to RGB format for MoviePy
# #         frame_with_new_bg = cv2.cvtColor(frame_with_new_bg, cv2.COLOR_BGR2RGB)
# #         frames.append(frame_with_new_bg)

# #     # Create a new video clip with the processed frames
# #     new_clip = ImageSequenceClip(frames, fps=clip.fps)
# #     new_clip.write_videofile(output_video, codec='libx264')


# # def merge_videos_with_transition(video_files, data, transition_duration=1):
# #     clips = []
# #     for file in video_files:
# #         try:
# #             clip = VideoFileClip(os.path.join(video_dir, file))
# #         except OSError as e:
# #             print(f"Error reading {file}: {e}")
# #             continue
# #         match = re.search(r'(\d+)', file)
# #         if match:
# #             i = int(match.group(1)) - 1  # Subtract 1 to match 0-based index of data['sentences']
# #         else:
# #             raise ValueError(f"Filename {file} does not contain a valid index")
# #         speaker = data[i]["speaker"]
# #         line1 = speaker

# #         if speaker.startswith("JUSTICE"):
# #             line2 = justices[speaker][1]
# #         else:
# #             line2 = "Lawyer"  # or any appropriate description

# #         print(i)
# #         print(line1)
# #         print(line2)

# #         # If the speaker is not a justice, replace background with Court bg
# #         if speaker.startswith("JUSTICE"):
# #             print("Justice")
# #         else:
# #             replace_video_background(os.path.join(video_dir, file), os.path.join(video_dir, file))

# #         if clip.duration > 10:
# #             clip = add_text_overlay(clip, line1, line2, position=('center', 'bottom'), fontsize1=24, fontsize2=16, color='white', bg_color='black', bg_opacity=0.5, display_duration=8)

# #         clips.append(clip)

# #     final_clip = concatenate_videoclips(clips, method="compose")
# #     return final_clip

# # # Get all video files in the directory and sort them
# # video_files = sorted([f for f in os.listdir(video_dir) if f.endswith('.mp4')],
# #                      key=lambda x: int(re.search(r'(\d+)', os.path.basename(x)).group()))[:20]  # Limit to first 20 files
# # print(video_files)

# # # Merge videos with conditions and transitions
# # final_clip = merge_videos_with_transition(video_files, data['sentences'], transition_duration=1)

# # # Write the final video to a file
# # final_clip.write_videofile(output_file, codec="libx264")

# # print("Final video with overlays and transitions created successfully.")

# # -*- coding: utf-8 -*-
# """Supreme Court TV"""

# import os
# import re
# import json
# import cv2
# import numpy as np
# from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ColorClip, concatenate_videoclips, ImageSequenceClip

# def print_system_info():
#     import psutil
#     print(f"Memory usage: {psutil.virtual_memory().percent}%")
#     print(f"CPU usage: {psutil.cpu_percent()}%")
#     print(f"Disk usage: {psutil.disk_usage('/').percent}%")

# print("Script started")
# print_system_info()

# case_name = 'case3'
# data_dir = f'/home/akathpalia/data/{case_name}'
# video_dir = f'{data_dir}/vids/'
# output_file = f'{data_dir}/vids/{case_name}_first20.mp4'

# print(f"Processing case: {case_name}")
# print(f"Data directory: {data_dir}")
# print(f"Video directory: {video_dir}")
# print(f"Output file: {output_file}")

# # Load the JSON file
# print("Loading JSON data...")
# with open(f'{data_dir}/{case_name}.json', 'r') as file:
#     data = json.load(file)

# # Limit data to first 20 sentences
# data['sentences'] = data['sentences'][:20]
# print(f"Limited to first 20 sentences. Total sentences: {len(data['sentences'])}")

# justices = {
#     "JUSTICE ROBERTS": ("CHIEF JUSTICE JOHN G. ROBERTS, JR.", "Appointed by President George W. Bush (2005)"),
#     "JUSTICE THOMAS": ("ASSOCIATE JUSTICE CLARENCE THOMAS", "Appointed by President George H.W. Bush (1991)"),
#     "JUSTICE ALITO": ("ASSOCIATE JUSTICE SAMUEL A. ALITO, JR.", "Appointed by President George W. Bush (2006)"),
#     "JUSTICE SOTOMAYOR": ("ASSOCIATE JUSTICE SONIA SOTOMAYOR", "Appointed by President Barack Obama (2009)"),
#     "JUSTICE KAGAN": ("ASSOCIATE JUSTICE ELENA KAGAN", "Appointed by President Barack Obama (2010)"),
#     "JUSTICE GORSUCH": ("ASSOCIATE JUSTICE NEIL M. GORSUCH", "Appointed by President Donald Trump (2017)"),
#     "JUSTICE KAVANAUGH": ("ASSOCIATE JUSTICE BRETT M. KAVANAUGH", "Appointed by President Donald Trump (2018)"),
#     "JUSTICE BARRETT": ("ASSOCIATE JUSTICE AMY CONEY BARRETT", "Appointed by President Donald Trump (2020)"),
#     "JUSTICE JACKSON": ("ASSOCIATE JUSTICE KETANJI BROWN JACKSON", "Appointed by President Joe Biden (2022)"),
#     "JUSTICE BREYER": ("ASSOCIATE JUSTICE STEPHEN G. BREYER", "Appointed by President Bill Clinton (1994)"),
#     "JUSTICE SCALIA": ("ASSOCIATE JUSTICE ANTONIN SCALIA", "Appointed by President Ronald Reagan (1986)"),
#     "JUSTICE KENNEDY": ("ASSOCIATE JUSTICE ANTHONY M. KENNEDY", "Appointed by President Ronald Reagan (1988)"),
#     "JUSTICE SANDRA DAY O'CONNOR": ("ASSOCIATE JUSTICE SANDRA DAY O'CONNOR", "Appointed by President Ronald Reagan (1981)"),
#     "JUSTICE RUTH BADER GINSBURG": ("ASSOCIATE JUSTICE RUTH BADER GINSBURG", "Appointed by President Bill Clinton (1993)")
# }

# def add_text_overlay(clip, line1, line2, position=('center', 'bottom'), fontsize1=50, fontsize2=30, color='white', bg_color='black', bg_opacity=0.5, display_duration=5):
#     print(f"Adding text overlay: {line1}, {line2}")
#     if clip.duration >= display_duration:
#         text_clip1 = TextClip(line1, fontsize=fontsize1, color=color, font='Arial-Bold').set_duration(display_duration)
#         text_clip2 = TextClip(line2, fontsize=fontsize2, color=color, font='Arial-Bold').set_duration(display_duration)

#         text_w1, text_h1 = text_clip1.size
#         text_w2, text_h2 = text_clip2.size
#         bg_width = clip.w
#         bg_height = text_h1 + text_h2 + 30
#         bg_clip = ColorClip(size=(bg_width, bg_height), color=(0, 0, 0)).set_opacity(bg_opacity).set_duration(display_duration)

#         if position[1] == 'bottom':
#             text_y = clip.h - bg_height - 10
#         else:
#             text_y = position[1]

#         text_clip1 = text_clip1.set_position(('center', text_y + 10))
#         text_clip2 = text_clip2.set_position(('center', text_y + text_h1 + 20))
#         bg_clip = bg_clip.set_position((0, text_y))

#         composite_clip = CompositeVideoClip([clip, bg_clip.set_start(0), text_clip1.set_start(0), text_clip2.set_start(0)])
#         return composite_clip
#     else:
#         return clip

# print("Loading background image...")
# background_image = f"{data_dir}/../src/images/bg.png"
# background = cv2.imread(background_image)
# if background is None:
#     print(f"Error: Background image at '{background_image}' not found or cannot be loaded.")
#     raise FileNotFoundError(f"Background image at '{background_image}' not found or cannot be loaded.")

# def replace_frame_background(frame):
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     lower_green = np.array([35, 100, 100])
#     upper_green = np.array([85, 255, 255])
#     mask = cv2.inRange(hsv, lower_green, upper_green)
#     mask_inv = cv2.bitwise_not(mask)
#     bg_resized = cv2.resize(background, (frame.shape[1], frame.shape[0]))
#     fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
#     bg = cv2.bitwise_and(bg_resized, bg_resized, mask=mask)
#     combined = cv2.add(fg, bg)
#     return combined

# def replace_video_background(input_video, output_video):
#     print(f"Replacing background for video: {input_video}")
#     clip = VideoFileClip(input_video)
#     frames = []

#     for i, frame in enumerate(clip.iter_frames()):
#         if i % 100 == 0:
#             print(f"Processing frame {i} of video {input_video}")
#         frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
#         frame_with_new_bg = replace_frame_background(frame)
#         frame_with_new_bg = cv2.cvtColor(frame_with_new_bg, cv2.COLOR_BGR2RGB)
#         frames.append(frame_with_new_bg)

#     new_clip = ImageSequenceClip(frames, fps=clip.fps)
#     new_clip.write_videofile(output_video, codec='libx264')
#     print(f"Background replaced for video: {input_video}")

# def merge_videos_with_transition(video_files, data, transition_duration=1):
#     print("Starting to merge videos...")
#     clips = []
#     for i, file in enumerate(video_files):
#         print(f"Processing video {i+1}/{len(video_files)}: {file}")
#         try:
#             clip = VideoFileClip(os.path.join(video_dir, file))
#             match = re.search(r'(\d+)', file)
#             if match:
#                 j = int(match.group(1)) - 1
#             else:
#                 raise ValueError(f"Filename {file} does not contain a valid index")
#             speaker = data[j]["speaker"]
#             line1 = speaker

#             if speaker.startswith("JUSTICE"):
#                 line2 = justices[speaker][1]
#             else:
#                 line2 = "Lawyer"

#             print(f"Speaker: {line1}, Info: {line2}")

#             if not speaker.startswith("JUSTICE"):
#                 replace_video_background(os.path.join(video_dir, file), os.path.join(video_dir, file))

#             if clip.duration > 10:
#                 clip = add_text_overlay(clip, line1, line2, position=('center', 'bottom'), fontsize1=24, fontsize2=16, color='white', bg_color='black', bg_opacity=0.5, display_duration=8)

#             clips.append(clip)
#             print(f"Video {i+1} processed successfully")
#         except Exception as e:
#             print(f"Error processing video {file}: {str(e)}")
#         print_system_info()

#     print("All individual videos processed. Starting concatenation.")
#     final_clip = concatenate_videoclips(clips, method="compose")
#     print("Concatenation completed")
#     return final_clip

# print("Getting video files...")
# video_files = sorted([f for f in os.listdir(video_dir) if f.endswith('.mp4')],
#                      key=lambda x: int(re.search(r'(\d+)', os.path.basename(x)).group()))[:20]
# print(f"Video files to process: {video_files}")

# print("Merging videos...")
# final_clip = merge_videos_with_transition(video_files, data['sentences'], transition_duration=1)

# print("Writing final video...")
# print_system_info()
# try:
#     final_clip.write_videofile(output_file, codec="libx264")
#     print(f"Final video written successfully to {output_file}")
# except Exception as e:
#     print(f"Error writing final video: {str(e)}")

# print("Script completed")
# print_system_info()

#--------------- New Script -------------#

# Imports
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ColorClip, concatenate_videoclips, ImageSequenceClip
from config import case_name, data_dir, video_dir, output_dir, output_file, background, background_video
import os
import re
import json
import cv2
import numpy as np

with open(f'{data_dir}/{case_name}.json', 'r') as file:
    data = json.load(file)

justices = {
    "JUSTICE ROBERTS": ("CHIEF JUSTICE JOHN G. ROBERTS, JR.", "Appointed by President George W. Bush (2005)"),
    "JUSTICE THOMAS": ("ASSOCIATE JUSTICE CLARENCE THOMAS", "Appointed by President George H.W. Bush (1991)"),
    "JUSTICE ALITO": ("ASSOCIATE JUSTICE SAMUEL A. ALITO, JR.", "Appointed by President George W. Bush (2006)"),
    "JUSTICE SOTOMAYOR": ("ASSOCIATE JUSTICE SONIA SOTOMAYOR", "Appointed by President Barack Obama (2009)"),
    "JUSTICE KAGAN": ("ASSOCIATE JUSTICE ELENA KAGAN", "Appointed by President Barack Obama (2010)"),
    "JUSTICE GORSUCH": ("ASSOCIATE JUSTICE NEIL M. GORSUCH", "Appointed by President Donald Trump (2017)"),
    "JUSTICE KAVANAUGH": ("ASSOCIATE JUSTICE BRETT M. KAVANAUGH", "Appointed by President Donald Trump (2018)"),
    "JUSTICE BARRETT": ("ASSOCIATE JUSTICE AMY CONEY BARRETT", "Appointed by President Donald Trump (2020)"),
    "JUSTICE JACKSON": ("ASSOCIATE JUSTICE KETANJI BROWN JACKSON", "Appointed by President Joe Biden (2022)"),
    "JUSTICE BREYER": ("ASSOCIATE JUSTICE STEPHEN G. BREYER", "Appointed by President Bill Clinton (1994)"),
    "JUSTICE SCALIA": ("ASSOCIATE JUSTICE ANTONIN SCALIA", "Appointed by President Ronald Reagan (1986)"),
    "JUSTICE KENNEDY": ("ASSOCIATE JUSTICE ANTHONY M. KENNEDY", "Appointed by President Ronald Reagan (1988)"),
    "JUSTICE SANDRA DAY O'CONNOR": ("ASSOCIATE JUSTICE SANDRA DAY O'CONNOR", "Appointed by President Ronald Reagan (1981)"),
    "JUSTICE RUTH BADER GINSBURG": ("ASSOCIATE JUSTICE RUTH BADER GINSBURG", "Appointed by President Bill Clinton (1993)")
}

# Methods
def add_text_overlay(clip, line1, line2, position=('center', 'bottom'), fontsize1=50, fontsize2=30, color='white', bg_color='black', bg_opacity=0.5, display_duration=5):
    print(f"Adding text overlay: {line1}, {line2}")
    if clip.duration >= display_duration:
        print(f"Adding text: {line1}")
        text_clip1 = TextClip(line1, fontsize=fontsize1, color=color, font="DejaVu-Sans").set_duration(display_duration)
        print("Text clip 1 generated")
        print(f"Adding text: {line2}")
        text_clip2 = TextClip(line2, fontsize=fontsize2, color=color, font="DejaVu-Sans").set_duration(display_duration)
        print("Text clips generated")

        text_w1, text_h1 = text_clip1.size
        text_w2, text_h2 = text_clip2.size
        bg_width = clip.w
        bg_height = text_h1 + text_h2 + 30
        bg_clip = ColorClip(size=(bg_width, bg_height), color=(0, 0, 0)).set_opacity(bg_opacity).set_duration(display_duration)

        if position[1] == 'bottom':
            text_y = clip.h - bg_height - 10
        else:
            text_y = position[1]

        text_clip1 = text_clip1.set_position(('center', text_y + 10))
        text_clip2 = text_clip2.set_position(('center', text_y + text_h1 + 20))
        bg_clip = bg_clip.set_position((0, text_y))

        composite_clip = CompositeVideoClip([clip, bg_clip.set_start(0), text_clip1.set_start(0), text_clip2.set_start(0)])
        return composite_clip
    else:
        return clip

# ------ Replace with video----------- #


def replace_green_screen(frame, background):
    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define range for green color in HSV
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])
    
    # Create a mask for green color
    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    # Invert the mask
    mask_inv = cv2.bitwise_not(mask)
    
    # Use the mask to extract the foreground
    foreground = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
    # Use the inverted mask to extract the background
    background_area = cv2.bitwise_and(background, background, mask=mask)
    
    # Combine foreground and background
    result = cv2.add(foreground, background_area)
    
    return result

def process_video(input_video, background_video, output_video):
    # Load the input video
    clip = VideoFileClip(input_video)
    
    # Load the background video and loop it if necessary
    bg_clip = VideoFileClip(background_video).loop(duration=clip.duration)
    
    # Ensure background video has the same size as the input video
    bg_clip = bg_clip.resize(clip.size)
    
    # Process each frame
    def process_frame(get_frame, t):
        frame = get_frame(t)
        bg_frame = bg_clip.get_frame(t)
        return replace_green_screen(frame, bg_frame)
    
    # Apply the processing to each frame
    final_clip = clip.fl(process_frame)

    return final_clip

# Usage
input_video = f"{video_dir}/3.mp4"
output_video = f"{output_dir}/output_video_bg_replaced.mp4"

process_video(input_video, background_video, output_video)

def merge_videos_with_transition(video_files, data, transition_duration=1):
    clips = []
    n = 0
    custom_resolution = (1920, 1080)
    for file in video_files:
        # if n > 20:
        #     break
        try:
            clip = VideoFileClip(os.path.join(video_dir, file))
        except OSError as e:
            print(f"Error reading {file}: {e}")
            n += 1
            continue
        match = re.search(r'(\d+)', file)
        if match:
            i = int(match.group(1))
        else:
            raise ValueError(f"Filename {file} does not contain a valid index")
        speaker = data[i]["speaker"]
        line1 = speaker

        if speaker.startswith("JUSTICE"):
            line2 = justices[speaker][1]
        else:
            line2 = "Lawyer"

        print(i)
        print(line1)
        print(line2)

        # If the speaker is not a justice, replace background with Court bg
        if speaker.startswith("JUSTICE"):
            print("Justice")
        else:
            input_video = os.path.join(video_dir, file)
            output_video = os.path.join(video_dir, file)
            clip = process_video(input_video, background_video, output_video)
            # replace_video_background(os.path.join(video_dir, file), os.path.join(video_dir, file))

        if clip.duration > 10:
            clip = add_text_overlay(clip, line1, line2, position=('center', 'bottom'), fontsize1=24, fontsize2=16, color='white', bg_color='black', bg_opacity=0.5, display_duration=8)

        clips.append(clip.resize(newsize=custom_resolution))
        n += 1

    final_clip = concatenate_videoclips(clips, method="compose")
    return final_clip

# Get all video files in the directory and sort them
video_files = sorted([f for f in os.listdir(video_dir) if f.endswith('.mp4')],
                     key=lambda x: int(re.search(r'(\d+)', os.path.basename(x)).group()))
print(video_files)
final_clip = merge_videos_with_transition(video_files, data['sentences'], transition_duration=1)
final_clip.write_videofile(f"{output_file}", codec="libx264")

print("Final video with overlays and transitions created successfully.")