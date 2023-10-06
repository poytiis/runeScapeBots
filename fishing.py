import cv2
import numpy as np
from PIL import Image, ImageGrab, ImageStat
import autopy
import time

def main():

  for _ in range(0,1):
    find_fishing_spot()
    # set Runescape client to right top corner 
   


    # corner_map = pic.crop(box=(600, 5, 745, 175))
    # corner_map.save('./pics/map3.png')


def find_fishing_spot():
  pic = ImageGrab.grab(bbox=(1100, 35, 1920, 600))
  play_view = pic.crop(box=(20, 0, 500, 330))
  play_view_cropped = play_view.crop(box=(0, 30, 480, 330))
  play_view_cropped.save('./pics/play_view.png')

  lake = play_view.crop(box=(250, 250, 340, 330))
  lake.save('./pics/lake.png')

  lake_cv2 =  np.array(lake)
  play_view_cv2 = np.array(play_view_cropped)

  opencvImage = cv2.cvtColor(play_view_cv2, cv2.COLOR_RGB2BGR)

  # hsv_img = cv2.cvtColor(np.array(opencvImage), cv2.COLOR_BGR2HSV)

  # opencvImage = cv2.cvtColor(lake_cv2, cv2.COLOR_RGB2BGR)

  hsv_img = cv2.cvtColor(np.array(opencvImage), cv2.COLOR_BGR2HSV)

  hue = hsv_img[0]
  # print(hsv_img)

  lower_blue = np.array([90,0,0])
  upper_blue = np.array([120,255,255])
  # Threshold the HSV image to get only blue colors
  mask = cv2.inRange(hsv_img, lower_blue, upper_blue)

  mask_blur = cv2.blur(mask,(5,5))

  edges = cv2.Canny(mask_blur, 50, 150) 

  output = cv2.bitwise_and(hsv_img, hsv_img, mask = mask)
	# show the images
  # cv2.imshow("images", np.hstack([hsv_img, output]))
  # cv2.imshow("images", mask)
  # cv2.imshow("images2", mask_blur)
  # cv2.imshow("images3", edges)
  cv2.waitKey(0)

  # cv2.imwrite('./pics/view.png', opencvImage)
  print(edges.shape)

  x_points = []
  y_points = []

  for y_index, arr in enumerate(edges):
    for x_index, pixel_value in enumerate(arr) :
      if pixel_value == 255:
        x_points.append(x_index)
        y_points.append(y_index)

  # print(y_points)

  z = np.polyfit(np.array(x_points), np.array(y_points), 9)
  p = np.poly1d(z)

  print(z)

  x_points = [50, 100, 150, 200, 250, 300, 350, 400]

  for x in x_points:
    y = int(p(x))

    opencvImage = cv2.circle(opencvImage, (x, y), 2, (255, 0, 0), 2)
  cv2.imshow("images3", opencvImage)
  cv2.imshow("images2", edges)
  cv2.waitKey(0)

if __name__ == "__main__":
  main()