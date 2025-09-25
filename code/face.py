import cv2
face_cascade_path = './haarcascade_frontalface_default.xml'

def face_detection(src):
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(src_gray)
    for x, y, w, h in faces:
        cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = src[y: y + h, x: x + w]
        face_gray = src_gray[y: y + h, x: x + w]

    return src

def main():
    cv2.namedWindow('frame',cv2.WINDOW_AUTOSIZE)
    cap = cv2.VideoCapture(0)

    while(1):
        ret, frame = cap.read()
        result = face_detection(frame)#Face detetion
        cv2.imshow('frame',result)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
