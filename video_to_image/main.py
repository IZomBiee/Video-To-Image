import argparse
import cv2 as cv
import os
import random

def letterbox_resize(image, target_width, target_height):
    h, w = image.shape[:2]
    ratio = min(target_width / w, target_height / h)
    new_w = int(w * ratio)
    new_h = int(h * ratio)
    resized = cv.resize(image, (new_w, new_h))
    
    if len(image.shape) == 3:
        canvas = np.zeros((target_height, target_width, image.shape[2]), dtype=np.uint8)
    else:
        canvas = np.zeros((target_height, target_width), dtype=np.uint8)
    
    y_offset = (target_height - new_h) // 2
    x_offset = (target_width - new_w) // 2
    canvas[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = resized
    return canvas

parser = argparse.ArgumentParser()
parser.add_argument('video_path', help='Video file path')
parser.add_argument('--width', type=int, help='Output width')
parser.add_argument('--height', type=int, help='Output height')
parser.add_argument('--skip_begin', type=int, default=0, help='Frames to skip at start')
parser.add_argument('--skip_every', type=int, default=1, help='Save every n-th frame')
parser.add_argument('--no_keep_aspect', action='store_true', help='Disable aspect ratio preservation')
args = parser.parse_args()

video_dir = os.path.dirname(args.video_path)
video_name = os.path.splitext(os.path.basename(args.video_path))[0]
save_dir = os.path.join(video_dir, video_name)
os.makedirs(save_dir, exist_ok=True)

video = cv.VideoCapture(args.video_path)
for _ in range(args.skip_begin):
    video.read()

frame_count = 0
save_count = 0

seed = random.randint(1000, 9999)

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    
    if frame_count % args.skip_every == 0:
        if args.width or args.height:
            if args.width and args.height:
                if args.no_keep_aspect:
                    frame = cv.resize(frame, (args.width, args.height))
                else:
                    import numpy as np
                    frame = letterbox_resize(frame, args.width, args.height)
            elif args.width:
                ratio = frame.shape[0] / frame.shape[1]
                new_height = int(args.width * ratio)
                frame = cv.resize(frame, (args.width, new_height))
            elif args.height:
                ratio = frame.shape[1] / frame.shape[0]
                new_width = int(args.height * ratio)
                frame = cv.resize(frame, (new_width, args.height))
        
        cv.imwrite(f'{save_dir}/{save_count}-{seed}.jpg', frame)
        save_count += 1
    
    frame_count += 1