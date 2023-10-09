import cv2 as cv

# Distance Constants
KNOWN_DISTANCE_CM = 30  # Known distance for distance estimation
MOBILE_WIDTH_CM = 8  # Width of a mobile phone in centimeters
MINIMUM_OBJECT_SPACING_CM = 10  # Minimum spacing between detected objects in centimeters

# Width of the mobile phone in the reference frame
MOBILE_WIDTH_IN_RF = 270

# Object Detector Constants
CONFIDENCE_THRESHOLD = 0.4  # Confidence threshold for object detection
NMS_THRESHOLD = 0.3  # Non-maximum suppression threshold

# API Endpoints
YOLO_ENDPOINT = "http://localhost:8002/yolo/detect_objects/"

# colours for Detected Objects
COLOURS = [
    (255, 0, 0),
    (255, 0, 255),
    (0, 255, 255),
    (255, 255, 0),
    (0, 255, 0),
    (255, 0, 0),
]

# Colours
GREEN = (0, 255, 0)  # Green colour
BLACK = (0, 0, 0)  # Black colour

# Fonts
FONTS = cv.FONT_HERSHEY_COMPLEX  # Font for text on images
