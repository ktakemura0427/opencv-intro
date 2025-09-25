import cv2


def apply_roi(img):
    h, w, c = img.shape
    dst = img[0:int(h/2), 0:int(w/2)]  # top:bottom,left,right
    return dst


def main():
    img = cv2.imread('./img/Mandrill.png')
    dst = apply_roi(img)
    cv2.imshow('image', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
