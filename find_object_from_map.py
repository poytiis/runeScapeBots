import cv2
import numpy as np

img_rgb = cv2.imread('./worldMap/map4.png')
template = cv2.imread('./worldMap/minimap11.png')
w, h = template.shape[:-1]

res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCORR_NORMED )

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = max_loc


bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img_rgb,top_left, bottom_right, 255, 20)



# threshold = .9
# loc = np.where(res >= threshold)
# for pt in zip(*loc[::-1]):  # Switch columns and rows
#     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imwrite('./worldMap/result.png', img_rgb)