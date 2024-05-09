import cv2
import numpy as np

def main():
    img = cv2.imread('./img/Mandrill.png')
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('image', gray)
    cv2.imwrite('./img/Mandrill_gray.png', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
