import pyautogui
from PIL import ImageGrab
import numpy as np
import cv2
import math


def main():
    is_fighting = False
    if not is_fighting:
       find_target()
    pass

def find_target():
    screen = ImageGrab.grab(bbox=(910, 0, 1900, 620))
    play_view = screen.crop(box=(0, 30, 650, 450))
    play_view.save('./pics/a.png')

    play_view_numpy = np.array(play_view)
    play_view_cv2 = cv2.cvtColor(play_view_numpy, cv2.COLOR_RGB2BGR)

    play_view_hsv  = cv2.cvtColor(play_view_numpy, cv2.COLOR_RGB2HSV)

    lower_pink = np.array([150,100,100])
    upper_pink = np.array([160,255,255])

    # Threshold the HSV image to get only pink colors
    target_borders = cv2.inRange(play_view_hsv, lower_pink, upper_pink)

    contours, _ = cv2.findContours(target_borders, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    img = cv2.drawContours(play_view_cv2, contours, -1, (0,255,0), 3)

    player_location = [300, 200]
    shortest_distance = 1000000
    shortest_location = [0,0]

    for contour in contours:
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
       

if __name__ == "__main__":
  main()