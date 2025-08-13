import cv2
import numpy as np
import heapq
from collections import Counter
import matplotlib.pyplot as plt

# -------------------------------
# Huffman Coding Node Definition
# -------------------------------
class Node:
    def __init__(self, value, freq):
        """
        Represents a node in the Huffman Tree.
        :param value: Pixel value (0–255) or None for internal nodes.
        :param freq: Frequency of the pixel value in the image.
        """
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        """
        Comparator for priority queue (min-heap) based on frequency.
        """
        return self.freq < other.freq


# -------------------------------
# Build Huffman Tree
# -------------------------------
def build_huffman_tree(freq_dict):
    """
    Builds the Huffman Tree from a frequency dictionary.
    :param freq_dict: Dictionary {pixel_value: frequency}
    :return: Root node of Huffman Tree
    """
    # Create a heap of leaf nodes
    heap = [Node(value, freq) for value, freq in freq_dict.items()]
    heapq.heapify(heap)

    # Merge nodes until only one root remains
    while len(heap) > 1:
        left = heapq.heappop(heap)   # Smallest frequency node
        right = heapq.heappop(heap)  # Second smallest

        merged = Node(None, left.freq + right.freq)  # Internal node
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]  # Root node


# -------------------------------
# Generate Huffman Codes
# -------------------------------
def generate_codes(node, current_code="", codes=None):
    """
    Recursively generates Huffman codes for each pixel value.
    :param node: Current node in Huffman Tree
    :param current_code: Code built so far
    :param codes: Dictionary to store codes
    :return: Dictionary {pixel_value: huffman_code}
    """
    if codes is None:
        codes = {}

    if node is None:
        return codes

    # Leaf node → store its code
    if node.value is not None:
        codes[node.value] = current_code
        return codes

    # Traverse left → append "0"
    generate_codes(node.left, current_code + "0", codes)
    # Traverse right → append "1"
    generate_codes(node.right, current_code + "1", codes)

    return codes


# -------------------------------
# Huffman Encode
# -------------------------------
def huffman_encode(pixels, codes):
    """
    Converts pixel values into a Huffman-encoded bitstring.
    :param pixels: 1D array of pixel values
    :param codes: Huffman code mapping
    :return: Encoded bitstring
    """
    return ''.join(codes[p] for p in pixels)


# -------------------------------
# Huffman Decode
# -------------------------------
def huffman_decode(encoded_str, codes):
    """
    Converts a Huffman-encoded bitstring back into pixel values.
    :param encoded_str: Encoded bitstring
    :param codes: Huffman code mapping
    :return: Decoded pixel list
    """
    reverse_codes = {v: k for k, v in codes.items()}  # Reverse mapping
    current_code = ""
    decoded_pixels = []

    for bit in encoded_str:
        current_code += bit
        if current_code in reverse_codes:  # Found a complete code
            decoded_pixels.append(reverse_codes[current_code])
            current_code = ""  # Reset for next code

    return decoded_pixels


# -------------------------------
# Main Implementation
# -------------------------------

# Step 1: Read the input grayscale image
img = cv2.imread("./img.jpg", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError("Image not found! Please check the file path.")

# Step 2: Flatten image into 1D array
pixels = img.flatten()

# Step 3: Count frequency of each pixel value
freq_dict = Counter(pixels)

# Step 4: Build Huffman Tree
root = build_huffman_tree(freq_dict)

# Step 5: Generate Huffman Codes
codes = generate_codes(root)

# Step 6: Encode image pixels into a bitstring
encoded_str = huffman_encode(pixels, codes)

# Step 7: Decode the bitstring back into pixels
decoded_pixels = huffman_decode(encoded_str, codes)

# Step 8: Convert decoded pixels back into image format
decoded_img = np.array(decoded_pixels, dtype=np.uint8).reshape(img.shape)

# Step 9: Display Original vs Decoded images
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(decoded_img, cmap='gray')
plt.title("Decoded Image (Huffman)")
plt.axis('off')

plt.show()

# Step 10: Print Compression Statistics
original_size = len(pixels) * 8  # bits (8 bits per pixel)
compressed_size = len(encoded_str)  # bits
compression_ratio = round(original_size / compressed_size, 2)

print("Original size (bits):", original_size)
print("Compressed size (bits):", compressed_size)
print("Compression ratio:", compression_ratio)
