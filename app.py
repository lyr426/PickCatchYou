# app.py

from flask import Flask, render_template, Response, request

import sys
import face_recog
import save_img
import capture
import cv2

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    print(2)
    return render_template('index.html')



def gen(fr):
    while True:
        jpg_bytes = fr.get_jpg_bytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n\r\n')

def gene(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(face_recog.FaceRecog()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/cap_img')
def cap_img():
    return Response(gene(save_img.Save()), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/cap')
def cap():
    #sys.setrecursionlimit(10**5)
    return Response(capture.capture())
    #cap_img = capture()


@app.route('/face_register')
def face_register():
    return render_template('face_register.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
