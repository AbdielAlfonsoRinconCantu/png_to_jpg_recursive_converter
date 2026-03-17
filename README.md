# png_to_jpg_recursive_converter

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-%20%20GNU%20GPLv3%20-green?style=plastic)

Short python script to convert .PNG files to .JPG from one folder to another, recursively as new files are added.

## Installation

Make sure the following is installed:
- [pillow](https://pypi.org/project/pillow/)

On a terminal:
```bash
pip install pillow
git clone https://github.com/AbdielAlfonsoRinconCantu/png_to_jpg_recursive_converter.git
```

## Before using
Edit `line 15` with the path of your input folder, edit `line 16` with the path of your output folder.

```python
input_folder = r'\\YOUR\FOLDER\PATH\HERE'
output_folder = r'NEW_FOLDER'
```

## Usage 
On a terminal:
```bash
cd ~/png_to_jpg_recursive_converter
python png_to_jpg_recursive_converter.py
```

