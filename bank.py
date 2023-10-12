from PIL import ImageGrab
from tesseract import read_text_from_image
import math
import pyautogui
import time
from random import seed, random

def store_all_items():
  pyautogui.moveTo(1550, 350)
  pyautogui.click()
  time.sleep(1.5)
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
        time.sleep(3)
        return True
  return False


if __name__ == "__main__":
  is_bank_open = open_bank_window()
  if is_bank_open:
    store_all_items()