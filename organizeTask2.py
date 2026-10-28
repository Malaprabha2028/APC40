import os
import shutil

source = "files"
destination = "organized"

os.makedirs(destination, exist_ok=True)

for file in os.listdir(source):
    path = os.path.join(source, file)

    if os.path.isfile(path):
        ext = os.path.splitext(file)[1].lower()

        if ext:
            folder = ext[1:] + "_files"
        else:
            folder = "others"

        folder_path = os.path.join(destination, folder)
        os.makedirs(folder_path, exist_ok=True)

        shutil.move(path, os.path.join(folder_path, file))

print("Files organized successfully!")