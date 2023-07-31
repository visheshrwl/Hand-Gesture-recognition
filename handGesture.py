import cv2
import mediapipe as mp
import pyautogui

def detect_gestures(hand_landmarks):

    index_finger_extended = hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y

    thumb_extended = hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x

    return index_finger_extended, thumb_extended

if __name__ == "__main__":
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    screen_width, screen_height = 1920, 1080

    camera = cv2.VideoCapture(0)

    with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        while True:
            ret, frame = camera.read()
            if not ret:
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = hands.process(image=frame_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    index_finger_extended, thumb_extended = detect_gestures(hand_landmarks)

                    if index_finger_extended and not thumb_extended:
                        pyautogui.hotkey('ctrl', 'tab')

            cv2.imshow("Hand Gesture Tab Change", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    camera.release()
    cv2.destroyAllWindows()
