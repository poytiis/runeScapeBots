from PIL import ImageGrab, ImageStat
import autopy
import time

def main():
  
  for i in range(0,50000):
    print(i)
    maining = False

    # set Runescape client to right top corner 
    pic = ImageGrab.grab(bbox=(1100, 35, 1920, 600))

  
    #  2 rocks in desert, face to south
    rock_1 = pic.crop(box=(260, 205, 300, 230))
    rock_2 = pic.crop(box=(210, 170, 255, 190))
    last_space = pic.crop(box=(730, 402, 740, 409))

    stat_rock_1 = ImageStat.Stat(rock_1)
    stat_rock_2 = ImageStat.Stat(rock_2)
    stat_space = ImageStat.Stat(last_space)
      
    if stat_space.mean[2] < 20:
      empty_bag()

    if stat_rock_1.mean[2] < 20:
     
      autopy.mouse.move(1100 + 281, 35 + 215)
      autopy.mouse.click()
      autopy.mouse.click()
      autopy.mouse.move(1100 + 280, 35 + 160)
      maining = True
    

    if stat_rock_2.mean[2] < 20 and not maining:
    
      autopy.mouse.move(1100 + 230, 35 + 183)
      autopy.mouse.click()
      autopy.mouse.click()
      autopy.mouse.move(1100 + 280, 35 + 160)
      maining = True

    if maining:
      time.sleep(2)
    else: 
      time.sleep(0.4)


def empty_bag():

  for i in range (0, 5):
    for j in range(0, 4):

      autopy.mouse.move(1100 + 610 + j*40, 35 + 250 + 40*i)    
      autopy.mouse.click(button=autopy.mouse.Button.RIGHT)
      time.sleep(0.1)
      autopy.mouse.smooth_move(1100 + 610 + j*40,  35 + 250 + 35+ 40*i)
      time.sleep(0.1)
      autopy.mouse.click()
      time.sleep(0.1)


if __name__ == "__main__":
  main()
  