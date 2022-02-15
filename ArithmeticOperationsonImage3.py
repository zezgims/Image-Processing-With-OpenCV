
import cv2
import numpy as np

image = cv2.imread("messi.jpg")
image2 = cv2.imread("logo.jpg")

line, column, canal = resim2.shape
roi = image[0:line, 0:column]

image2_grey = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey Logo", image2_grey)

ret, mask = cv2.threshold(image2_grey, 10, 255, cv2.THRESH_BINARY)
cv2.imshow("Mask", mask)

mask_reverse = cv2.bitwise_not(mask)
cv2.imshow("Reverse of Mask", mask_reverse)

image_bg = cv2.bitwise_and(roi, roi, mask = mask_reverse)
cv2.imshow("Image_bg", image_bg)

image2_fg = cv2.bitwise_and(image2, image2, mask = mask)
cv2.imshow("Image2_fg", image2_fg)

last_image = cv2.add(image_bg, image2_fg)
image[0:line, 0:column] = last_image

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
