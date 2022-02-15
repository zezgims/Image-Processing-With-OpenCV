
import cv2
import numpy as np

image = np.zeros((500,500,3), dtype="uint8")

cv2.rectangle(image, (10,10),(490,490),(0,180,180),2)
cv2.line(image, (10,10),(490,490),(180,0,180),2)
cv2.line(image, (10,250),(490,250),(50,0,250),2)
cv2.circle(image, (255,255),(50),(0,200,0),2)

cv2.imshow("Black Screen", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
