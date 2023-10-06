from PIL import Image
from pytesseract import pytesseract
import numpy as np
import argparse
import cv2

image = cv2.imread(r"./pics/screen_crop.png")

lower = [221, 221, 5]
upper =  [241, 241, 15]

lower = np.array(lower, dtype = "uint8")
upper = np.array(upper, dtype = "uint8")
# find the colors within the specified boundaries and apply
# the mask
mask = cv2.inRange(image, lower, upper)
output = cv2.bitwise_and(image, image, mask = mask)
# show the images
cv2.imshow("images", np.hstack([image, output]))
cv2.waitKey(0)


# # Defining paths to tesseract.exe
# # and the image we would be using
# path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# image_path = r"./pics/screen_crop2.png"

  
# # Opening the image & storing it in an image object
# img = Image.open(image_path)
  
# # Providing the tesseract executable
# # location to pytesseract library
# pytesseract.tesseract_cmd = path_to_tesseract
  
# # Passing the image object to image_to_string() function
# # This function will extract the text from the image
# text = pytesseract.image_to_string(img)
  
# # Displaying the extracted text
# print(text[:-1])