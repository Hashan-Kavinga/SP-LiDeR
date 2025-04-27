import os
import imageio
from PIL import Image

# Define paths
input_root = r"C:\Users\hasha\Downloads\11788_Joint_Depth_and_Reflecti_Supplementary Material\Supplementary"
output_root = r"C:\Users\hasha\Downloads\11788_Joint_Depth_and_Reflecti_Supplementary Material\Supplementary"

# Ensure output directory exists
os.makedirs(output_root, exist_ok=True)

# Walk through all subdirectories and find .mp4 files
for root, _, files in os.walk(input_root):
    for file in files:
        if file.endswith(".mp4"):
            input_path = os.path.join(root, file)
            
            # Preserve folder structure in output directory
            relative_path = os.path.relpath(root, input_root)
            output_folder = os.path.join(output_root, relative_path)
            os.makedirs(output_folder, exist_ok=True)
            
            # Define output path (same file name, just .gif extension)
            output_path = os.path.join(output_folder, file.replace(".mp4", ".gif"))
            
            # Convert to GIF
            try:
                reader = imageio.get_reader(input_path)
                fps = reader.get_meta_data().get('fps', 30)  # Default to 30 FPS if missing
                
                # Read and save first 140 frames
                frames = []
                for i, frame in enumerate(reader):
                    if i >= 140:  # Stop after 140 frames
                        break
                    frames.append(Image.fromarray(frame))
                
                print(f"Saved {len(frames)} frames for {file}")  # Debugging output
                
                # Save frames as GIF with the same file name
                if frames:
                    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=int(1000/fps), loop=0)
                    print(f"Converted: {input_path} → {output_path}")
                else:
                    print(f"No frames extracted from {input_path}")
                
            except Exception as e:
                print(f"Error processing {input_path}: {e}")
