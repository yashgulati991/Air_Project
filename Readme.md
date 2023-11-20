Virtual Coffee Machine
This project is a combination of 2 projects a virtual mouse and online ordering coffee system . So there are many projects like this but the resolution and the refresh rate for 
them are too bad and they also can't catch all mark points on our landing fingers so this is resolved in our project . 

Coffee is a popular drink enjoyed by many people worldwide, and as the demand for coffee increases, 
so does the need for efficient and user-friendly coffee machines. However, the conventional physical buttons and switches on coffee machines can pose 
challenges to certain users, particularly those with physical disabilities or limited technical knowledge.

Hardware Requirements:
•	A computer with a dedicated graphics card
•	A camera capable of capturing high-quality images.
•	A coffee machine with programmable settings
•	A microcontroller board (e.g., Arduino) to connect the computer and the coffee machine.
•	Hand tracking hardware, such as Leap Motion or Intel RealSense camera
Software Requirements:
•	Operating system: Windows or Linux
•	Python programming language
•	OpenCV library for computer vision tasks
•	Machine learning libraries, such as scikit-learn or TensorFlow, for gesture recognition.
•	Arduino IDE for programming the microcontroller board.
•	GUI toolkit, such as PyQt, for developing the virtual interface
![image](https://github.com/yashgulati991/Air_Project/assets/83648916/6c98daca-4ef8-46d3-9c98-3894d3ac7434)
![image](https://github.com/yashgulati991/Air_Project/assets/83648916/2826cf70-4940-4fac-8962-f973c03f597c)
It uses the HandTrackingModule from cvzone to detect the hand and its landmarks in the webcam feed. It then overlays the webcam feed on a background image and allows the user to select various coffee modes by using hand gestures. The selection process involves moving the hand in a circular motion over the mode icon, and the selection speed can be controlled by the user. The selected mode is displayed at the bottom of the interface using icons.
The code runs continuously until the user exits the program by pressing the 'q' key.

