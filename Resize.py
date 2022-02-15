
import cv2

image = cv2.imread("image.jpg")

up = cv2.pyrUp(image) 
down = cv2.pyrDown(image)

cv2.imshow("Orijinal", image)
cv2.imshow("Up", up)
cv2.imshow("Down", down)

cv2.waitKey(0)
cv2.destroyAllWindows()
