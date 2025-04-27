import os
from PIL import Image
import imageio

# Define paths
input_root = r"/media/hashankavinga/5e384346-d3cc-422c-9519-68e8d779fc6b/Final Results reflectivity/ours/results/test_00027_dout_jet/"
output_root = r"/home/hashankavinga/Desktop/SP_LiDAR web/static/videos/Ours/depth"


# Ensure output directory exists
os.makedirs(output_root, exist_ok=True)

# Walk through all subdirectories and find PNG files
for root, _, files in os.walk(input_root):
    png_files = sorted([f for f in files if f.endswith(".png")])
    
    if png_files:
        # Prepare output path
        relative_path = os.path.relpath(root, input_root)
        output_folder = os.path.join(output_root, relative_path)
        os.makedirs(output_folder, exist_ok=True)
        
        output_gif_path = os.path.join(output_folder, "scene_06.gif")
        
        # Load up to 140 frames
        frames = []
        for i, file in enumerate(png_files):
            if i >= 140:
                break
            img_path = os.path.join(root, file)
            frame = Image.open(img_path).convert("RGB")
            frames.append(frame)

        print(f"Loaded {len(frames)} frames from {root}")

        # Save as GIF
        if frames:
            frames[0].save(output_gif_path, save_all=True, append_images=frames[1:], duration=33, loop=0)
            print(f"Saved GIF: {output_gif_path}")
