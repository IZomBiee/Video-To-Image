# What Does the Program Do?
This program is a simple tool for extracting images from a video with customizable settings. It saves the images to a folder named after the video, located in the same directory.
---
# How to Set Up
1. Install Python 3.13 or higher from [python.org](https://www.python.org/downloads/)

2. Install Poetry by running:
```shell
pip install poetry
```

3. Clone the repository (e.g., to your Desktop) or download it manually:
```shell
cd Desktop
git clone https://github.com/IZomBiee/Video-To-Image.git
```

4. Navigate to the project directory and set up the Poetry environment:
```shell
cd Pubg-Mortar-Calculator
poetry install
```

5. Run the program:
```shell
poetry run python pubg_mortar_calculator/main.py
```
---
# How to use
### --width 1920
Sets the width of the output images.
### --height 1080
Sets the height of the output images.
### --no_keep_aspect
If enabled, the image will stretch to fit the specified resolution. Otherwise, it will preserve the aspect ratio with black borders.
### --skip_every 5
Skips 5 frames between each captured image.
### --skip_begin 50
Skips the first 50 frames before starting capture.
```python
poetry run python pubg_mortar_calculator/main.py "C:\Users\patri\Videos\2025-06-07 11-38-44.mkv" --skip_every 5 --width 1080 --height --1080 --no_keep_aspect --skip_begin 50
``` 
