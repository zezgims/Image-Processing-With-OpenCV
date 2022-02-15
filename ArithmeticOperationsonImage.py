
import cv2

image = cv2.imread("image.jpg")

image[80,80] = [255,255,255]

part = image[155:495,125:490]

image[0:340,0:365] = part
cv2.rectangle(image, (125,155),(490,495),(0,0,255),5)

cv2.imshow("Image", image)
cv2.imshow("Part", partpart)

cv2.waitKey(0)
cv2.destroyAllWindows()
