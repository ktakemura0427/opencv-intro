import cv2

def arGenrator(dictionary):
    fileName = "./img/ar.png"
    generator = cv2.aruco.generateImageMarker(dictionary,0,150)
    cv2.imwrite(fileName,generator)
    img = cv2.imread(fileName)
    return img
    
def main():
    cv2.namedWindow('Marker',cv2.WINDOW_AUTOSIZE)
    dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    img=arGenrator(dict)
    cv2.imshow("Marker",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
