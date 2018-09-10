# 360-live-streaming-server
This is a demo app which serves a live streaming video on the web over http. In principle, it should be compatible with any 360 cameras which meet these conditions:
- Conforms to v4l (Video 4 Linux).
- Outputs a dual-fisheye video stream

# Background
Many 360 cameras on the market come bundled with priorietary software packages that allow users to stream videos on well-established platforms such as YouTube. If you want to stream a video on your own website, however, things are not straightfoward. Here, by 'your own website', I mean a website you make by coding frontend and backend yourself. One typical scenario is to build a linux server and stream a video from a camera interfaced as a v4l (Video for Linux) device, i.e. /dev/video* file. This application is intended to provide a minimalist package for such a scenario.
