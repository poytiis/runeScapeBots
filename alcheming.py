import time
import pyautogui
from random import seed, random

def main():
  seed(1)
  time.sleep(5)
  for _ in range(0, 6 * 50000):
    time.sleep(0.2 + 0.8 * random()) 
    pyautogui.leftClick()
    time.sleep(0.2 + 0.8 * random()) 

if __name__ == "__main__":
  main()