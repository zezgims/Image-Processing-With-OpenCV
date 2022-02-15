
import cv2

image = cv2.imread("image.jpg", 0)
cv2.imshow("Image", image)
cv2.imwrite("Grey Image.jpg", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
