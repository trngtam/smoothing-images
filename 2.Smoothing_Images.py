#PHẦN 1: blur()
import cv2
import numpy as np
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Blurred Image', cv2.WINDOW_NORMAL)
im = cv2.imread('C:/Users/tran ngoc tam/Desktop/python/opencv.py/lena.JPG')
# scale_percent = 10
# height= int(im.shape[0]*scale_percent/100)
# width = int(im.shape[1]*scale_percent/100)
# img = cv2.resize(im,(height,width))
cv2.imshow('Original Image', im)
cv2.imshow('Blurred Image', cv2.blur(im,(5,5)))
cv2.waitKey(0)
cv2.destroyAllWindows()

#PHẦN 2: GaussianBlur()
import cv2
import numpy as np

cv2.namedWindow("Gaussian Smoothing",cv2.WINDOW_NORMAL)
src= cv2.imread('C:/Users/tran ngoc tam/Desktop/python/opencv.py/lena.JPG')
dst = cv2.GaussianBlur(src,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow("Gaussian Smoothing",cv2.resize(dst,(500,500)))
cv2.waitKey(0)
cv2.destroyAllWindows()

#PHẦN 3: medianBlur()
import cv2
import numpy as np
# cv2.namedWindow("blur", cv2.WINDOW_NORMAL)
cv2.namedWindow("blur", cv2.WINDOW_FULLSCREEN)
img= cv2.imread('C:/Users/tran ngoc tam/Desktop/python/opencv.py/lena.JPG',1)
img2=cv2.resize(img,(500,500))
dst = median= cv2.medianBlur(img2,5)

cv2.imshow("blur",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
