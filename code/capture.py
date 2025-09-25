import cv2
 
def main():
    cv2.namedWindow('frame',cv2.WINDOW_AUTOSIZE)
    cap = cv2.VideoCapture(0)

    while(1):
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
