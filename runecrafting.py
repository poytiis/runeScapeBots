import time
import pyautogui
from random import seed, random
from navigation import navigate_to_location, look_at_compass_point_direction, find_location
from PIL import Image, ImageGrab, ImageStat

def main():
  seed(1)
  for _ in range(0, 1):
    screen = ImageGrab.grab(bbox=(1110, 0, 1900, 540))
    world_map = screen.crop(box=(589, 63, 700, 150))
    current_position = find_location(world_map, '6')   
    print(current_position)

if __name__ == "__main__":
  main()