# Shannon–Fano Image Compression & Decompression

This project demonstrates **Shannon–Fano coding** for **lossless image compression** in Python.  
The algorithm is implemented from scratch and applied to a grayscale image.

---

## 📌 Overview

Shannon–Fano coding is a technique for constructing a **prefix code** based on a set of symbols and their probabilities.  
It is a **lossless compression algorithm**, meaning the decompressed image is exactly the same as the original.

---

## 🚀 Features

- Reads an image in **grayscale** mode.
- Computes **pixel frequency distribution**.
- Generates **Shannon–Fano codes** recursively.
- Encodes image data into a **binary bitstring**.
- Decodes the binary data back into the original image.
- Displays **compression ratio** and statistics.
- Shows both **original** and **decoded** images.


## 🚀 How to Run

### 1️⃣ Install dependencies
Make sure you have Python 3 installed. Then install required packages:
```bash
pip install opencv-python numpy matplotlib

python kaustubh_shannon.py

