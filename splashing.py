import time
import pyautogui
from random import seed, random

def main():
  seed(1)
  time.sleep(5)
  for _ in range(0, 6 * 5000):   
    with pyautogui.hold('left'):
      pyautogui.sleep(5 * random())

    time.sleep(60 * 10 + 20 * random())

if __name__ == "__main__":
  main()