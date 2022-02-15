
import cv2
import numpy as np

image = cv2.imread("image.jpg")     
grey = cv2.imread("image.jpg", 0)   
ret, black = cv2.threshold(grey, 100, 255, cv2.THRESH_BINARY)   

#Converting image to black and white with non-ready function

x, y = grey.shape      
black2 = np.zeros((x,y), "uint8")

threshold = 100

for i in range(0,x):
    for j in range(0,y):
        if(grey[i][j] <= threshold):
            black2[i][j] = 0
        else:
            black2[i][j] = 255

cv2.imshow("Black and White Image",black)
cv2.imshow("Black and White Image2",black2)

cv2.waitKey(0)
cv2.destroyAllWindows()
