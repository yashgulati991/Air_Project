import os
import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Load the background image
background_image = cv2.imread("Resources/Background.png")

# Load mode images into a list
modes_folder = "Resources/Modes"
mode_images = [cv2.imread(os.path.join(modes_folder, mode_path)) for mode_path in os.listdir(modes_folder)]
print(mode_images)

# Load icons into a list
icons_folder = "Resources/Icons"
icon_images = [cv2.imread(os.path.join(icons_folder, icon_path)) for icon_path in os.listdir(icons_folder)]

# Initialize variables
mode_type = 0
selection = -1
counter = 0
selection_speed = 7
hand_detector = HandDetector(detectionCon=0.8, maxHands=1)
mode_positions = [(1136, 196), (1000, 384), (1136, 581)]
counter_pause = 0
selection_list = [-1, -1, -1]

while True:
    # Read from the webcam
    success, webcam_img = cap.read()

    # Detect hands in the image
    hands, webcam_img = hand_detector.findHands(webcam_img)

    # Overlay the webcam feed on the background image
    background_image[139:139 + 480, 50:50 + 640] = webcam_img
    background_image[0:720, 847:1280] = mode_images[mode_type]

    if hands and counter_pause == 0 and mode_type < 3:
        # Extract information about the first hand
        hand1 = hands[0]
        fingers1 = hand_detector.fingersUp(hand1)
        print(fingers1)

        # Check finger positions to determine selection
        if fingers1 == [0, 1, 0, 0, 0]:
            if selection != 1:
                counter = 1
            selection = 1
        elif fingers1 == [0, 1, 1, 0, 0]:
            if selection != 2:
                counter = 1
            selection = 2
        elif fingers1 == [0, 1, 1, 1, 0]:
            if selection != 3:
                counter = 1
            selection = 3
        else:
            selection = -1
            counter = 0

        if counter > 0:
            counter += 1
            print(counter)

            # Draw the ellipse to indicate the selection progress
            cv2.ellipse(background_image, mode_positions[selection - 1], (103, 103), 0, 0,
                        counter * selection_speed, (0, 255, 0), 20)
            if counter * selection_speed > 360:
                selection_list[mode_type] = selection
                mode_type += 1
                counter = 0
                selection = -1
                counter_pause = 1

    # Pause after each selection is made
    if counter_pause > 0:
        counter_pause += 1
        if counter_pause > 60:
            counter_pause = 0

    # Add selection icon at the bottom
    for i, selection_value in enumerate(selection_list):
        if selection_value != -1:
            img_x = 133 + i * 207
            img_background_x = 636 + i * 207
            img_background[img_background_x:img_background_x + 65, img_x:img_x + 65] = icon_images[selection_value - 1]

    # Display the images
    cv2.imshow("Background", background_image)
    cv2.waitKey(1)
