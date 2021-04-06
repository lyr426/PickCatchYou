# -*- coding: utf-8 -*-
import cv2
import camera

######### 얼굴 등록할 때 카메라 켜지는 기능 


class Save(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        if self.video.isOpened() == False:
            return None


    def __del__(self):
        self.video.release()

    def get_frame2(self):
        ret, frame = self.video.read()

        if frame is None:
            print("frame open the cam")
            return None 

        return frame

    def get_frame(self):
        ret, frame = self.video.read()

        if frame is None:
            print("frame open the cam")
            return None 

        sucess, jpeg = cv2.imencode('.jpg', frame)
            
        return jpeg.tobytes()


        
if __name__ == '__main__':
    save = Save()

    frame = save.get_frame2()

    while True:
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    cv2.destroyAllWindows()
    