# This script generates different .jpg files according to a few settings.
# Images differ in size, background, text color and number in the printed text
# Before you run it you need to provide the values of several variables below in section Settings
# and set destination folder

from PIL import Image, ImageDraw, ImageFont
import os
import random

# Create a destination folder to store the generated images
output_folder = "/home/michal/pictures"
os.makedirs (output_folder, exist_ok=True)

# Settings
start_with = 1                 # Start numbering files with this value
num_images = start_with + 9    # Change this to the number of images you want
image_width = 100              # Set the image width
image_height = 100             # Set the image height
font_size = 10                 # Define font size
font_path = "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf" # Replace with your font file
font = ImageFont.truetype(font_path, font_size)

# Function to generate a random color
def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
# Generating an image
for start_with in range (start_with, num_images+1):
    image = Image.new("RGB", (image_width, image_height), color=get_random_color())
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), f"Image no. {str(start_with)}", fill=get_random_color(), font=font)  # Add some text starting
    # from the point with the given coordinates
    image.save(f"{output_folder}/image_{start_with}.jpg")
    print(f"Generated image {start_with}")        


print("Generation completed!")
