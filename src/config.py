# config.py

import os
import cv2
import moviepy.config as cfg

cfg.change_settings({"IMAGEMAGICK_BINARY": r"/home/akathpalia/miniconda3/envs/py38/bin/convert"})  # Adjust this path as needed

# Data
case_name = 'case3'
data_dir = f'/home/akathpalia/data/{case_name}'
video_dir = f'{data_dir}/vids'
output_dir = f'{data_dir}/outputs'
output_file = f'{output_dir}/output_case3.mp4'

background_image = "src/images/bg.png"
background = cv2.imread(background_image)
if background is None:
    raise FileNotFoundError(f"Background image at '{background_image}' not found or cannot be loaded.")
background_video = "src/images/background.mp4"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)