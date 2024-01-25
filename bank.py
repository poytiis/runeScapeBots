from PIL import ImageGrab
from tesseract import read_text_from_image
import math
import pyautogui
import time
from random import seed, random

def store_all_items():
  is_bank_open = open_bank_window()
  if is_bank_open:
    store_all_items_ui_clicking()

def store_all_items_ui_clicking():
  pyautogui.moveTo(1550, 350)
  pyautogui.click()
  time.sleep(1.5 + random())
  pyautogui.moveTo(1595, 40)
  pyautogui.click()
  time.sleep(1)

def open_bank_window():
  x_points = [ *range(1200, 1600, 10)]
  seed(1)
  for x_point in x_points:
    print(math.sin(x_point))
    y_point = 150 + int(70 * random())
    pyautogui.moveTo(x_point, y_point)

    play_view = ImageGrab.grab(bbox=(1120, 35, 1620, 365))
    text_area = play_view.crop(box=(10, 0, 290, 30))

    text = read_text_from_image(text_area)
    print(text)

    valid_words = ['Bank', 'Booth']

    for word in valid_words:
      if word in text:
        pyautogui.click()
        time.sleep(3 + random())
        return True
  return False

def store_all_items_and_take_one_item(item: str):
  open_bank_window()
  if item == 'tuna':
    pyautogui.moveTo(1550, 350)
    pyautogui.click()
    time.sleep(1.5 + random())
    pyautogui.moveTo(1480, 160)
    pyautogui.click(button='right')
    time.sleep(0.6 + random())
    pyautogui.move(0, 110)
    time.sleep(0.3 + random())
    pyautogui.click()
    time.sleep(1 + random())
    pyautogui.moveTo(1595, 40)
    pyautogui.click()
    time.sleep(1 + random())



if __name__ == "__main__":
  store_all_items_and_take_one_item('tuna')