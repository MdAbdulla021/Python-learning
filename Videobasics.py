
import cv2 

#Open the video file
video = cv2.VideoCapture("Video.mp3.mp4")
#Read the video file frame by frame
while True:
    success, frame = video.read()
    if not success:
        break
    
    # Resize the frame
    resized_frame = cv2.resize(frame, (640, 480))
    
    # Show the video frame
    cv2.imshow("My Video", resized_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()