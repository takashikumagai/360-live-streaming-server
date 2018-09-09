import flask
import GenericCamera

app = flask.Flask(__name__)

#cam = GenericCamera.GenericCamera('/dev/v4l/by-id/usb-Arashi_Vision_Insta360_Air-video-index0')
cam = GenericCamera.GenericCamera('/dev/video1')

@app.route('/')
def hello_world():
  return flask.render_template('page.html')

def gen(camera):
  while True:
    frame = camera.get_frame()
    yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_stream.mjpg')
def video_stream():
  global cam
  return flask.Response(gen(cam), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/js/<path:path>')
def send_js(path):
    return flask.send_from_directory('js', path)
