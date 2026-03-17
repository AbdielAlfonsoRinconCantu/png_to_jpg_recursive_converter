# png_to_jpg_recursive_converter

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-%20%20GNU%20GPLv3%20-green?style=plastic)

Short python script to convert .PNG files to .JPG from one folder to another, recursively as new files are added.

<img width="1115" height="628" alt="png_to_jpg_recursive_converter" src="https://github.com/user-attachments/assets/19a07c71-16ad-49f9-8dbe-b11f85658e5f" />

## Installation

Make sure the following is installed:
- [pillow](https://pypi.org/project/pillow/)

On a terminal:
```bash
pip install pillow
git clone https://github.com/AbdielAlfonsoRinconCantu/png_to_jpg_recursive_converter.git
```

## Before using
Edit `line 14` with the path of your input folder, edit `line 15` with the path of your output folder.

```python
14  input_folder = r'\\YOUR\FOLDER\PATH\HERE'
15  output_folder = r'NEW_FOLDER'
```

## Usage 
On a terminal:
```bash
cd ~/png_to_jpg_recursive_converter
python png_to_jpg_recursive_converter.py
```

