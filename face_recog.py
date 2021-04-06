# face_recog.py


########## 얼굴 인식 모델 
import face_recognition
import cv2
import camera
import os
import numpy as np

class FaceRecog():
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.camera = camera.VideoCamera()

        self.known_face_encodings = []
        self.known_face_names = []

        # Load sample pictures and learn how to recognize it.
        dirname = 'knowns'
        files = os.listdir(dirname)
        for filename in files:
            name, ext = os.path.splitext(filename)
            if ext == '.jpg':
                self.known_face_names.append(name)  #파일 이름에서 사람 이름 추출
                pathname = os.path.join(dirname, filename)
                img = face_recognition.load_image_file(pathname) #사진 파일에서 얼굴영역 인식
                face_encoding = face_recognition.face_encodings(img)[0] #얼굴 특징 위치 분석 데이터 저장
                self.known_face_encodings.append(face_encoding)

        # Initialize some variables
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True

    def __del__(self):
        del self.camera

    def get_frame(self):
        # Grab a single frame of video 카메라로 부터 frame을 읽음
        frame = self.camera.get_frame()

        # Resize frame of video to 1/4 size for faster face recognition processing --> 계산 양을 줄이기 위해 크기를 줄임
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if self.process_this_frame:
            # Find all the faces and face encodings in the current frame of video #읽은 frame에서 얼굴영역과 특징을 추출함 
            self.face_locations = face_recognition.face_locations(rgb_small_frame)
            self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations) 

            self.face_names = []
            for face_encoding in self.face_encodings:
                # See if the face is a match for the known face(s) 
                # #frame에서 추출한 얼굴 특징과 konwns파일안에 있는 얼굴들과 비교하여 거리(비슷한 척도)를 구함 
                distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                min_value = min(distances)

                # tolerance: How much distance between faces to consider it a match. Lower is more strict.
                # 0.6 is typical best performance.
                name = "Unknown"
                if min_value < 0.3: # 거리가 0.6이면 다른 사람의 얼굴  #거리가 0.6이하이면서 최소값을 가진 사람의 이름을 찾음 
                    index = np.argmin(distances)
                    name = self.known_face_names[index] 
                


                self.face_names.append(name)

        self.process_this_frame = not self.process_this_frame

        # Display the results --> 찾은 사람의 얼굴 영역과 이름을 비디오 화면에 띄움 
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            #얼굴 영역 표시 --> 인증 되면 파란색, 인증 안되면 빨간색 
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2) 

            if name == "username": 
                cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2) 
            else :
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2) 


            # 찾은 이름 표시 
            font = cv2.FONT_HERSHEY_DUPLEX
            if name == "username": 
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 0, 0), cv2.FILLED)
                cv2.putText(frame, "OK", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            else :
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                cv2.putText(frame, "X", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            #cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    

            ##########################
            # if name == user name :
            #       cv2.putText(frame, "OK", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            #            
            #else :
            #       cv2.putText(frame, "X", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


        return frame

    def get_jpg_bytes(self):
        frame = self.get_frame()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpg = cv2.imencode('.jpg', frame)
        return jpg.tobytes()


if __name__ == '__main__':
    face_recog = FaceRecog()
    print(face_recog.known_face_names)
    while True:
        frame = face_recog.get_frame()

        # show the frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

    # do a bit of cleanup
    cv2.destroyAllWindows()
    print('finish')
