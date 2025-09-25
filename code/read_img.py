import cv2
 
def main():
    cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)#Set window name
    img = cv2.imread('./img/Mandrill.png')#Read image file
    cv2.imshow('image',img)#Show image file
    cv2.waitKey(0)#Wait
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
