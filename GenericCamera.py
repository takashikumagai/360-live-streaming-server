#!/usr/bin/env python3

import cv2

class GenericCamera:

  def __init__(self,device_path = None):
    device_path_to_use = device_path if device_path is not None else '/dev/video0'
    print('Setting up video capture. Camera: {}'.format(device_path_to_use))
    self.cap = cv2.VideoCapture(device_path_to_use)
    #self.cap = cv2.VideoCapture('/dev/v4l/by-id/usb-Arashi_Vision_Insta360_Air-video-index0')
    #self.cap = cv2.VideoCapture(1)

  def get_frame(self):
    ret, frame = self.cap.read()
    #print('frame: {}'.format(frame))
    #print('frame size: {}'.format(len(img)))
    return cv2.imencode('.jpg', frame)[1].tobytes()
    #return frame

  def test_video(self):
    while(True):
      ret, frame = self.cap.read()

      # Our operations on the frame come here
      #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

      #cv2.imshow('frame',gray)
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Release the capture
    print('Releasing the capture')
    self.cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
  cam = GenericCamera()
  cam.test_video()
