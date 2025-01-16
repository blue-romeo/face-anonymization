# Face Detection and Blurring Project

## Overview
This project performs **real-time face detection and blurring** using Python, OpenCV, and MediaPipe. It supports processing images, videos, and live webcam feeds (including IP Webcam streams) to anonymize faces by applying a blur effect to detected regions.

## Features
- Detects faces using MediaPipe's high-performance face detection model.
- Applies a blur effect to anonymize detected faces.
- Supports:
  - **Images**: Processes single image files.
  - **Videos**: Processes video files frame-by-frame.
  - **Webcam Streams**: Processes live webcam feeds (including streams from the IP Webcam app).
- Saves processed images and videos to an output directory.

## Requirements
### Software
- Python 3.8 or higher

### Python Libraries
Install the required libraries using:
```bash
pip install opencv-python mediapipe
```

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/blue-romeo/face-blurring
   cd face-blurring
   ```

2. **Run the script** with the appropriate mode and file path:
   ```bash
   python script.py --mode [mode] --filePath [path]
   ```

## Usage
### Command-Line Arguments
- `--mode`:
  - `image`: Processes a single image file.
  - `video`: Processes a video file.
  - `webcam`: Processes live webcam feed.
- `--filePath`:
  - Specify the path to the input file for `image` or `video` mode.
  - This is not required for `webcam` mode.

### Examples
1. **Process an Image**:
   ```bash
   python script.py --mode image --filePath ./input.jpg
   ```
   Output saved as `output/output.jpg`.

2. **Process a Video**:
   ```bash
   python script.py --mode video --filePath ./input.mp4
   ```
   Output saved as `output/output.mp4`.

3. **Process Live Webcam Stream**:
   ```bash
   python script.py --mode webcam
   ```
   Displays processed frames in real time; press `q` to exit.

4. **Process IP Webcam Stream**:
   Update the `address` variable in the code to match your phone’s IP stream address.

## Output
- All processed images and videos are saved to the `output` directory.
- If the directory does not exist, it will be created automatically.

## Code Explanation
1. **Face Detection**:
   - Uses MediaPipe to detect faces with a minimum confidence of `0.5`.
   - Bounding boxes are scaled to the image dimensions.

2. **Face Blurring**:
   - Detected face regions are blurred using OpenCV’s `cv.blur()` method.

3. **Input Modes**:
   - **Image Mode**: Reads and processes a single image.
   - **Video Mode**: Reads and processes each video frame.
   - **Webcam Mode**: Captures frames in real-time and processes them dynamically.

4. **Output Handling**:
   - Images and videos are saved in the `output` directory with default filenames (`output.jpg` or `output.mp4`).

## Future Improvements
- Add support for adjusting blur intensity via a command-line argument.
- Implement multi-threading for faster video processing.
- Extend support to detect and blur multiple face features (e.g., eyes, mouth).
- Add a graphical user interface (GUI) for easier usage.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to enhance the project.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments
- [OpenCV Documentation](https://docs.opencv.org/)
- [MediaPipe Documentation](https://mediapipe.dev/)
- [IP Webcam App](https://play.google.com/store/apps/details?id=com.pas.webcam)

