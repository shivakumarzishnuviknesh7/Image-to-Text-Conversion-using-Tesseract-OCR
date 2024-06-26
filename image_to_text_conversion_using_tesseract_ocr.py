# -*- coding: utf-8 -*-
"""Image-to-Text Conversion using Tesseract OCR.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1M5x-AgC7jYNXi29o76EbP9PtANNdbR7t
"""

# Install pytesseract and OpenCV
!apt-get install tesseract-ocr
!pip install pytesseract
!pip install opencv-python-headless

import pytesseract
import cv2
from google.colab.patches import cv2_imshow

from google.colab import files

uploaded = files.upload()

for filename in uploaded.keys():
    print(f'User uploaded file "{filename}" with length {len(uploaded[filename])} bytes')
    img_path = filename

# Load the image using OpenCV
image = cv2.imread(img_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, binary_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display the preprocessed image
cv2_imshow(binary_image)

# Perform OCR
text = pytesseract.image_to_string(binary_image)

# Print the extracted text
print("Extracted Text:")
print(text)