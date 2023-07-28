import canny
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt


def main():
    reflective_arr = []
    for filename in os.listdir("./reflective"):
        # Read image, detect edges, and show
        img = cv2.imread("./reflective/"+filename, cv2.IMREAD_GRAYSCALE)
        binary_mask = cv2.imread("./binaryMask.jpg", cv2.IMREAD_GRAYSCALE)
        img_blur = cv2.GaussianBlur(img, (3,3), 3)
        img_canny = canny.canny(img_blur,20,20)
        img_masked = cv2.bitwise_and(img_canny, binary_mask)

        reflective_arr.append(np.sum(img_masked&1))
        print(np.sum(img_masked&1))

    matte_arr = []
    for filename in os.listdir("./matte"):
        # Read image, detect edges, and show
        img = cv2.imread("./matte/"+filename, cv2.IMREAD_GRAYSCALE)
        binary_mask = cv2.imread("./binaryMask.jpg", cv2.IMREAD_GRAYSCALE)
        img_blur = cv2.GaussianBlur(img, (3,3), 3)
        img_canny = canny.canny(img_blur,20,20)
        img_masked = cv2.bitwise_and(img_canny, binary_mask)

        matte_arr.append(np.sum(img_masked&1))
        print(np.sum(img_masked&1))


    print(reflective_arr)
    print(matte_arr)


    
if (__name__=="__main__"):
    main()