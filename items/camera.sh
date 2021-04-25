#!/bin/sh

if [ $1 = "start" ]; then
    ps -ef | grep mjpg_streamer | grep -v grep || /home/pi/mjpg-streamer/mjpg-streamer-experimental/mjpg_streamer -o "/home/pi/mjpg-streamer/mjpg-streamer-experimental/output_http.so -w /home/pi/www" -i "/home/pi/mjpg-streamer/mjpg-streamer-experimental/input_raspicam.so -x 640 -y 480 -fps 30 -q 10" &
else
    pkill mjpg_streamer
fi