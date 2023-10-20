import os
import fileinput

# Define the directory where you want to search for files
directory = 'C:/Users/kairn/Music/kk/'

# Function to search and replace in a single file
def replace_in_file(file_path):
    with fileinput.FileInput(file_path, inplace=True) as file:
        for line in file:
            print(line.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7033703888764854" crossorigin="anonymous"></script>'), end='')

# Recursively search for files in the directory
for foldername, subfolders, filenames in os.walk(directory):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        if file_path.endswith('.html'):  # Adjust the file extension as needed
            replace_in_file(file_path)
            print(file_path)
