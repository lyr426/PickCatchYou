import cv2
import sys

######## 얼굴 등록 할 때 사용되는 코드 --> 이미지 캡쳐 

def capture():

    cam = cv2.VideoCapture(0)

    if cam.isOpened() == False:
        return None

    ret, frame = cam.read()
    if frame is None:
        print ('frame is not exist')
        return None
    
    cv2.imwrite('knowns/username.jpg',frame, params=[cv2.IMWRITE_PNG_COMPRESSION,0]) #username 불러와서 저장 



    cam.release()

if __name__ == '__main__':
    capture()