import cv2
import numpy as np

image = cv2.imread("image.jpg")
image2 = cv2.imread("image2.jpg")

sum = cv2.add(image, image2)                         #Adds pictures together equally.
sum2 = cv2.addWeighted(image, 0.2, image2, 0.8, 0)      #Adds pictures together according to conditions.

cv2.imshow("New Image",sum)
cv2.imshow("New Image2",sum2)

cv2.waitKey(0)
cv2.destroyAllWindows()
