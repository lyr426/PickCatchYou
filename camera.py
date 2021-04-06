# camera.py

import cv2

####### 얼굴 인식 시작할 때 카메라 키는 작동

class VideoCamera(object):
   
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()
        return frame


if __name__ == '__main__':

    cam = VideoCamera()
    
    while True:
        frame = cam.get_frame()
    
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"): #q누르면 종료 
            break

    cv2.destroyAllWindows() #반환
    print('finish')
