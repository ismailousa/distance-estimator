# Object Distance Estimator with Live Object Detection

This project is a real-time object distance estimator that uses a live stream from your camera and detects objects within the frames. It calculates and displays the distance of the detected objects, specifically designed for objects such as cell phones for reference.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Object Detection Model](#object-detection-model
- [How It Works](#how-it-works)
- [Customization](#customization)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python (>=3.9) is installed on your system.
- You have access to a camera (built-in or external).

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/ismailousa/distance-estimator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd object-distance-estimator
   ```

3. Use Poetry to install the project dependencies:

   ```bash
   poetry install
   ```

## Usage

To run the object distance estimator, execute the following command:

```bash
poetry run python app/main.py
```

This will start the application, accessing your camera's live stream and detecting objects within the frames.

Press the 'q' key to exit the application.

## Object Detection Model

To perform object detection in real-time, this project uses an object detection model available in a separate GitHub repository. You can easily integrate it with this distance estimator by following these steps:

Clone the object detection model repository to your local machine and use Poetry to install

```bash
git clone https://github.com/ismailousa/yolo-detector.git
```

## How It Works

The core logic of the application is based on real-time object detection and distance estimation. Here's how it works:

1. The application initializes your camera and video recorder.

2. It calculates the focal length based on known parameters such as the known distance (`KNOWN_DISTANCE_CM`), the real width of the object (`MOBILE_WIDTH_CM`), and the width of the object in the reference frame (`MOBILE_WIDTH_IN_RF`).

3. The application continuously captures frames from the camera.

4. It detects objects within each frame and records their details, including the name, width in the frame, and coordinates.

5. For detected cell phones, the application estimates the distance from the camera using the focal length and displays it on the frame.

6. The application logs the results (to be implemented) for monitoring and analysis.

7. It draws rectangles around detected objects and labels them with their names and distances.

8. The processed frames with object annotations are displayed on the screen and simultaneously written to a video file ("out.mp4").

9. You can exit the application by pressing the 'q' key.

## Customization

You can customize this project by:

- Modifying the `constants.py` file to adjust parameters such as the known distance, object widths, and inference endpoints.
- Implementing logging and analysis of the detected objects for your specific use case.
- Adapting the code to work with different object detection models or camera configurations.

## License

This project is licensed under the MIT License.

Feel free to explore, modify, and use this project for your own applications!