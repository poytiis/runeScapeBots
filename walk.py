from PIL import Image, ImageGrab, ImageStat
import autopy
import time
import pyautogui
from navigation import find_location, navigate_to_location, look_at_compass_point_direction

def main():
  look_at_compass_point_direction('North')
  time.sleep(1)
  for i in range(0,2):
    # mapp 111, 87

    # set Runescape client to right top corner 
    screen = ImageGrab.grab(bbox=(1110, 0, 1900, 540))
    world_map = screen.crop(box=(589, 63, 700, 150))
    world_map.save('./pics/dummy.png')
    location = navigate_to_location('bank', world_map)
    # print(location)
    time.sleep(0.5)



if __name__ == "__main__":
  main()