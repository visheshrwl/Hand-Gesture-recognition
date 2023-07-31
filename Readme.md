# Hand Gesture Tab Change

This Python script uses computer vision and hand tracking to detect specific hand gestures and simulate a keyboard command to change browser tabs accordingly. It utilizes the OpenCV library for computer vision tasks, the Mediapipe library for hand tracking, and the PyAutoGUI library to simulate keyboard input.

## Requirements

To run this script, you need to have the following Python packages installed:

- opencv-python
- mediapipe
- pyautogui

You can install these packages using `pip` with the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## How It Works

The script uses a webcam to capture real-time video frames. It processes each frame using Mediapipe's hand tracking module to detect hand landmarks. The key hand landmarks are used to identify specific hand gestures. The following hand gestures are recognized:

1. **Index Finger Extended**: The index finger is extended (pointing forward).
2. **Thumb Extended**: The thumb is extended outward.

The script checks for the above two gestures simultaneously. If the index finger is extended, and the thumb is not extended, it simulates a keyboard command to change the active tab in a web browser.

## Supported Hand Gesture

The supported hand gesture to change the tab is as follows:

1. **Gesture to Change Tab**: Extend your index finger while keeping the thumb relaxed (not extended).

## How to Use

1. Make sure you have Python and the required packages installed.
2. Run the script by executing the following command:

```bash
python hand_gesture_tab_change.py
```

1. A window will open showing the video feed from your webcam and detecting your hand.
2. Show your hand in front of the webcam and perform the supported hand gesture.
3. When you extend your index finger and the thumb is relaxed, the script will simulate a keyboard command to change the tab (Ctrl + Tab).


## Note
* For optimal performance, ensure that the webcam has enough light and your hand is clearly visible.
* The script may require adjustments in certain lighting conditions or for different hand sizes and positions.

## Author

[Vishesh Rawal](https://github.com/visheshrwl)