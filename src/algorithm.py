#import the libraries

import cv2
import numpy as np
import os
from datetime import datetime

#folder to save outputs
if not os.path.exists("saved_frames"):
    os.makedirs("saved_frames")

#video writer will be created after reading the first frame
video_writer = None

#loading the webcam
cap = cv2.VideoCapture(0)  # parameter 0 for default camera opening

#current date-time for filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

#output video name
output_video_name = f"enhanced_output_{timestamp}.avi"

#frame counter for saving images
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    #frame size
    frame = cv2.resize(frame, (640, 480))

    #convert the image frame into grayscale - preprocessing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #contrasting
    #using histogram equalization for contrast improvement
    contrast = cv2.equalizeHist(gray)

    # clarity
    #using canny edge detection for visibility enhacement
    edges = cv2.Canny(contrast, 50, 150)

    #combining both contrasting and clarity for a readable output
    colored_edge = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    enhanced_image = cv2.addWeighted(frame, 0.6, colored_edge, 0.4, 0)

    if video_writer is None:
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        video_writer = cv2.VideoWriter(output_video_name, fourcc, 20.0, (640, 480))

    #enhanced frame to video
    video_writer.write(enhanced_image)
    
    #Outputs
    # #frame for original image
    # cv2.imshow("Original image", frame)
    # #frame for contrast image
    # cv2.imshow("Contrast Improved", contrast)
    # #frame for detected edges
    # cv2.imshow("Edges", edges)
    #frame for enhanced view
    cv2.imshow("Enhanced View", enhanced_image)

    #Wait key
    key = cv2.waitKey(1) & 0xFF

    # Press 's' to save current frame as image
    if key == ord('s'):
        save_name = f"saved_frames/frame_{timestamp}_{frame_count}.jpg"
        cv2.imwrite(save_name, enhanced_image)
        print(f"Saved image: {save_name}")
        frame_count += 1

    #Exit with a click ('q') key
    if key == ord('q'):
        break

#release camera resources
cap.release()
video_writer.release()

#close all openCV windows
cv2.destroyAllWindows()

#save output
print(f"\nSaved video: {output_video_name}")
print("All saved images are in 'saved_frames' folder.")