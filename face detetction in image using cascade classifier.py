import cv2

def Facedetction(imgpath,cascasepath):
    #convert the color image into grey image.
    grey_image = cv2.cvtColor(input_image,cv2.COLOR_BGR2GRAY)
    #detect face function and it's give values in x,y,w,h
    rect_face = Cascade_face.detectMultiScale(grey_image,scaleFactor=1.03, minNeighbors=9)
    print("Total Face detected in image",len(rect_face))
    # Loop through each face detected in the image and retireve the bounding box cordinates.
    for (x1, y1, bbox_width, bbox_height) in rect_face:
        # Draw bounding box around the face on the copy of the input image using the retrieved coordinates.
        cv2.rectangle(input_image, pt1=(x1, y1), pt2=(x1 + bbox_width, y1 + bbox_height), color=(0, 255, 0),thickness=3)
    #if the orignal image size is too large then we can resize it,or if it not large then ignore resize step.
    image_resize = cv2.resize(input_image,(int(input_image.shape[1]/2),int(input_image.shape[0]/2)))
    cv2.imshow('Detected faces', image_resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#Creating the required cascade_classifier.xml classifier file
Cascade_face = cv2.CascadeClassifier(r"C:\Users\user\Desktop\AAmer works\haarcascade_frontalface_default.xml")

#read the image
input_image = cv2.imread(r"C:\Users\user\Desktop\AAmer works\967516-virat-kohli-rcb.jpg")

Facedetction(input_image,Cascade_face)


