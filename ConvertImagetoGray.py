
import cv2
import numpy as np

image = cv2.imread("image.jpg")     
grey = cv2.imread("image.jpg", 0)           

cv2.imshow("Image", image)
cv2.imshow("Grey Image", grey)

#Converting image to gray with non-ready function.

x,y = image.shape[:2]       
grey2 = np.zeros((x,y), "uint8")   

for i in range(0,x):
    for j in range(0,y):
        sum = 0
        for k in range(0,3):
            sum += image[i][j][k]

        pixel = sum/3   
        grey2[i][j] = pixel

cv2.imshow("Grey Image2", grey2)

cv2.waitKey(0)
cv2.destroyAllWindows()
