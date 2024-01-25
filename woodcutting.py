from PIL import Image, ImageGrab, ImageStat
import autopy
import time
import numpy as np
import cv2
import pyautogui
import math
from datetime import datetime
from navigation import navigate_to_location, look_at_compass_point_direction
from bank import store_all_items

max_duration_between_fish = 10

def main():
  is_cutting = False
  last_logs_time = 0
  logs_in_bag = 0

  for _ in range(0,1000):
    if not is_cutting:
      spot_found = find_willows()
      last_logs_time = datetime.now()
      if spot_found:
        is_cutting = True
    else:
      last_logs_time, logs_in_bag, is_cutting = restart_woodcutting_if_needed(last_logs_time, logs_in_bag)
      print(logs_in_bag)
      if logs_in_bag == 20:
          screen = ImageGrab.grab(bbox=(1110, 0, 1900, 540))
          world_map = screen.crop(box=(589, 63, 700, 150))
          navigate_to_location('bank')
          time.sleep(1)
          look_at_compass_point_direction('West')
          time.sleep(1)
          store_all_items()
          time.sleep(1)
          navigate_to_location('fishing')
          is_cutting = False
    time.sleep(1)


 
    # waitKey() waits for a key press to close the window and 0 specifies indefinite loop
    cv2.waitKey(0)


    # play_view.save('./pics/view.png')


def restart_woodcutting_if_needed(last_fish_time, last_fish_in_bag):
  inventort_pic = ImageGrab.grab(bbox=(1680, 240, 1840, 500))
  inventort_pic.save('./pics/incentory.png')

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
        continue_fishing = False
      else:
        time_difference = (datetime.now() - last_fish_time).total_seconds()
        if time_difference > max_duration_between_fish:
          continue_fishing = False

  return fish_time, fish_in_bag, continue_fishing

def find_willows():
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

if __name__ == "__main__":
  main()