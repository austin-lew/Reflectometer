import numpy as np
import scipy
import math
import skimage

# Define convolution kernels
sobel_x = np.array([[1,   0, -1],
                    [2,   0, -2], 
                    [1,   0, -1]])

sobel_y = np.array([[1,   2,  1],
                    [0,   0,  0],
                    [-1, -2, -1]])

def canny(img, thresh_high, thresh_low):
    img_sobel_x, img_sobel_y = sobel(img)
    img_nms = nms(img_sobel_x, img_sobel_y)
    img_thresh = thresh(img_nms, thresh_high, thresh_low)

    img_canny = img_thresh

    return img_canny

def sobel(img):
    # Perform convolutions with x and y kernels
    img_sobel_x = scipy.signal.fftconvolve(img, sobel_x)
    img_sobel_y = scipy.signal.fftconvolve(img, sobel_y)

    return img_sobel_x, img_sobel_y

def nms(img_sobel_x, img_sobel_y):
    angles = np.arctan(img_sobel_y/img_sobel_x)
    norms = getNorm(img_sobel_x, img_sobel_y)

    for y, x in np.ndindex(norms.shape):
        # Exclude pixels on edge of image
        if (x==0 or y==0 or x==np.size(norms, 1)-1 or y==np.size(norms, 0)-1):
            pass
        else:
            theta = angles[y][x]%(math.pi/4) # The angle between the gradient and the clockwise pixel
            n = angles[y][x]/(math.pi/4) # The index of our pixel

            alpha = theta/(math.pi/4) # Constant used for interpolation
            # We have four conditionals (since there are eight neighbours per pixel)
            if (n==0):
                p0 = norms[y][x+1]
                p1 = norms[y-1][x+1]

                p2 = norms[y][x-1]
                p3 = norms[y+1][x-1]
            elif (n==1):
                p0 = norms[y-1][x+1]
                p1 = norms[y-1][x]

                p2 = norms[y+1][x-1]
                p3 = norms[y+1][x]
            elif (n==2):
                p0 = norms[y-1][x]
                p1 = norms[y-1][x-1]

                p2 = norms[y+1][x]
                p3 = norms[y+1][x+1]
            else:
                p0 = norms[y-1][x-1]
                p1 = norms[y][x-1]

                p2 = norms[y+1][x+1]
                p3 = norms[y][x+1]

            head = interpolate(p0, p1, alpha)
            tail = interpolate(p2, p3, alpha)

            # Perform non-max suppression
            if (norms[y][x] >= head and norms[y][x] >= tail):
                pass
            else:
                norms[y][x]=0 # If pixel is not the max along its gradient, suppress it 

    return norms

def getNorm(x,y):
    # Find the norm of the gradient at each pixel
    norm = np.sqrt(np.add(np.square(x), np.square(y)))

    # Normalize to 8 bit and return
    return np.multiply(norm, 255/math.sqrt(255*255*16*2))

def thresh(img, thresh_high, thresh_low):
    # Set all pixels below thresh_low to zero
    img_thresh = skimage.filters.apply_hysteresis_threshold(img, thresh_low, thresh_high)*255
    img_thresh = img_thresh.astype(np.uint8)
    return img_thresh

def interpolate(p0, p1, alpha):
    return ((1-alpha)*p0 + alpha*p1)