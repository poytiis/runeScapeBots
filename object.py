from PIL import ImageGrab
import autopy
import time
import numpy as np
import cv2
import pyautogui
import math

def click_nearest_object():
  screen = ImageGrab.grab(bbox=(1110, 0, 1900, 540))
  play_view = screen.crop(box=(10, 30, 520, 366))
  play_view_numpy = np.array(play_view)
  play_view_hsv  = cv2.cvtColor(play_view_numpy, cv2.COLOR_RGB2HSV)

  lower_pink = np.array([150,100,100])
  upper_pink = np.array([160,255,255])

  # Threshold the HSV image to get only pink colors
  target_borders = cv2.inRange(play_view_hsv, lower_pink, upper_pink)

  contours, _ = cv2.findContours(target_borders, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  player_location = [300, 200]
  shortest_distance = 1000000
  shortest_location = [0,0]

  for contour in contours:
      area = cv2.contourArea(contour)
      if area < 80:
          continue
      M = cv2.moments(contour)
      if M['m00'] == 0 or M['m00'] == 0:
          continue
      cx = int(M['m10']/M['m00'])
      cy = int(M['m01']/M['m00'])
      
      distance = math.dist([cx, cy], player_location)
      if distance < shortest_distance:
          shortest_location = [cx, cy]
          shortest_distance = distance

  if shortest_distance != 1000000:
      pyautogui.moveTo(1110 + shortest_location[0], 30 + shortest_location[1])
      pyautogui.click()
      return True
  return False