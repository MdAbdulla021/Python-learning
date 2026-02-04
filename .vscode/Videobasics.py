import cv2 

#Open the video file
video = cv2.VideoCapture("Video.mp3")

#Read the video file frame by frame
while True:
    success, frame = video.read()
    
    if not success:
        break
    
        # Show the video frame
        cv2.imshow("My Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    video.release()
    cv2.destroyAllWindows()