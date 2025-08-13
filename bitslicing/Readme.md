# Bit Plane Slicing in OpenCV

## 📌 Overview
This project demonstrates **Bit Plane Slicing** using OpenCV and Python.  
Bit Plane Slicing is a technique in image processing where we separate an image into its **binary layers** (bit planes) to analyze how much each bit contributes to the overall image.

Grayscale images are represented using **8 bits per pixel** (values 0–255). Each bit represents a different level of detail:
- **Lower bits (0–3)** → Fine details and noise
- **Higher bits (4–7)** → Main structure and contrast

---

## 🖼 Example Output
The script displays:
1. Original grayscale image
2. Bit planes from **0 (LSB)** to **7 (MSB)**

---

## 🚀 How to Run

### 1️⃣ Install dependencies
Make sure you have Python 3 installed. Then install required packages:
```bash
pip install opencv-python numpy matplotlib

python kaustubh_bitslicing.py


