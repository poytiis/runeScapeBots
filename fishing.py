import cv2
import numpy as np
from PIL import ImageGrab, ImageStat
import autopy
import time
from datetime import datetime
from tesseract import read_text_from_image
from random import seed, random

max_duration_between_fish = 14

def main():
  is_fishing = False
  last_fish_time = 0
  fish_in_bag = 0
  for _ in range(0,14000):
    if not is_fishing:
      spot_found = find_fishing_spot()
      last_fish_time = datetime.now()
      if spot_found:
        is_fishing = True
    else:
      last_fish_time, fish_in_bag, is_fishing = restart_fishing_if_needed(last_fish_time, fish_in_bag)
    time.sleep(1)

def empty_bag():
  seed(1)
  for i in range (0, 5):
    for j in range(0, 4):       
      random_num = random()
      autopy.mouse.move(1100 + 610 + j*40, 35 + 250 + 40*i)    
      autopy.mouse.click(button=autopy.mouse.Button.RIGHT)
      time.sleep(0.1)
      autopy.mouse.smooth_move(1100 + 610 + j*40,  35 + 250 + 35+ 40*i)
      time.sleep(0.1)
      autopy.mouse.click()
      time.sleep(random_num)

def restart_fishing_if_needed(last_fish_time, last_fish_in_bag):
  inventort_pic = ImageGrab.grab(bbox=(1690, 240, 1850, 500))

  image_height = 38
  margin_top = 34
  image_width = 40

  fish_in_bag = 0
  for column in range(0, 4):
    for row in range(0, 5):
      box = (
        image_width * column, 
        margin_top + image_height * row, 
        image_width * column + image_width,  
        margin_top + image_height * row + image_height
      )
      slot_image = inventort_pic.crop(box=box)
      slot_image_stat = ImageStat.Stat(slot_image)
      if slot_image_stat.var[0] > 20:
        fish_in_bag += 1

  fish_time = last_fish_time
  continue_fishing = True
  if fish_in_bag != last_fish_in_bag:
    fish_time = datetime.now()
  else:
      if fish_in_bag == 20:
        empty_bag()
        continue_fishing = False
        fish_in_bag = 0
      else:
        time_difference = (datetime.now() - last_fish_time).total_seconds()
        if time_difference > max_duration_between_fish:
          continue_fishing = False

  return fish_time, fish_in_bag, continue_fishing

def find_fishing_spot():
  pic = ImageGrab.grab(bbox=(1100, 35, 1920, 600))
  play_view = pic.crop(box=(20, 0, 500, 330))
  play_view_cropped = play_view.crop(box=(0, 30, 480, 330))
  play_view_cropped.save('./pics/play_view.png')

  play_view_cv2 = np.array(play_view_cropped)

  opencvImage = cv2.cvtColor(play_view_cv2, cv2.COLOR_RGB2BGR)

  hsv_img = cv2.cvtColor(np.array(opencvImage), cv2.COLOR_BGR2HSV)

  lower_blue = np.array([90,0,0])
  upper_blue = np.array([120,255,255])

  # Threshold the HSV image to get only blue colors
  mask = cv2.inRange(hsv_img, lower_blue, upper_blue)

  mask_blur = cv2.blur(mask,(5,5))

  edges = cv2.Canny(mask_blur, 50, 150) 

  x_points = []
  y_points = []

  for y_index, arr in enumerate(edges):
    for x_index, pixel_value in enumerate(arr) :
      if pixel_value == 255:
        x_points.append(x_index)
        y_points.append(y_index)


  z = np.polyfit(np.array(x_points), np.array(y_points), 9)
  p = np.poly1d(z)

  x_points = [ *range(50, 500, 25)]
  y_points = []

  for x in x_points:
    y = int(p(x))
    y_points.append(y)

  seed(1)
  random_num = random()
  for x_index, x_value in enumerate(x_points):
    if y_points[x_index] > 500 or y_points[x_index] < -500:
      print(y_points)
      continue
    autopy.mouse.move(1100 + x_value, 60 +  int(random_num * 150) + y_points[x_index])
    time.sleep(0.2)

    play_view = ImageGrab.grab(bbox=(1120, 35, 1620, 365))
    text_area = play_view.crop(box=(10, 0, 290, 30))

    text = read_text_from_image(text_area)
    print(text)

    valid_words = ['Small', 'Net', 'Fishing', 'spot']

    for word in valid_words:
      if word in text:
        autopy.mouse.click()
        return True
      
  return False

if __name__ == "__main__":
  main()