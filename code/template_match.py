import cv2
 
def main():
    cv2.namedWindow('StereoViewer',cv2.WINDOW_AUTOSIZE)
    rimg = cv2.imread('./img/Mandrill.png')
    limg = cv2.imread('./img/Mandrill.png')

    h = 50
    w = 50
    top=150
    left = 150
    bottom = top + h
    right =left + w
    
    template=rimg[top:bottom,left:right]#top:bottom,left,right
    cv2.rectangle(limg, (left,top),(right,bottom), (255, 255, 0), 2)
    
    result = cv2.matchTemplate(limg, template, cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    left_top = (max_loc[0], max_loc[1])
    right_bottom = (max_loc[0]+w, max_loc[1]+h)
    cv2.rectangle(rimg, left_top, right_bottom, (255, 255, 0), 2)
    img = cv2.hconcat([limg,rimg])

    cv2.imshow('StereoViewer',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
