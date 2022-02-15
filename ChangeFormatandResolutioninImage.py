
import cv2
import numpy as np

def save(path, image, jpg_quality = None, png_compress = None):

    if jpg_quality:
        cv2.imwrite(path, image, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])
    elif png_compress:
        cv2.imwrite(path, image, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compress])
    else:
        cv2.imwrite(path, image)

def main():
    impath = "image.jpg"
    img = cv2.imread(impath)

    cv2.imshow("image",img)

    last_jpeg = "image2JPG.jpg"
    kaydet(last_jpeg, img, jpg_quality = 60)

    last_png = "image2PNG.png"
    kaydet(last_png, img, png_compress = 3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()
