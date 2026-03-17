# png_to_jpg_recursive_converter.py
# ver 1.0
# Converts all PNG images from a folder and its subfolders
# to JPG, infinite loop, runs on console

print("\nImporting libraries...")
from PIL import Image
import os
import time
import datetime
print("Libraries imported succesfully")

print(f"Script start: {datetime.datetime.now()}\n")
input_folder = r'C:\Users\M2509007\Desktop\Desktop_0\0.Programming\BMP_and_PNG_to_JPG_converter\2025102400'
output_folder = r'NEW_FOLDER_wuuuu'
os.makedirs(output_folder, exist_ok=True)

converted_files = set()

while True:
    for dirpath, dirnames, filenames in os.walk(input_folder):
        for filename in filenames:
            if filename.lower().endswith('.png'):
                source_path = os.path.join(dirpath, filename)

                if source_path in converted_files:
                    continue

                relative_path = os.path.relpath(dirpath, input_folder)
                target_directory = os.path.join(output_folder, relative_path)
                os.makedirs(target_directory, exist_ok=True)
                target_path = os.path.join(
                    target_directory, os.path.splitext(filename)[0] + '.jpg')

                try:
                    with Image.open(source_path) as img:
                        img.convert('RGB').save(
                            target_path, 'JPEG', quality=95)
                        print(f"[{filename}] has been converted successfully")
                        converted_files.add(source_path)
                except Exception as e:
                    print(f"Failed to convert {source_path}: {e}")

    time.sleep(1)
