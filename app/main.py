import cv2 as cv
from constants import BLACK, FONTS, GREEN, KNOWN_DISTANCE_CM, MOBILE_WIDTH_CM, MOBILE_WIDTH_IN_RF
from utils.estimator import draw_rectangle_and_label, estimate_distance, find_focal_length, record_objects

# Function to set up camera and video recorder
def setup_camera_and_recorder():
    cap = cv.VideoCapture(0)  # Initialize the camera (0 indicates the default camera)
    fourcc = cv.VideoWriter_fourcc(*"XVID")  # Video codec for the recorder
    recorder = cv.VideoWriter(
        "out.mp4",
        fourcc,
        8.0,  # Frames per second
        (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))),  # Frame size
    )
    return cap, recorder

# Main function
def main():
    cap, recorder = setup_camera_and_recorder()  # Initialize camera and recorder
    focal_mobile = find_focal_length(KNOWN_DISTANCE_CM, MOBILE_WIDTH_CM, MOBILE_WIDTH_IN_RF)  # Calculate focal length

    while True:
        _, frame = cap.read()  # Read a frame from the camera
        response_data = record_objects(frame)  # Detects and records objects in the frame

        for data in response_data:
            name = data[0]  # Get the name of the detected object

            if name == "cell phone":
                distance = estimate_distance(focal_mobile, MOBILE_WIDTH_CM, data[1])  # Estimate the distance to the cell phone
                x, y = data[2]  # Get the coordinates of the object

            # Log results for monitoring and analysis (to be implemented)
            # logger(name, round(distance, 2))

            # Add distance information to the object if it's a cell phone
            cv.rectangle(frame, (x, y - 3), (x + 150, y + 23), BLACK, -1)  # Draw a rectangle for the distance text background
            cv.putText(
                frame,
                f"Distance: {round(distance, 2)} cm",  # Display the distance on the frame
                (x + 5, y + 13),
                FONTS,
                0.48,
                GREEN,
                2,
            )

        cv.imshow("frame", frame)  # Display the frame
        recorder.write(frame)  # Write the frame to the video recorder

        key = cv.waitKey(1)
        if key == ord("q"):  # Exit the loop if the 'q' key is pressed
            break

    cap.release()  # Release the camera
    recorder.release()  # Release the video recorder
    cv.destroyAllWindows()  # Close all OpenCV windows

if __name__ == "__main__":
    main()  # Execute the main function if this script is run directly
