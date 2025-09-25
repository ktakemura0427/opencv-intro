import cv2


def click_pos(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixelvalue = img[y, x]
        color_str = 'color=('+str(pixelvalue)+')'
        print(color_str)


if __name__ == '__main__':
    img = cv2.imread('./img/Mandrill.png')
    cv2.imshow('window', img)
    cv2.setMouseCallback('window', click_pos)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
