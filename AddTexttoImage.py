
import cv2
import numpy as np

image = cv2.imread("image.jpg")
cv2.putText(image, "OPEN CV", (180,100), cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(200,0,0))

cv2.imshow("Image ",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
