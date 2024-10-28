import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands(max_num_hands=1)
drawing_utils = mp.solutions.drawing_utils

# Get screen size
screen_width, screen_height = pyautogui.size()

# Initialize variables for cursor control
index_x, index_y = 0, 0
prev_index_x, prev_index_y = 0, 0

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process hand landmarks
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            # Draw hand landmarks
            drawing_utils.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)

            # Extract specific landmarks (e.g., index finger and thumb)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if id == 8:  # Index finger tip
                    # Smooth cursor movement
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y
                    index_x = prev_index_x + (index_x - prev_index_x) * 0.5
                    index_y = prev_index_y + (index_y - prev_index_y) * 0.5

                    # Move the cursor
                    pyautogui.moveTo(index_x, index_y)

                    # Update previous position for smoothing
                    prev_index_x, prev_index_y = index_x, index_y

                    # Visualize index finger tip
                    cv2.circle(frame, (x, y), 10, (0, 255, 255), -1)

                elif id == 4:  # Thumb tip
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y

                    # Check distance between index and thumb for clicking
                    if abs(index_y - thumb_y) < 30:
                        # Click action
                        pyautogui.click()

                        # Visual feedback for click
                        cv2.circle(frame, (x, y), 10, (0, 0, 255), -1)

    # Display the frame with annotations
    cv2.imshow('Virtual Mouse', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
