# This script creates .txt files according the settings - file size in KB and number of files.
# Before you use it, set destination folder and a variables' values in section Settings

import os

# Create a destination folder to store the generated files
output_folder = "/home/michal/txt"
os.makedirs (output_folder, exist_ok=True)

# Settings 
target_size_kb = 3 # Set the file size in KB
num_files = 10     # Set the number of files you need
target_size = target_size_kb * 1024

def generate_text_file(file_name, target_size):
    with open(file_name, 'w') as f:
        f.write('a' * target_size)  # Adding blocks of data to a file
    print(f"File {file_name} has been saved, it's size is {os.path.getsize(file_name) / 1024:.2f} KB")
        

# Create a specified number of files of a given size
for i in range(1, num_files + 1):
    generate_text_file(f'{output_folder}/generated_file_{i}.txt', target_size)
