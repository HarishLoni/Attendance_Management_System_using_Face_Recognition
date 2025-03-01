import cv2
import numpy as np

# Load the trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('TrainingImageLabel/trainner.yml')

# Load Haar Cascade for face detection
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

# Font settings
font = cv2.FONT_HERSHEY_SIMPLEX

# Start Video Capture
cam = cv2.VideoCapture(0)

while True:
    ret, im = cam.read()
    if not ret:
        break  # Stop if no frame is captured

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    for (x, y, w, h) in faces:
        Id, conf = recognizer.predict(gray[y:y+h, x:x+w])

        # Draw a rectangle around the face
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the recognized ID
        cv2.putText(im, f"ID: {Id}", (x, y - 10), font, 1, (255, 255, 255), 2)

    cv2.imshow('Face Recognition', im)

    # Press 'q' to exit
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()
