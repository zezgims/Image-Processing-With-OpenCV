
import cv2

def main():
    image = cv2.imread("image.jpg")
    screen_resolution = 640,480

    scale_width = screen_resolution[0]/image.shape[1]
    scale_height = screen_resolution[1]/image.shape[0]
    scale = min(scale_width, scale_height)

    window_width = int(image.shape[1]*scale)
    window_height = int(image.shape[0]*scale)

    cv2.namedWindow("Resizable Window", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Resizable Window", window_width, window_height)

    cv2.imshow("Resizable Window",image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__=="__main__":
    main()
