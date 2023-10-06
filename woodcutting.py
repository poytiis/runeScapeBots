from PIL import Image, ImageGrab, ImageStat
import autopy
import time

def main():

  for i in range(0,1):

    # set Runescape client to right top corner 
    pic = ImageGrab.grab(bbox=(750, 35, 1920, 750))
    pic.save('./pics/screen2.png')

    # corner_map = pic.crop(box=(600, 5, 745, 175))
    # corner_map.save('./pics/map3.png')


def find_willows():
  pass

if __name__ == "__main__":
  main()