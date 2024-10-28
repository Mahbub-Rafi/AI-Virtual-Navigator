
# AI VIRTUAL NAVIGATOR

The AI Virtual Navigator project studies the development of a gesture-based human computer interaction system, substituting standard input devices such as a mouse and keyboard with hand movements collected by a webcam. The system tracks hand movements in real time using OpenCV and MediaPipe computer vision techniques for virtual typing and mouse navigation. Under different environmental conditions, gesture detection accuracy, virtual keyboard performance, and virtual mouse precision were tried. Under ideal conditions, accuracy was great, but low-light and complicated backgrounds presented problems. The idea shows promise to improve accessibility and user experience in healthcare and contactless interface environments. Further developments could involve adding depth sensors and strengthening algorithmic robustness for wider uses.


## Documentation

[See Full Documentation](https://github.com/user-attachments/files/17544991/498R-Final-Report-black-book.pdf)


## Acknowledgements

 - [Directed Research, Summer 2024, North South University](http://ece.northsouth.edu/directed-research-498r/)


## Motivation

In recent years, computing has surpassed traditional desktops and laptops, spreading its reach to mobile devices such as palmtops and smartphones. With constant developments in technology and the expanding effect of artificial intelligence (AI), we were inspired to seek novel solutions within this changing landscape. This study focuses on a specialized use of AI, showing a system that utilizes finger movement gesture detection to operate a computer interface via a camera. The user can handle the entire system by simply moving a finger, providing a more intuitive and efficient alternative to conventional input devices. Leveraging innovative finger detection algorithms, this device offers quick camera access and features a user-friendly interface, boosting accessibility while eliminating dependency on physical keyboard and mouse. By eliminating physical contact, the technology optimizes efficiency, saves time, and decreases effort. Human computer interaction is one of the fastest-growing disciplines in technology, with hand gestures playing a crucial part in this realm. Our goal is to study unique HCI modules using hand gestures and deploy them to promote further developments in the industry. While keyboards and mice have long been crucial tools for human-computer interaction, we plan to propose a fresh idea of virtual input devices. Unlike typical virtual keyboards projected onto surfaces, our idea suggests a keyboard that operates in mid-air. Through the use of hand and fingertip gestures, users will be able to input letters and commands easily. This initiative contributes to the developing area of AI and digital innovation, aligning with the future of human-computer interaction.
## Installation

To install the required packages, run the following command:

```bash
make install requirements.txt
```
This will install the required packages specified in the requirements.txt file.


## Run 
To run the project with npm, follow the commands:

```bash
python -m venv env
cd env\scripts
activate
cd ..
pip install django
django-admin startproject name
cd name
python manage.py startapp login
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser (follow the steps)
python manage.py runserver
```

## Methodology

### Block Diagram of the System:

![ Block Diagram](https://github.com/user-attachments/assets/a064bd69-06cc-4915-a72f-6d723e1ef91a)

The block diagram shows the hardware components and signal flow of the AI Virtual Navigator method. The system relies on a webcam to record real-time video, which is sent to the processing unit (a computer) for gesture detection. Inside the computing unit, software components including OpenCV, Mediapipe, and CVZone process the video data to identify and understand hand movements. Based on these inputs, PyAutoGUI simulates virtual mouse and keyboard actions. The results are then displayed on the monitor, giving visual feedback to the user. A central power source powers both the webcam and the processing unit.


### Segmenting Skin Tones:

![Segmenting Skin Tones](https://github.com/user-attachments/assets/6e140ddd-f9d7-420b-b621-d17aff6b22ea)

### Monitoring Hand Motions
![Monitoring Hand Motions](https://github.com/user-attachments/assets/00ee9e03-2a67-45ae-b36a-e5b16ea2a783)

### Estimating Hand Landmarks
![Estimating Hand Landmarks](https://github.com/user-attachments/assets/b3acadf5-154c-429c-a156-a150ac75a7bb)

### User Interface
![User Interface](https://github.com/user-attachments/assets/84bf0ad8-7cba-4f27-a940-5804286c9e04)


### Virtual Keyboard

![Virtual Keyboard](https://github.com/user-attachments/assets/ac5991ef-bc29-4555-be2c-fcaede1289ae)

### Performing actions using the mouse and keyboard
![Performing actions using the mouse and keyboard](https://github.com/user-attachments/assets/f0f3a88e-b64d-471f-ae23-37cf670b5ffa)

## Results
The first experiment involved testing the system's ability to detect and interpret finger movements in different lighting conditions. Using OpenCV and MediaPipe, the system was evaluated for accuracy in capturing hand gestures. The results showed a 92% accuracy rate under optimal lighting conditions, but accuracy decreased to 78% in low-light environments. Figure 1a illustrates the relationship between lighting conditions and gesture detection accuracy, with appropriate axis labels ("Lighting Intensity" on the x-axis and "Accuracy (%)" on the y-axis).

![Results](https://github.com/user-attachments/assets/61332b50-c51e-4c69-8654-eadb265a6b2b)


- Lighting conditions and gesture detection accuracy
![lighting conditions and gesture detection accuracy](https://github.com/user-attachments/assets/d6fb0e1e-a6c1-4794-a648-0b4842f0ee88)

- Key detection accuracy under different hand movement speeds
![Key detection accuracy under different hand movement speeds](https://github.com/user-attachments/assets/6824594d-6019-444d-9329-b9f28d7e6cce)

- Key detection accuracy under different background complexity
![Key detection accuracy under different background complexity](https://github.com/user-attachments/assets/9ee21890-7352-47bc-8114-fcbdc70eeb55)



## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Mahbub-Rafi/AI-Virtual-Navigator/blob/main/LICENSE) file for details.


## References

[1] 	D. Rustagi, G. Maindola, H. Jain, B. Gakhar, G. Chugh and E. Ijmtst, "Virtual Control Using Hand -Tracking," International Journal for Modern Trends in Science and Technology, vol. 8, pp. 26-31, January 2022. 

[2] 	S. Chintamani, R. Bhad, N. Deokar, K. Kadam and P. A. B.A, "AI Virtual Mouse Using Open CV," International Journal of Emerging Technologies and Innovative Research, vol. 10, no. 5, pp. g689-g693, 2023. 

[3] 	P. S. Kumari Verma, S. Mahanta, S. B N and A. P. Shreedhar B, "Virtual Mouse and Keyboard for Computer Interaction by Hand Gestures Using Machine Learning," International Journal of Current Science Research and Review, vol. 6, no. 8, pp. 5469-5479, 2023. 

[4] 	T.-H. Lee, S. Kim, T. Kim, J.-S. Kim and H.-J. Lee, "Virtual Keyboards With Real-Time and Robust Deep Learning-Based Gesture Recognition," IEEE Transactions on Human-Machine Systems, vol. 52, pp. 725-735, August 2022. 

[5] 	Č. Livada, M. Proleta, K. Romić and H. Leventić, "Beyond the touch: A web camera based virtual keyboard," in 2017 International Symposium ELMAR, 2017. 

[6] 	T.-H. Lee and H.-J. Lee, "Ambidextrous Virtual Keyboard Design with Finger Gesture Recognition," in 2018 IEEE International Symposium on Circuits and Systems (ISCAS), 2018. 

[7] 	G. Van Rossum and F. L. Drake, Python 3 Reference Manual, Scotts, Valley: CreateSpace, 2009. 

[8] 	G. Bradski, "The OpenCV Library," Dr. Dobb's Journal of Software Tools, 2000. 

[9] 	CVZone, "GitHub," [Online]. Available: https://github.com/cvzone/cvzone

[10] 	Diwas, "AI Projects," 2021. [Online]. Available: https://aihubprojects.com/hand-detection-gesture-recognition-opencv-python/

[11] 	C. Lugaresi, J. Tang, H. Nash, C. McClanahan, E. Uboweja, M. Hays, F. Zhang, C.-L. Chang, M. G. Yong, J. Lee, W.-T. Chang, W. Hua, M. Georg and M. Grundmann, MediaPipe: A Framework for Building Perception Pipelines, 2019. 

[12] 	A. Sweigart, "PyAutoGUI," 2019. [Online]. Available: https://pyautogui.readthedocs.io/en/latest/

[13] 	JetBrains, "PyCharm," [Online]. Available: https://www.jetbrains.com/help/pycharm/getting-started.html
