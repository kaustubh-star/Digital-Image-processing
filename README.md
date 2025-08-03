# 🖼️ Digital Image Processing using MATLAB

This repository contains MATLAB scripts for basic digital image processing operations. It is intended for academic and learning purposes to understand how color spaces and pixel manipulation work at a foundational level.

## 📌 Script Overview

### ▶️ `main.m`
This script performs the following operations on an image named `wallpaper.jpg`:

1. **Display Original Image**
2. **Convert to Grayscale** – using a custom `toGrayscale()` function
3. **Convert to Black and White** – using a custom `toBlackWhite()` function with a threshold value
4. **Remove Individual Color Channels** – Red, Green, and Blue removed one at a time using `removeChannel()`

## 🧩 Custom Functions Used

You’ll need to implement or include the following user-defined functions in the same folder:
- `toGrayscale(image)` – Converts RGB image to grayscale manually (not using built-in `rgb2gray`)
- `toBlackWhite(image, threshold)` – Converts grayscale image to binary using the given threshold
- `removeChannel(image, channel)` – Removes one of the RGB channels and displays the result

## 📷 Output

The script will display:
- Original image
- Grayscale image
- Black & white image
- Three separate images with individual RGB channels removed

## 🧠 Learning Outcomes

- Understanding color spaces and conversions
- Manual thresholding and binary image generation
- Channel-wise pixel manipulation
- Basic use of figure plotting and image display in MATLAB


