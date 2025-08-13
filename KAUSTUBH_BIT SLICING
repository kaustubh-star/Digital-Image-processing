# ----------------------------
# Bit Plane Slicing in OpenCV
# ----------------------------
# Author: BT23ECI018
# Description:
# This script reads a grayscale image, extracts its 8 bit planes (from LSB to MSB),
# and displays them using matplotlib.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the image in grayscale mode
# cv2.IMREAD_GRAYSCALE ensures we load only intensity values (0-255)
img = cv2.imread('./img.jpg', cv2.IMREAD_GRAYSCALE)

# Step 2: Check if the image was loaded correctly
if img is None:
    raise FileNotFoundError("Image not found! Please check the file path.")

# Step 3: Prepare a list to store all bit planes
bit_planes = []

# Step 4: Extract each bit plane
# Pixel in binary → 8 bits: [b7 b6 b5 b4 b3 b2 b1 b0]
# i = 0 → Least Significant Bit (LSB), i = 7 → Most Significant Bit (MSB)
for i in range(8):
    # Extract bit i using bitwise AND with mask (1 << i)
    # Example: If i=2, mask = 00000100 in binary
    bit_plane = cv2.bitwise_and(img, (1 << i))
    
    # Convert all non-zero values to 255 (pure white) for visibility
    bit_plane = np.where(bit_plane > 0, 255, 0).astype(np.uint8)
    
    # Store the result
    bit_planes.append(bit_plane)

# Step 5: Plot the original image and all bit planes
plt.figure(figsize=(12, 6))

# Original image
plt.subplot(3, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Bit planes from 0 to 7
for i in range(8):
    plt.subplot(3, 3, i + 2)  # start from position 2
    plt.imshow(bit_planes[i], cmap='gray')
    plt.title(f'Bit Plane {i}')
    plt.axis('off')

plt.tight_layout()
plt.show()
