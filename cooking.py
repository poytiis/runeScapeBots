from PIL import Image, ImageGrab, ImageStat
import autopy
import time
import cv2
import numpy

def main():
  
  for i in range(0,1):
    print(i)
    pic = ImageGrab.grab(bbox=(1100, 35, 1920, 600))
    # pic.save('./pics/view.png')
    corner_map = pic.crop(box=(600, 5, 745, 175))
    range_pic = corner_map.crop(box=(51,69, 65, 82))
    # range_pic.save('./pics/range_icon.png')
  
    c = corner_map.convert('RGB')   
    open_cv_image = numpy.array(c) 
    open_cv_image = open_cv_image[:, :, ::-1].copy() 
    cv2.imwrite('./pics/shot.png',open_cv_image)
    range_icon = cv2.imread('./pics/range_icon.png')
    templ = cv2.imread('./pics/range_icon.png')
    view = cv2.imread('./pics/view.png')
    view = open_cv_image
    result = cv2.matchTemplate(view, templ, cv2.TM_SQDIFF_NORMED)
    # cv2.imshow('after matching',result)
    # cv2.waitKey(0)
    cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )
    _minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(result, None)
    matchLoc = minLoc
    print(matchLoc)

    img_display = view.copy()
    

    image_window = "Source Image"
    result_window = "Result window"
    cv2.rectangle(img_display, matchLoc, (matchLoc[0] + templ.shape[0], matchLoc[1] + templ.shape[1]), (0,0,0), 2, 8, 0 )
    cv2.rectangle(result, matchLoc, (matchLoc[0] + templ.shape[0], matchLoc[1] + templ.shape[1]), (0,0,0), 2, 8, 0 )
    cv2.imshow(image_window, img_display)
    cv2.imshow(result_window, result)
    cv2.imwrite('./pics/result.png', result)

    cv2.waitKey(0)
    return 0
    



if __name__ == "__main__":
  main()