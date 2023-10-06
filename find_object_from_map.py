import cv2
import numpy as np

img_rgb = cv2.imread('./pics/screen2.png')
template = cv2.imread('./pics/fire2.png')
w, h = template.shape[:-1]

res = cv2.matchTemplate(img_rgb, template, 1 )
threshold = .9
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):  # Switch columns and rows
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imwrite('./pics/result.png', img_rgb)