import os

root_path = "/Users/yumeng/Downloads/Canvas-0"
img_dir =os.path.join(root_path)
video_dir = os.path.join(root_path, "video")
if not os.path.exists(video_dir):
        os.makedirs(video_dir)

cmd = f"ffmpeg -f image2 -r 1/0.1 -i {img_dir}/frame_%4d.png -vcodec mpeg4 -y {video_dir}/video.mp4"
os.system(cmd)

