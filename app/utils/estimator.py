import cv2 as cv
import requests
from PIL import Image
from app.constants import FONTS, MINIMUM_OBJECT_SPACING_CM, YOLO_ENDPOINT, COLOURS

def record_objects(frame):
    # Detect objects using YOLO and return the results as a list
    data = yolo_detect(frame, YOLO_ENDPOINT)
    response_list = []

    for box_fl, score, label in zip(data['bounding_boxes'], data['confidence_scores'], data['classes']):
        # Define color for each object based on its class
        colour = COLOURS[len(label) % len(COLOURS)]

        # Cast box floats to integers (cv2 requirement)
        box = list(map(int, box_fl))

        if label == "cell phone":
            response_list.append([label, box[2] - box[0], (box[0], box[1] - 2)])

        label = "%s : %f" % (label, score)

        # Draw rectangle and label on the object
        draw_rectangle_and_label(frame, box, label, colour)

    return response_list

def yolo_detect(frame, endpoint_url):
    # Encode the frame as JPEG
    _, img_encoded = cv.imencode(".jpg", frame)

    # Convert the encoded frame to bytes
    img_bytes = img_encoded.tobytes()

    try:
        # Send a POST request to the FastAPI endpoint with the frame data
        response = requests.post(
            endpoint_url, files={"file": ("frame.jpg", img_bytes, "image/jpeg")}
        )

        # Process the response if needed
        data = response.json()
        return data
    except Exception as e:
        raise Exception(f"Error sending request: {e}")

def draw_rectangle_and_label(frame, box, label, colour):
    cv.rectangle(frame, (box[0], box[1]), (box[2], box[3]), colour, 2)
    cv.putText(frame, label, (box[0], box[1] - 14), FONTS, 0.5, colour, 2)

def estimate_distance(focal_length, real_object_width, width_in_frame):
    distance = (real_object_width * focal_length) / width_in_frame
    return int(distance)

def find_focal_length(measured_distance, real_width, width_in_rf):
    focal_length = (width_in_rf * measured_distance) / real_width
    return focal_length

def handle_distance(label: str, distance):
    if distance < MINIMUM_OBJECT_SPACING_CM:
        body = {"name": label, "distance": distance}
        # response = requests.post(Logger.URL, json=body)
        # print(body)