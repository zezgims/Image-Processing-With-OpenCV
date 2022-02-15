
import cv2
import numpy as np

image = cv2.imread("messi.jpg")
image2 = cv2.imread("logo.jpg")

satir, sutun, kanal = resim2.shape
roi = resim1[0:satir,0:sutun]

resim2gri = cv2.cvtColor(resim2,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gri Logo",resim2gri)

ret, mask = cv2.threshold(resim2gri,10,255,cv2.THRESH_BINARY)
cv2.imshow("Maske",mask)

maskTers= cv2.bitwise_not(mask)
cv2.imshow("Maskenin Tersi",maskTers)

resim1_bg = cv2.bitwise_and(roi,roi,mask = maskTers)
cv2.imshow("resim1_bg",resim1_bg)

resim2_fg =cv2.bitwise_and(resim2,resim2,mask = mask)
cv2.imshow("im2_fg",resim2_fg)

son_resim = cv2.add(resim1_bg,resim2_fg)
resim1[0:satir,0:sutun] = son_resim

cv2.imshow("son resim",resim1)


cv2.waitKey(0)
cv2.destroyAllWindows()
