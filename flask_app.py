from unittest import skip
from flask import Flask, render_template, Response, request
import cv2
app = Flask(__name__)

def gen_frames1(cameral):  
    while True:
        success, frame = cameral.read()
        if not success:
            continue
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 

@app.route('/video_feed1/<string:data>')
def video_feed1(data):
    camera1 = cv2.VideoCapture('rtsp://'+data+'/ISAPI/Streaming/channels/101/httpPreview')
    return Response(gen_frames1(camera1), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed2/<string:data>')
def video_feed2(data):
    camera1 = cv2.VideoCapture('rtsp://'+data+'/ISAPI/Streaming/channels/202/httpPreview')
    return Response(gen_frames1(camera1), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed3/<string:data>')
def video_feed3(data):
    camera1 = cv2.VideoCapture('rtsp://'+data+'/ISAPI/Streaming/channels/302/httpPreview')
    return Response(gen_frames1(camera1), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed4/<string:data>')
def video_feed4(data):
    camera1 = cv2.VideoCapture('rtsp://'+data+'/ISAPI/Streaming/channels/402/httpPreview')
    return Response(gen_frames1(camera1), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stream', methods=['POST'])
def stream():
    return render_template('stream.html', meta= f"{request.form['username']}:{request.form['password']}@{request.form['ip']}:{request.form['port']}")

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)