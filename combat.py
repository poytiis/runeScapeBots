import pyautogui
from PIL import ImageGrab, Image
import numpy as np
import cv2
import math
from tesseract import read_text_from_image
import time


def main():
    is_fighting = False
    failed_rounds = 0
    for _ in range(0, 500):
        if not is_fighting:
            target_found = find_target()
            if target_found:
                is_fighting = True
            failed_rounds +=1
        else:
            target_health = check_target_health()
            if target_health == False or target_health == 0:
                is_fighting = False
        
        if failed_rounds > 5:
           failed_rounds = 0
           with pyautogui.hold('left'):
               time.sleep(0.3)
        else:
            time.sleep(0.5)


def check_target_health():
    screen = ImageGrab.grab(bbox=(910, 0, 1900, 620))
    play_view = screen.crop(box=(0, 30, 650, 450))
    health_bar = play_view.crop(box=(18,66,167,87))

    health_text = read_text_from_image(health_bar)
    print(health_text)
    if health_text == '':
       return False
    elif health_text[0] == 'o' or health_text[0] == '0':
       return 0
    else:
        return 1
   
def find_target():
    screen = ImageGrab.grab(bbox=(910, 0, 1900, 620))
    play_view = screen.crop(box=(0, 30, 650, 450))

    play_view_numpy = np.array(play_view)
    play_view_cv2 = cv2.cvtColor(play_view_numpy, cv2.COLOR_RGB2BGR)

    play_view_hsv  = cv2.cvtColor(play_view_numpy, cv2.COLOR_RGB2HSV)

    lower_pink = np.array([150,100,100])
    upper_pink = np.array([160,255,255])

    # Threshold the HSV image to get only pink colors
    target_borders = cv2.inRange(play_view_hsv, lower_pink, upper_pink)

    contours, _ = cv2.findContours(target_borders, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    player_location = [300, 200]
    shortest_distance = 1000000
    shortest_location = [0,0]

    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 80:
            continue
        M = cv2.moments(contour)
        if M['m00'] == 0 or M['m00'] == 0:
           continue
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
       
        distance = math.dist([cx, cy], player_location)
        if distance < shortest_distance:
           shortest_location = [cx, cy]
           shortest_distance = distance

    if shortest_distance != 1000000:
        pyautogui.moveTo(910 + shortest_location[0], 30 + shortest_location[1])
        pyautogui.click()
        return True
    
    return False
       

if __name__ == "__main__":
  main()