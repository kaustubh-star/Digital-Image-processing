"""
Shannon–Fano Image Compression & Decompression
------------------------------------------------
This script demonstrates Shannon–Fano coding for lossless image compression.

Steps:
1. Load a grayscale image.
2. Calculate the frequency of each pixel value (0–255).
3. Generate Shannon–Fano binary codes for each pixel value.
4. Encode the image into a binary string.
5. Decode the binary string back into an image.
6. Display original and decompressed images.
7. Show compression statistics.

Author: Kaustubh + ChatGPT
"""

import cv2
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import os


# -------------------------------------------------
# Shannon–Fano Recursive Code Assignment
# -------------------------------------------------
def shannon_fano_recursive(symbols, codes):
    """
    Recursively assigns Shannon–Fano codes to symbols based on frequency.

    Parameters:
    - symbols: List of tuples (pixel_value, frequency) sorted by frequency (descending)
    - codes: Dictionary mapping pixel_value -> binary_code
    """

    # Base case: Only one symbol left, no further splitting
    if len(symbols) <= 1:
        return

    # Step 1: Total frequency of current set
    total_freq = sum(freq for _, freq in symbols)

    # Step 2: Find split point where frequency sum is close to half
    acc_freq = 0
    split_index = 0
    for i, (_, freq) in enumerate(symbols):
        acc_freq += freq
        if acc_freq >= total_freq / 2:
            split_index = i + 1
            break

    # Step 3: Assign binary prefix
    for i in range(split_index):
        codes[symbols[i][0]] += '0'  # First half gets '0'
    for i in range(split_index, len(symbols)):
        codes[symbols[i][0]] += '1'  # Second half gets '1'

    # Step 4: Recursively split each half
    shannon_fano_recursive(symbols[:split_index], codes)
    shannon_fano_recursive(symbols[split_index:], codes)


# -------------------------------------------------
# Encoding Function
# -------------------------------------------------
def shannon_fano_encode(pixels, codes):
    """
    Converts pixel array into a single binary string using Shannon–Fano codes.
    """
    return ''.join(codes[pixel] for pixel in pixels)


# -------------------------------------------------
# Decoding Function
# -------------------------------------------------
def shannon_fano_decode(encoded_str, codes):
    """
    Decodes binary string back into pixel values.
    """
    # Reverse mapping: binary_code -> pixel_value
    reverse_codes = {v: k for k, v in codes.items()}

    current_bits = ""
    decoded_pixels = []

    for bit in encoded_str:
        current_bits += bit
        # If we find a match in the reverse mapping
        if current_bits in reverse_codes:
            decoded_pixels.append(reverse_codes[current_bits])
            current_bits = ""  # Reset for next symbol

    return decoded_pixels


# -------------------------------------------------
# Main Program
# -------------------------------------------------
if __name__ == "__main__":
    # Input image path
    image_path = "./img.jpg"

    # Check if file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at: {image_path}")

    # Step 1: Load image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Step 2: Flatten into 1D pixel list
    pixels = img.flatten()

    # Step 3: Count pixel frequencies
    freq_dict = Counter(pixels)

    # Step 4: Sort symbols by frequency (descending)
    symbols = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    # Step 5: Initialize code dictionary with empty strings
    codes = {sym: '' for sym, _ in symbols}

    # Step 6: Generate Shannon–Fano codes
    shannon_fano_recursive(symbols, codes)

    # Step 7: Encode image
    encoded_str = shannon_fano_encode(pixels, codes)

    # Step 8: Decode back to pixels
    decoded_pixels = shannon_fano_decode(encoded_str, codes)

    # Step 9: Reshape decoded pixels into original shape
    decoded_img = np.array(decoded_pixels, dtype=np.uint8).reshape(img.shape)

    # Step 10: Display results
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(decoded_img, cmap='gray')
    plt.title("Decoded Image (Shannon–Fano)")
    plt.axis('off')
    plt.show()

    # Step 11: Compression statistics
    original_size_bits = len(pixels) * 8  # 8 bits per pixel
    compressed_size_bits = len(encoded_str)
    compression_ratio = round(original_size_bits / compressed_size_bits, 2)

    print("\n--- Compression Statistics ---")
    print(f"Original size (bits): {original_size_bits}")
    print(f"Compressed size (bits): {compressed_size_bits}")
    print(f"Compression Ratio: {compression_ratio}x")
    print("------------------------------")
