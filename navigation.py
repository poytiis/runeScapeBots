import cv2
import numpy as np
import time
import pyautogui
from PIL import Image, ImageGrab, ImageStat

locations = {
  'bank': (394, 435),
  'fishing': (367, 477),
  'fire': (420, 465),
  'body_ruins': (60, 310),
  'bank_edge': ()
}

def find_location(mini_map, map_number = '5'):
  large_map = cv2.imread('./worldMap/map' + map_number + '.png')

  mini_map_numpy = np.array(mini_map)
  template_map = cv2.cvtColor(mini_map_numpy, cv2.COLOR_RGB2BGR)
  template_width, template_height = template_map.shape[:-1]

  template_res = cv2.matchTemplate(large_map, template_map, cv2.TM_CCORR_NORMED )
  _, _, _, max_loc = cv2.minMaxLoc(template_res)
  top_left = max_loc

  player_position = (top_left[0] +  int(0.7 * template_width), top_left[1] +  int(0.5 * template_height))
  a = cv2.circle(large_map, player_position, 4, (255, 0, 0) , 2)
  cv2.imwrite('./worldMap/result' + str(int(time.time())) + '.png', a)

  return player_position

def navigate_to_location(location: str):
  look_at_compass_point_direction('North')
  position = locations[location]
  time.sleep(1)
  for _ in range(0, 3):
    screen = ImageGrab.grab(bbox=(1110, 0, 1900, 540))
    world_map = screen.crop(box=(589, 63, 700, 150))
    current_position = find_location(world_map)
    print(current_position)
    dx = current_position[0] - position[0]
    dy = current_position[1] - position[1]

    if abs(dx) > 200 or abs(dy) > 200:
      print(dx, dy)
      print('invalid template matching')
      return

    if dx > 60:
      dx = 60
    elif dx < -60:
      dx = -60
    if dy > 60:
      dy = 60
    elif dy < -60:
      dy = -60

    player_location_in_screen = (1755 - dx, 110 - dy)

    pyautogui.moveTo(player_location_in_screen[0], player_location_in_screen[1])
    pyautogui.click()
    time.sleep(4)

    if abs(dx) + abs(dy) < 14:
      break

    print(dx, dy)

def look_at_compass_point_direction(compass_point: str):
  compass_center_point = (1675, 35) 
  pyautogui.moveTo(compass_center_point[0], compass_center_point[1])
 
  if compass_point == 'North':
    pyautogui.click()
  else:
    pyautogui.click(button='right')
    if compass_point == 'East':
      pyautogui.move(0, 35)
    elif compass_point == 'South':
      pyautogui.move(0, 50)
    elif compass_point == 'West':
      pyautogui.move(0, 65)
    else:
      print('Invalid compass point')

    pyautogui.click()
