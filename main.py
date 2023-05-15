import numpy as np
import cv2

# Set confidence and NMS thresholds

# Path to model configuration and weights files
modelConfiguration = 'cfg/yolov3.cfg'
modelWeights = 'yolov3.weights'

# Path to labels file
labelsPath = 'coco.names'

# Load labels from file
labels = open(labelsPath).read().strip().split('\n')

# Load YOLO object detection network


# Load image
image = cv2.imread('static/img1.jpg')

# Get image dimensions


# Create blob from image and set input for YOLO network
# Syntax: blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size)
# 1/255 is takes to normalise the pixel value from 0-255 to 0-1 as the yolo (other models also) require the pixel to be in range 0 to 1.
# 416,416 is size of images taken by yolo model


# Get names of unconnected output layers


# Forward pass through network



# Initialize lists to store bounding boxes, confidences, and class Ids
boxes = []
confidences = []
classIds = []

# Process each output from YOLO network


        # Get class scores and ID of class with highest score
        

        # If confidence threshold is met, save bounding box coordinates and class Id
        

# Apply Non Maxima Suppression to remove overlapping bounding boxes
indexes =[]

font = cv2.FONT_HERSHEY_SIMPLEX
for i in range(len(boxes)):
    if i in indexes:
        x = boxes[i][0]
        y = boxes[i][1]
        w = boxes[i][2]
        h = boxes[i][3]

        label = labels[classIds[i]]

        # default red color
        color = (0, 0, 255)
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
        text = '{}: {:.2f}'.format(label, confidences[i]*100)
        cv2.putText(image, text, (x, y - 5), font, 1, color, 1)


# Display image with bounding boxes and labels
cv2.imshow('Image', image)
cv2.waitKey(0)
