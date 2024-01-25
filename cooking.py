import time
import pyautogui
from object import click_nearest_object
from navigation import navigate_to_location, look_at_compass_point_direction
from bank import store_all_items_and_take_one_item
from random import seed, random

def main():
  seed(1)
  for _ in range(0,150):
      fire_found = click_nearest_object()
      if fire_found:
        time.sleep(3)
        pyautogui.moveTo(1370, 430)
        pyautogui.click()
        time.sleep(62 +  3 * random())
        navigate_to_location('bank')
        look_at_compass_point_direction('West')
        time.sleep(1)
        store_all_items_and_take_one_item('tuna')
        time.sleep(1)
        navigate_to_location('fire')


    

if __name__ == "__main__":
  main()