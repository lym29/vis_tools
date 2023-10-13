import os

# root_path = "/Users/yumeng/Working/Project2023/result/grasptta_grab/"
# root_path = "/Users/yumeng/Working/Project2023/result/vis_shadowhand/"
# model_name = "120-245"
# img_dir =os.path.join(root_path, model_name, "img")
# video_dir = os.path.join(root_path, model_name)

# cmd = f"ffmpeg -f image2 -r 1/0.1 -i {img_dir}/snapshot00_L%2d.png -vcodec mpeg4 -y {video_dir}/{model_name}.mp4"
# os.system(cmd)

root_path = "/Users/yumeng/Working/Project2023/result/toch-grab-refine/mug-test"
model_name = "2"
img_dir =os.path.join(root_path, "imgs-"+model_name)
video_dir = os.path.join(root_path, "video", model_name)
if not os.path.exists(video_dir):
        os.makedirs(video_dir)

cmd = f"ffmpeg -f image2 -r 1/0.1 -i {img_dir}/snapshot00_L%2d.png -vcodec mpeg4 -y {video_dir}/{model_name}.mp4"
os.system(cmd)