#this script is used for inference in real time for images coming from the cctv 

import cv2
import tensorflow as tf
from tensorflow.image import resize

# Loading the pre-trained model trained on 320x320
model = tf.keras.models.load_model('your_model.h5')

# CCTV camera stream, 0 usually refers to the default webcam.use an IP address or video stream URL
cap = cv2.VideoCapture(0)  

while True:
    # Read frame from the camera
    ret, frame = cap.read()
    
    if not ret:
        break

    # Resize the frame to 320x320
    frame_resized = cv2.resize(frame, (320, 320))
    frame_resized = frame_resized / 255.0  
    frame_resized = frame_resized.reshape(1, 320, 320, 3)  # Adding batch dimension
    prediction = model.predict(frame_resized)
    
    # Display the result
    print(prediction)

    # Display the frame
    cv2.imshow('CCTV Camera Feed', frame_resized)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
