import cv2 
import numpy as np 
  
# Load the image 
image = cv2.imread("./pics/map2.png") 
  
# Convert to grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
  
# Blur the image 
blurred = cv2.GaussianBlur(gray, (7, 7), 0) 
  
# Detect edges 
edges = cv2.Canny(blurred, 50, 150) 
  
# Find contours 
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
  
# Filter contours 
rects = [] 
for contour in contours: 
    # Approximate the contour to a polygon 
    polygon = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True) 
      
    # Check if the polygon has 4 sides and the aspect ratio is close to 1 
    if len(polygon) == 4 and abs(1 - cv2.contourArea(polygon) / (cv2.boundingRect(polygon)[2] * cv2.boundingRect(polygon)[3])) < 0.1: 
      rects.append(polygon) 
  
# Draw rectangles 
for rect in rects: 
    cv2.drawContours(image, [rect], 0, (0, 255, 0), 2) 
  
# Show the result 
cv2.imshow("Rectangles", image) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 