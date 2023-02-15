import cv2
import os
import mimetypes
from sys import argv

video_path = argv[1]
output_path = argv[2]

if not os.path.exists(video_path):
    print(f'video does not exist at {video_path}')
    quit()

type = mimetypes.guess_type(video_path)[0]
if 'video' not in type:
    print(f'file is a {type} not a video!')
    quit()

if not os.path.exists(output_path):
    os.mkdir(output_path)
    print(f'{output_path} does not exist. Created a new folder at {output_path}')
video = cv2.VideoCapture(video_path)
success, image = video.read()
count = 0

while success:
    cv2.imwrite(f'{output_path}/{count}.jpg', image)
    success, image = video.read()
    print('Read a new frame: ', success)
    count += 1