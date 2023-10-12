from PIL import Image, ImageGrab, ImageStat
import autopy
import time

def main():

  for i in range(0,1):

    # set Runescape client to right top corner 
    pic = ImageGrab.grab(bbox=(750, 35, 1920, 750))
    pic.save('./pics/screen2.png')



if __name__ == "__main__":
  main()