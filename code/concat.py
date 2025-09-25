import cv2
 
def main():
    cv2.namedWindow('Viewer',cv2.WINDOW_AUTOSIZE)
    rimg = cv2.imread('./img/Mandrill.png')
    limg = cv2.imread('./img/Mandrill.png')
    img = cv2.hconcat([limg,rimg])
    cv2.imshow('Viewer',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
