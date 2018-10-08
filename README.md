# 360° Camera Live Streaming on the Web
This is a demo app which serves a 360° live streaming video on the web over http. In principle, it should be compatible with any 360° cameras which meet these conditions:
- Available as a v4l (Video 4 Linux) device.
- Outputs a dual-fisheye video stream

# Background
Many 360 cameras on the market come bundled with proprietary software packages that allow users to stream videos on well-established platforms such as YouTube. If you want to stream a video on your own website, however, things are not straightfoward. One typical scenario is a linux server + serving live stream from /dev/video*. This application is intended to provide a minimalist package for this.

# System Requirements
## Hardware
- A spherical camera capable of live streaming video in the fisheye format. 
- PC or PCs compatible with the spherical camera
- Note that client and the server can be the same computer

## Software
- Linux PC for the server.
- Python3 and the following Python libraries (server)
  - Flask
  - OpenCV
- A browser (client)

