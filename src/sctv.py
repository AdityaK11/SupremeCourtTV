# # -*- coding: utf-8 -*-
# """Supreme Court TV"""

from config import case_name, data_dir, video_dir, output_dir, output_file, background

# # """# Match original transcript with audio transcript"""
# # import fitz  # PyMuPDF
# # import re

# # doc = fitz.open(f'{data_dir}/{case_name}.pdf')
# # proceedings_found = False
# # end_of_case_found = False  # Flag to check if end marker has been found

# # transcript_text = ""

# # with open(f'{data_dir}/cleaned_transcript.txt', 'w') as output_file:
# #   for page in doc:
# #       if not end_of_case_found:
# #           text = page.get_text("text")
# #           # Check for "PROCEEDINGS" if not found in previous pages
# #           if not proceedings_found:
# #               proceedings_index = text.find("P R O C E E D I N G S")
# #               if proceedings_index != -1:
# #                   proceedings_found = True
# #                   text = text[proceedings_index:]  # Start text extraction from "PROCEEDINGS"

# #           if proceedings_found:
# #               # Remove line numbers, specific phrases, and clean up text
# #               cleaned_text = re.sub(r'^\d+\s*', '', text, flags=re.MULTILINE)
# #               cleaned_text = re.sub(r'Heritage Reporting Corporation\s*', '', cleaned_text)
# #               cleaned_text = re.sub(r'Official - Subject to Final Review\s*', '', cleaned_text)
# #               cleaned_text = re.sub(r'\n+', ' ', cleaned_text)
# #               cleaned_text = re.sub(r'\s{2,}', ' ', cleaned_text)
# #               cleaned_text = re.sub(r'-- |- ', '', cleaned_text)
# #               cleaned_text = re.sub(r'CHIEF ', '', cleaned_text)
# #               cleaned_text = re.sub(r' (?=(CHIEF JUSTICE|JUSTICE|MR\.|MS\.|DR\.|GENERAL) [A-Z]+:)', '\n', cleaned_text)

# #               # Check for the end of the case marker and truncate if found
# #               marker_regex = r'\(Whereupon, at \d+:\d+ [ap]\.m\., the case was submitted\.\)'
# #               if re.search(marker_regex, cleaned_text):
# #                   cleaned_text, _ = re.split(marker_regex, cleaned_text, maxsplit=1)
# #                   end_of_case_found = True  # Set flag to stop processing further pages

# #               print(cleaned_text)
# #               transcript_text += cleaned_text + '\n'
# #               output_file.write(cleaned_text + '\n')
# #       else:
# #           break  # Stop processing remaining pages once the end marker is found

# # import json
# # import re
# # import numpy as np

# # # Load JSON data
# # def load_json_data(filepath):
# #     with open(filepath, 'r') as file:
# #         data = json.load(file)
# #     return data['words']


# # def filter_transcript(transcript_text):
# #     filtered_text = ""
# #     # Regular expression to identify and remove speaker labels
# #     pattern = r"([A-Z ]+):\s*(.*?)\s*(?=[A-Z ]+:|$)"
# #     # Remove the patterns
# #     temp = re.findall(pattern, transcript_text, re.DOTALL)
# #     for speaker, segment in temp:
# #         filtered_text += segment

# #     return filtered_text

# # def parse_transcript(transcript_text):
# #     pattern = r"((?:CHIEF JUSTICE|JUSTICE|MR\.|MS\.|DR\.|GENERAL) [A-Z]+):\s*(.*?)\s*(?=(?:CHIEF JUSTICE|JUSTICE|MR\.|MS\.|DR\.|GENERAL) [A-Z]+:|$)"
# #     return re.findall(pattern, transcript_text, re.DOTALL)

# # def print_unique_speakers(transcript_text):
# #     # Extract speaker segments
# #     segments = parse_transcript(transcript_text)
# #     # Create a set to store unique speakers
# #     unique_speakers = set()
# #     # Loop through the segments to add speakers to the set
# #     for speaker, _ in segments:
# #         unique_speakers.add(speaker.strip())

# #     # Print the list of unique speakers
# #     print("List of Unique Speakers:")
# #     for speaker in sorted(unique_speakers):  # Sorting for display purposes
# #         print(speaker)


# # # Align words from JSON with the transcript using a simple scoring mechanism
# # def align_transcript(words, transcript_tokens):
# #     # Create a matrix for dynamic programming
# #     len_words = len(words)
# #     len_tokens = len(transcript_tokens)
# #     scores = np.zeros((len_words + 1, len_tokens + 1), dtype=int)

# #     # Initialize the matrix for alignment
# #     for i in range(1, len_words + 1):
# #         scores[i][0] = i * -1
# #     for j in range(1, len_tokens + 1):
# #         scores[0][j] = j * -1

# #     # Fill the matrix based on alignment scores
# #     for i in range(1, len_words + 1):
# #         for j in range(1, len_tokens + 1):
# #             match_score = scores[i-1][j-1] + (1 if words[i-1]['word'] == transcript_tokens[j-1] else -1)
# #             delete_score = scores[i-1][j] - 1
# #             insert_score = scores[i][j-1] - 1
# #             scores[i][j] = max(match_score, delete_score, insert_score)

# #     # Trace back to find the alignment
# #     i, j = len_words, len_tokens
# #     aligned_pairs = []
# #     while i > 0 and j > 0:
# #         if scores[i][j] == scores[i-1][j-1] + (1 if words[i-1]['word'] == transcript_tokens[j-1] else -1):
# #             aligned_pairs.append((words[i-1], transcript_tokens[j-1], i-1, j-1))
# #             i -= 1
# #             j -= 1
# #         elif scores[i][j] == scores[i-1][j] - 1:
# #             i -= 1
# #         else:
# #             j -= 1

# #     aligned_pairs.reverse()
# #     return aligned_pairs

# # # Load output from nemo
# # json_filepath = f'{data_dir}/modified_{case_name}.json'

# # # Tokenize the transcript
# # segments = parse_transcript(transcript_text)
# # transcript_tokens = []
# # for speaker, segment in segments:
# #     transcript_tokens += re.findall(r'\w+', segment.lower())

# # # Align original and generated transcript
# # words = load_json_data(json_filepath)
# # aligned_words = align_transcript(words, transcript_tokens)

# # # Save aligned_words in a json format
# # def convert_to_serializable_format(aligned_pairs):
# #     serialized_data = []
# #     for word_info, token, word_idx, token_idx in aligned_pairs:
# #         serialized_data.append({
# #             "audio_word": word_info['word'],
# #             "transcript_token": token,
# #             "audio_word_idx": word_idx,
# #             "transcript_token_idx": token_idx,
# #             "start_time": word_info['start_time'],
# #             "end_time": word_info['end_time'],
# #         })
# #     return serialized_data

# # def dump_to_json_file(data, filename):
# #     with open(filename, 'w') as file:
# #         json.dump(data, file, indent=4)

# # # Convert aligned words to a serializable format
# # serializable_data = convert_to_serializable_format(aligned_words)

# # # Dump to JSON file
# # output_filename = f'{data_dir}/aligned_words.json'
# # dump_to_json_file(serializable_data, output_filename)

# # print(f"Aligned words have been saved to {output_filename}")

# # def generate_json(filepath, transcript_text):
# #     words = load_json_data(filepath)
# #     segments = parse_transcript(transcript_text)

# #     with open(f'{data_dir}/aligned_words.json', 'r') as file:
# #         aligned_words_from_json = json.load(file)
# #     results = []


# #     # Index in aligned words json
# #     current_word_index = 0

# #     # Index to get where current segment ends
# #     idx_count = 0

# #     for speaker, segment in segments:
# #         segment_tokens = re.findall(r'\w+', segment.lower())
# #         idx_count += len(segment_tokens)
# #         start_time = aligned_words_from_json[current_word_index]['start_time'] if current_word_index < len(aligned_words) else None
# #         end_time = None

        
# #         for token in segment_tokens:
# #             if (current_word_index < len(aligned_words_from_json) and
# #                aligned_words_from_json[current_word_index]['transcript_token_idx'] < idx_count):
# #                 end_time = aligned_words_from_json[current_word_index]['end_time']
# #                 current_word_index += 1

# #         if start_time is not None and end_time is not None:
# #             results.append({
# #                 "speaker": speaker.strip(),
# #                 "start_time": start_time,
# #                 "end_time": end_time,
# #                 "duration": end_time - start_time,
# #             })

# #     for j in range(len(results) - 1):
# #         results[j]['gap'] = float(results[j + 1]['start_time']) - float(results[j]['end_time'])

# #     return {"sentences": results}

# # # Save the final JSON output to words.json
# # json_output = generate_json(json_filepath, transcript_text)

# # output_file_path = f'{data_dir}/{case_name}.json'

# # # Write the JSON output to the file
# # with open(output_file_path, 'w') as json_file:
# #     json.dump(json_output, json_file, indent=4)

# # """ Split audio
# # We have the JSON with sentences, speaker of the sentence, timestamp of start and end of audio. Now we want to split the audio into smaller clips based on these timestamps. And store them numbered
# # """

# # import json
# # from pydub import AudioSegment
# # import os

# # # Create a directory to store the audios
# # os.makedirs(f'{data_dir}/audio/', exist_ok=True)

# # # Load the JSON file
# # with open(f'{data_dir}/{case_name}.json', 'r') as file:
# #     data = json.load(file)

# # # Load the audio file
# # audio = AudioSegment.from_wav(f"{data_dir}/{case_name}.wav")

# # # Split the audio based on the timestamps and export
# # for i, sentence in enumerate(data['sentences']):
# #     t1 = int(sentence['start_time'] * 1000)  # Start time in milliseconds
# #     t2 = int(sentence['end_time'] * 1000)    # End time in milliseconds
# #     new_audio = audio[t1:t2]
# #     new_audio.export(f'{data_dir}/audio/{i+1}.wav', format='wav')

# # print("Audio split and saved successfully.")

"""# Generate Videos using SadTalker"""

# Link speaker to people ID - A classs storing all the information on People including the photos

# Iterate over the sentences and generate videos
# for i, sentence in enumerate(data['sentences']):

#    speaker = sentence['speaker']
#    if(i<168 and speaker != 'ROBERTS'):
#        continue

#    audio_file = f'{data_dir}/audio/{i+1}.wav'
#    source_image = speaker_images[speaker]
#    result_dir = f'{data_dir}/vids/'

#    command = [
#        "python3.8", f"{data_dir}/../SadTalker/inference.py",
#        "--driven_audio", audio_file,
#        "--source_image", source_image,
#        "--result_dir", result_dir,
#        "--checkpoint_dir", f"{data_dir}/../SadTalker/checkpoints",
#        "--still", "--preprocess", "full", "--enhancer", "gfpgan"
#    ]

#     Run the command
#    subprocess.run(command, check=True)

# print("Videos generated successfully.")

import json
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load the JSON file
with open(f'{data_dir}/{case_name}.json', 'r') as file:
    data = json.load(file)

# Initialize image counters
male_counter = 1
female_counter = 1

# Dictionary mapping speaker names to their corresponding image paths
speaker_images = {}

def get_speaker_image(speaker):
    global male_counter, female_counter
    if speaker.startswith('JUSTICE'):
        return f'src/images/{speaker.lower().replace(" ", "_")}.png'
    elif speaker.startswith('MR.'):
        image_path = f'src/images/male{male_counter}.png'
        male_counter += 1
        return image_path
    elif speaker.startswith('MS.'):
        image_path = f'src/images/female{female_counter}.png'
        female_counter += 1
        return image_path
    elif speaker.startswith('GENERAL'):
        image_path = f'src/images/general.png'
        return image_path
    else:
        return f'src/images/prosecutor.png'

# Assign unique images to each speaker
for sentence in data['sentences']:
    speaker = sentence['speaker']
    if speaker not in speaker_images:
        speaker_images[speaker] = get_speaker_image(speaker)

# Create a directory to store the videos
os.makedirs(f'{video_dir}/', exist_ok=True)

def generate_video(sentence_data):
    i, sentence = sentence_data
    speaker = sentence['speaker']
    audio_file = f'{data_dir}/audio/{i+1}.wav'
    source_image = speaker_images[speaker]
    result_dir = f'{video_dir}/'

    command = [
        "python3.8", f"{data_dir}/../SadTalker/inference.py",
        "--driven_audio", audio_file,
        "--source_image", source_image,
        "--result_dir", result_dir,
        "--checkpoint_dir", f"{data_dir}/../SadTalker/checkpoints",
        "--still", "--preprocess", "full", "--enhancer", "gfpgan",
        "--iteration", str(i),
    ]

    subprocess.run(command, check=True)
    return f"Video {i} generated successfully."

# Using ThreadPoolExecutor to manage multiple threads
with ThreadPoolExecutor(max_workers=4) as executor:  # Adjust max_workers based on your hardware
    futures = [executor.submit(generate_video, (i, sentence)) for i, sentence in enumerate(data['sentences'])]
    for future in as_completed(futures):
        try:
            result = future.result()
            print(result)
        except Exception as e:
            print(f"Exception occured: {e}")

# from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ColorClip, concatenate_videoclips
# import os
# import re
# import json

# # Load the JSON file
# with open(f'{data_dir}/{case_name}.json', 'r') as file:
#     data = json.load(file)

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

# import cv2
# import numpy as np
# from moviepy.editor import VideoFileClip, ImageSequenceClip

# background_image = f"{data_dir}/../src/images/bg.png"

# # Read the background image
# background = cv2.imread(background_image)
# if background is None:
#     raise FileNotFoundError(f"Background image at '{background_image}' not found or cannot be loaded.")

# # Function to replace the green background
# def replace_frame_background(frame):
#     # Convert frame to HSV
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
#     # Define the range for the green color
#     lower_green = np.array([35, 100, 100])
#     upper_green = np.array([85, 255, 255])
    
#     # Create a mask for the green color
#     mask = cv2.inRange(hsv, lower_green, upper_green)
    
#     # Invert the mask
#     mask_inv = cv2.bitwise_not(mask)
    
#     # Resize the background to match the frame
#     bg_resized = cv2.resize(background, (frame.shape[1], frame.shape[0]))
    
#     # Extract the foreground (subject)
#     fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
#     # Extract the background where the green is detected
#     bg = cv2.bitwise_and(bg_resized, bg_resized, mask=mask)
    
#     # Combine foreground and new background
#     combined = cv2.add(fg, bg)
    
#     return combined

# def replace_video_background(input_video, output_video):
#     # Process video frames
#     clip = VideoFileClip(input_video)
#     frames = []

#     for frame in clip.iter_frames():
#         # Convert the frame from MoviePy to OpenCV format
#         frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
#         # Replace the background
#         frame_with_new_bg = replace_frame_background(frame)
#         # Convert back to RGB format for MoviePy
#         frame_with_new_bg = cv2.cvtColor(frame_with_new_bg, cv2.COLOR_BGR2RGB)
#         frames.append(frame_with_new_bg)

#     # Create a new video clip with the processed frames
#     new_clip = ImageSequenceClip(frames, fps=clip.fps)
#     new_clip.write_videofile(output_video, codec='libx264')


# def merge_videos_with_transition(video_files, data, transition_duration=1):
#     clips = []
#     for file in video_files:
#         try:
#             clip = VideoFileClip(os.path.join(video_dir, file))
#         except OSError as e:
#             print(f"Error reading {file}: {e}")
#             continue
#         #clip = VideoFileClip(os.path.join(video_dir,os.path.join(video_dir,file)))
#         match = re.search(r'(\d+)', file)
#         if match:
#             i = int(match.group(1))
#         else:
#             raise ValueError(f"Filename {file} does not contain a valid index")
#         speaker = data[i]["speaker"]
#         line1 = speaker

#         if speaker.startswith("JUSTICE"):
#             line2 = justices[speaker][1]
#         else:
#             line2 = "Lawyer"  # or any appropriate description

#         print(i)
#         print(line1)
#         print(line2)

#         # If the speaker is not a justice, replace background with Court bg
#         if speaker.startswith("JUSTICE"):
#             print("Justice")
#         else:
#             replace_video_background(os.path.join(video_dir, file), os.path.join(video_dir, file))

#         if clip.duration > 10:
#             clip = add_text_overlay(clip, line1, line2, position=('center', 'bottom'), fontsize1=24, fontsize2=16, color='white', bg_color='black', bg_opacity=0.5, display_duration=8)

# #        if i > 0:
# #            gap = float(data[i-1]['gap'])
# #
# #            if gap > 2 and len(clips) != 0:
# #                prev_clip = clips[-1]
# #                if prev_clip.duration > transition_duration:
# #                    transition = prev_clip.subclip(prev_clip.duration - transition_duration).crossfadeout(transition_duration)
# #                    clips[-1] = prev_clip.set_end(prev_clip.duration - transition_duration)
# #                    clip = transition.set_start(0).crossfadein(transition_duration).set_duration(clip.duration)

#         clips.append(clip)

#     final_clip = concatenate_videoclips(clips, method="compose")
#     return final_clip

# # Get all video files in the directory and sort them
# video_files = sorted([f for f in os.listdir(video_dir) if f.endswith('.mp4')],
#                      key=lambda x: int(re.search(r'(\d+)', os.path.basename(x)).group()))
# print(video_files)
# # Merge videos with conditions and transitions
# final_clip = merge_videos_with_transition(video_files, data['sentences'], transition_duration=1)

# # Write the final video to a file
# final_clip.write_videofile(f"{video_dir}/{case_name}_final.mp4", codec="libx264")

# print("Final video with overlays and transitions created successfully.")

# -*- coding: utf-8 -*-


# import os
# """Supreme Court TV"""

# case_name = 'case3'
# data_dir = f'/home/akathpalia/data/{case_name}'

# # Directory containing the MP4 files
# video_dir = f'{data_dir}/vids/'

# if not os.path.exists(data_dir):
#     raise FileNotFoundError(f"Data directory not found: {data_dir}")

# if not os.access(data_dir, os.W_OK):
#     raise PermissionError(f"No write permission for directory: {data_dir}")

# # Path to the output file
# output_file = f'{data_dir}/vids/{case_name}_first20.mp4'

# from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ColorClip, concatenate_videoclips

# import re
# import json
# import cv2
# import numpy as np
# from moviepy.editor import VideoFileClip, ImageSequenceClip

# # Load the JSON file
# with open(f'{data_dir}/{case_name}.json', 'r') as file:
#     data = json.load(file)

# # Limit data to first 20 sentences
# data['sentences'] = data['sentences'][:20]

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

# background_image = f"{data_dir}/../src/images/bg.png"

# # Read the background image
# background = cv2.imread(background_image)
# if background is None:
#     raise FileNotFoundError(f"Background image at '{background_image}' not found or cannot be loaded.")

# # Function to replace the green background
# def replace_frame_background(frame):
#     # Convert frame to HSV
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
#     # Define the range for the green color
#     lower_green = np.array([35, 100, 100])
#     upper_green = np.array([85, 255, 255])
    
#     # Create a mask for the green color
#     mask = cv2.inRange(hsv, lower_green, upper_green)
    
#     # Invert the mask
#     mask_inv = cv2.bitwise_not(mask)
    
#     # Resize the background to match the frame
#     bg_resized = cv2.resize(background, (frame.shape[1], frame.shape[0]))
    
#     # Extract the foreground (subject)
#     fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
#     # Extract the background where the green is detected
#     bg = cv2.bitwise_and(bg_resized, bg_resized, mask=mask)
    
#     # Combine foreground and new background
#     combined = cv2.add(fg, bg)
    
#     return combined

# def replace_video_background(input_video, output_video):
#     # Process video frames
#     clip = VideoFileClip(input_video)
#     frames = []

#     for frame in clip.iter_frames():
#         # Convert the frame from MoviePy to OpenCV format
#         frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
#         # Replace the background
#         frame_with_new_bg = replace_frame_background(frame)
#         # Convert back to RGB format for MoviePy
#         frame_with_new_bg = cv2.cvtColor(frame_with_new_bg, cv2.COLOR_BGR2RGB)
#         frames.append(frame_with_new_bg)

#     # Create a new video clip with the processed frames
#     new_clip = ImageSequenceClip(frames, fps=clip.fps)
#     new_clip.write_videofile(output_video, codec='libx264')


# def merge_videos_with_transition(video_files, data, transition_duration=1):
#     clips = []
#     for file in video_files:
#         try:
#             clip = VideoFileClip(os.path.join(video_dir, file))
#         except OSError as e:
#             print(f"Error reading {file}: {e}")
#             continue
#         match = re.search(r'(\d+)', file)
#         if match:
#             i = int(match.group(1)) - 1  # Subtract 1 to match 0-based index of data['sentences']
#         else:
#             raise ValueError(f"Filename {file} does not contain a valid index")
#         speaker = data[i]["speaker"]
#         line1 = speaker

#         if speaker.startswith("JUSTICE"):
#             line2 = justices[speaker][1]
#         else:
#             line2 = "Lawyer"  # or any appropriate description

#         print(i)
#         print(line1)
#         print(line2)

#         # If the speaker is not a justice, replace background with Court bg
#         if speaker.startswith("JUSTICE"):
#             print("Justice")
#         else:
#             replace_video_background(os.path.join(video_dir, file), os.path.join(video_dir, file))

#         if clip.duration > 10:
#             clip = add_text_overlay(clip, line1, line2, position=('center', 'bottom'), fontsize1=24, fontsize2=16, color='white', bg_color='black', bg_opacity=0.5, display_duration=8)

#         clips.append(clip)

#     final_clip = concatenate_videoclips(clips, method="compose")
#     return final_clip

# # Get all video files in the directory and sort them
# video_files = sorted([f for f in os.listdir(video_dir) if f.endswith('.mp4')],
#                      key=lambda x: int(re.search(r'(\d+)', os.path.basename(x)).group()))[:20]  # Limit to first 20 files
# print(video_files)

# # Merge videos with conditions and transitions
# final_clip = merge_videos_with_transition(video_files, data['sentences'], transition_duration=1)

# # Write the final video to a file
# final_clip.write_videofile(output_file, codec="libx264")

# print("Final video with overlays and transitions created successfully.")

# -*- coding: utf-8 -*-
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