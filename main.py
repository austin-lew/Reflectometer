import canny
import numpy as np
import cv2

def main():
    # Read image, detect edges, and show
    img = cv2.imread("test.jpg")
    img_blur = cv2.GaussianBlur(img, (3,3), 3)
    img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

    img_canny = canny.canny(img_gray,20,10)
    cv2.imshow("test.jpg", img_canny)
    cv2.waitKey(0)
    
if (__name__=="__main__"):
    main()