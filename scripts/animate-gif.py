import os
from PIL import Image

# Set the folder path containing the images
folder_path = "/home/long/Documents/repositories/stable-diffusion-webui/outputs/img2img-images/2023-06-20/"

# Get all image file names in the folder
image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Create a list to store the image frames
frames = []

# Load each image and append it to the frames list
for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    image = Image.open(image_path)
    frames.append(image)

# Create the first frame as a base for the animation
base_frame = frames[0].convert('RGBA')
duration = 150  # Transition time between frames (in milliseconds)

# Create a list to store the frames with the dissolve effect
dissolve_frames = [base_frame]

# Apply the dissolve effect to each pair of consecutive frames
for i in range(1, len(frames)):
    next_frame = frames[i].convert('RGBA')
    dissolved_frame = Image.blend(base_frame, next_frame, alpha=(i / len(frames)))
    dissolve_frames.append(dissolved_frame)
    base_frame = next_frame

# Save the frames with the dissolve effect as an animated GIF
output_path = os.path.join(folder_path, "animated.gif")
dissolve_frames[0].save(output_path, format='GIF', append_images=dissolve_frames[1:], save_all=True, duration=duration, loop=0)