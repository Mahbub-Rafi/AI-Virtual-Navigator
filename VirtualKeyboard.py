import cv2
import cvzone
from time import sleep
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Controller, Key

# Initialize video capture
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize Hand Detector
detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

# Define keyboard keys
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
        ["Space", "Backspace"]]

# Text storage
finalText = ""

# Initialize keyboard controller
keyboard = Controller()

# Function to draw all buttons
def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size

        # Draw semi-transparent rectangles
        overlay = img.copy()
        cv2.rectangle(overlay, button.pos, (x + w, y + h), (50, 50, 50), cv2.FILLED)
        alpha = 0.3  # Transparency factor
        img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)

        # Calculate the position to center the text
        text_size = cv2.getTextSize(button.text, cv2.FONT_HERSHEY_SIMPLEX, 1.5, 2)[0]
        text_x = x + (w - text_size[0]) // 2
        text_y = y + (h + text_size[1]) // 2

        # Draw text with better styling
        cv2.putText(img, button.text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
    return img

# Define button class
class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text

# Create button instances
buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        if key == "Space":
            buttonList.append(Button([100 * j + 50, 100 * i + 50], key, size=[350, 85]))
        elif key == "Backspace":
            buttonList.append(Button([100 * j + 650, 100 * i + 50], key, size=[285, 85]))
        else:
            buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

while True:
    # Capture each frame from the webcam
    success, img = cap.read()

    # Find hands in the current frame
    hands, img = detector.findHands(img, draw=True, flipType=True)

    # Draw all buttons
    img = drawAll(img, buttonList)

    # Check if any hands are detected
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        center1 = hand1['center']
        handType1 = hand1["type"]

        # Check if a second hand is detected
        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            center2 = hand2['center']
            handType2 = hand2["type"]

        # Count the number of fingers up for the first hand
        fingers1 = detector.fingersUp(hand1)

        # Check for button interaction
        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < lmList1[8][0] < x + w and y < lmList1[8][1] < y + h:
                overlay = img.copy()
                cv2.rectangle(overlay, (x - 5, y - 5), (x + w + 5, y + h + 5), (200, 200, 200), cv2.FILLED)
                alpha = 0.5  # Transparency factor for hover effect
                img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)
                cv2.putText(img, button.text, (x + 10, y + 60), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)

                # Calculate distance between specific landmarks on the first hand and draw it on the image
                length, info, img = detector.findDistance(lmList1[4][0:2], lmList1[8][0:2], img, color=(255, 0, 255), scale=2)

                # When clicked
                if length < 30:
                    if button.text == "Space":
                        keyboard.press(Key.space)
                        finalText += " "
                    elif button.text == "Backspace":
                        keyboard.press(Key.backspace)
                        finalText = finalText[:-1]
                    else:
                        keyboard.press(button.text)
                        finalText += button.text

                    overlay = img.copy()
                    cv2.rectangle(overlay, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    alpha = 0.6
                    img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)
                    cv2.putText(img, button.text, (x + 10, y + 60), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)

                    sleep(0.20)

    # Draw semi-transparent text box
    overlay = img.copy()
    cv2.rectangle(overlay, (50, 500), (1040, 600), (50, 50, 50), cv2.FILLED)
    alpha = 0.3
    img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)
    cv2.putText(img, finalText, (60, 580), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

    # Display the image in a window
    cv2.imshow("Image", img)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
