import os

def rename_files(directory_path):
    # Change current working directory
    os.chdir(directory_path)

    # Get all .png files
    png_files = [file for file in os.listdir() if file.endswith('.png')]

    # Rename files
    i = 1
    for file in png_files:
        new_name = f"{i}.png"
        os.rename(file, new_name)
        print(f"Renamed {file} to {new_name}")
        i += 1

# Use a raw string or double backslashes to avoid issues with backslashes
path = r"C:\Users\jassi\Documents\HPYTHON\data\Tut1"
rename_files(path)
