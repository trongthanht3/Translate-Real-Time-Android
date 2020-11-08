from imutils.object_detection import  non_max_suppression
import numpy as np
import argparse
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str,
                help="path to input image")
ap.add_argument("-east", "--east", type=str,
                help="path to input EAST text detector models")
ap.add_argument("-c", "--min-confidence", type=float, default=0.5,
                help="minium probability required to inspect a region/threshold to determine text")
ap.add_argument("-w", "--width", type=int, default=320,
                help="resized image width (should be multiple to 32)")
ap.add_argument("-e", "--height", type=int, default=320,
                help="resized image height (should be multiple to 32)")
args = vars(ap.parse_args())

#load input and grab dimensions
image = cv2.imread(args["image"])
orig = image.copy()
(H,W) = image.shape[:2]

#set new width and height then determine the ration in change for both
(newH, newW) = (args["height"], args["width"])
rH = H / float(newH)
rW = W / float(newW)

#resize image and grab new dimensions
image = cv2.resize(image, (newW, newH))

#define 2 output layers names for EAST
#first is the output probabilities
#second can be use to derive the bounding box coordinates of text
layerNames = {
    "feature_fusion/Conv_7/Sigmoid",
    "feature_fusion/concat_3"
}
