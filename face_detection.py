import cv2

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#trained_face_data = cv2.CascadeClassifier('haarcascade_smile.xml')


# Choose and image to detect a face in
# img = cv2.imread('multi.png')

# TO capture video from webcam  
webcam =  cv2.VideoCapture('covid.mov')

# Iterate over each frame
while True:
    successful_frame_read, frame = webcam.read()
    greyscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)
    count = 0
    
    for (x, y, w, h) in face_coordinates:
        count = len(face_coordinates)
        text = 'Face Count: ' + str(count)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, text, (10,50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
        cv2.imshow('Clever Face Detector', frame)
        key = cv2.waitKey(1)
        
   ##if key==81 or key==113:
     #   break
# Converting image to grayscale


# Detect faces
#face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)
#print(face_coordinates)

# Draw rectangles around the faces


print('\nCode Completed')
