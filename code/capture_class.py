import cv2

class Application:
    def __init__(self,device_num):
        print('constructor')
        self.cap = cv2.VideoCapture(device_num)


    def __del__(self):
        print('destructor')
        self.cap.release()
        cv2.destroyAllWindows()


    def run(self):
        while(1):
            ret, frame = self.cap.read()
            cv2.imshow('image',frame)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break


if __name__ == '__main__':
    app=Application(0)
    app.run()
