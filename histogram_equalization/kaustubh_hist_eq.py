# ---------------------------
# Histogram Equalization using OpenCV
# ---------------------------

import cv2  # OpenCV for image processing

# Step 1: Read the image in grayscale mode
# (Grayscale is used because histogram equalization works on intensity values)
img = cv2.imread('./img.jpg', cv2.IMREAD_GRAYSCALE)

# Step 2: Check if the image was loaded successfully
if img is None:
    raise FileNotFoundError("Image file not found! Please check the path.")

# Step 3: Apply histogram equalization
# This improves the contrast of the image by spreading out pixel intensity values
equalized_img = cv2.equalizeHist(img)

# Step 4: Resize the equalized image for display purposes
# (800px width x 600px height)
resized_img = cv2.resize(equalized_img, (800, 600))

# Step 5: Display the processed image
cv2.imshow("Histogram Equalized Image", resized_img)

# Step 6: Wait for a key press and then close the display window
cv2.waitKey(0)  # 0 means wait indefinitely until a key is pressed
cv2.destroyAllWindows()
