# config.py

import os
import cv2

# Data
case_name = 'case3'
data_dir = f'/home/akathpalia/data/{case_name}'
video_dir = f'{data_dir}/vids'
output_dir = f'{data_dir}/outputs'
output_file = f'{output_dir}/output_gpu.mp4'
background_image = "src/images/bg.png"
background = cv2.imread(background_image)

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)