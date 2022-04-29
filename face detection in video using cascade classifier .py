import cv2


def facedetection(video_source,face_cascade):
    
    while True:
        # Capture frame-by-frame
        check,frame = video_cascade.read()
        #converting to gray image for faster video processing
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #detect face function and it's give values in x,y,w,h
        rect_face = Cascade_face.detectMultiScale(gray_img,scaleFactor=1.3, minNeighbors=3)
        for (x1, y1, bbox_width, bbox_height) in rect_face:
            # Draw bounding box around the face on the copy of the input image using the retrieved coordinates.
            cv2.rectangle(frame, pt1=(x1, y1), pt2=(x1 + bbox_width, y1 + bbox_height), color=(0, 255, 0),thickness=3)
        # Display the resulting frame
        cv2.imshow('Face Detection', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video_cascade.release()
    cv2.destroyAllWindows()


#Creating the required cascade_classifier.xml classifier file
Cascade_face = cv2.CascadeClassifier(r"C:\Users\user\Desktop\AAmer works\haarcascade_frontalface_default.xml")
#video path if it is webcam then give how much web cam 0,1,2,3 or if it video path then give video path in it.
video_cascade = cv2.VideoCapture(0)


facedetection(video_cascade,Cascade_face)

