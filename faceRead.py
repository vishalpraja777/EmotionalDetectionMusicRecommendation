import cv2
from deepface import DeepFace
import matplotlib.pyplot as plt
import spotifyApi

# Load the cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
# eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')

# Load the pre-trained model for face recognition
recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.read('recognizers/face-trainner.yml')
recognizer.read('recognizers/face-trainner.yml')

def readImage():
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture("C:\\Users\\Vishal Prajapathi\\Downloads\\sampleVideo.mp4")
    flag = 0
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            # Extract the face region of interest
            resized = cv2.resize(frame,(w,h))

            roi_gray = gray[y:y+h, x:x+w]

            # Recognize the face
            id_, confidence = recognizer.predict(roi_gray)
            print('Confidence: ' + str(confidence))

        # If the confidence is high enough, draw the name of the recognized person on the frame
            if confidence > 50 and confidence < 100:
                # cv2.putText(frame, 'Person ' + str(id_), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
                # resized = cv2.resize(frame,(w,h))

                # Draw a rectangle around the face
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                # print(x,y)
                # print(w,h)
                crop = frame[y-50:y+h+50,x-50:x+w+50]
                cv2.imwrite('ImageOutput/croppedOutput.jpg', crop)
                cv2.imwrite('ImageOutput/originalOutput.jpg', frame)
                flag = 1
                break
        

        # Show the frame
        cv2.imshow('Video', frame)
        if flag == 1:
            break
        # Exit the loop if the user presses the 'q' key
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()
    emotion = detectEmotion()
    lang = 'Hindi'
    res = spotifyApi.selectPlaylist(emotion,lang)
    res["mood"] = emotion
    return res

def detectEmotion():
    OriImg = cv2.imread('ImageOutput/originalOutput.jpg')
    CrpImg = cv2.imread('ImageOutput/croppedOutput.jpg')

    fig = plt.figure(figsize=(7, 5))

    fig.add_subplot(2,2,1)
    plt.imshow(OriImg[:,:,::-1])
    plt.title("OriginalImage")

    fig.add_subplot(2,2,2)
    plt.imshow(CrpImg[:,:,::-1])
    plt.title("CroppedImage")
    
    # plt.show()
    result = DeepFace.analyze(CrpImg,actions = ['emotion'])
    print('\nResult: ' + str(result))
    dominant_emotion = result[0]["dominant_emotion"]
    print('\nDominant Emotion: ',dominant_emotion)
    return dominant_emotion

# readImage()
