import cv2

aruco = cv2.aruco
def main():
    cv2.namedWindow('Marker',cv2.WINDOW_AUTOSIZE)
    cap = cv2.VideoCapture(1)
    
    dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    param = aruco.DetectorParameters()

    while(1):
        ret, frame = cap.read()
        corners,ids,rejectedCandidates = aruco.detectMarkers(frame,dict,parameters=param)
        img= aruco.drawDetectedMarkers(frame,corners,ids)
        cv2.imshow("Marker",img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
