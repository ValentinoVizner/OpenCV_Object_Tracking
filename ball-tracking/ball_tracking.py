from collections import deque
from imutils import VideoStream
import numpy as np
import argparse
import cv2
import time
import os

os.putenv("DISPLAY", ":1.0")
"""
list-like data structure with super fast appends and pops to maintain a list of the past N (x, y)-locations of the ball in our video stream. 
Maintaining such a queue allows us to draw the “contrail” of the ball as its being tracked.
"""
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument(
    "-v",
    "--video",
    help="/home/vaba/Desktop/podatci/Python/Python_PyImageSearch_DL4Cv/Day_5_Object_Tracking/ball-tracking/",
)
ap.add_argument("-b", "--buffer", type=int, default=64, help="max buffer size")
args = vars(ap.parse_args())


# python ball_tracking.py --video ball_tracking_example.mp4
