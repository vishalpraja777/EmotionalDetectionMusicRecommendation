import cv2
import numpy as np
from keras.models import model_from_json


emotion_dict = {0: "angry", 1: "disgust", 2: "fear", 3: "happy", 4: "neutral", 5: "sad", 6: "surprise"}

# load json and create model
json_file = open('modelFiles/model/emotion_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
emotion_model = model_from_json(loaded_model_json)

# load weights into new model
emotion_model.load_weights("modelFiles/model/emotion_model.h5")
# print("Loaded model from disk")

# start the webcam feed
cap = cv2.VideoCapture(0)



def findEmotion(img,x,y,w,h):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    roi_gray_frame = gray_frame[y:y + h, x:x + w]
    cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)
    emotion_prediction = emotion_model.predict(cropped_img)
    maxindex = int(np.argmax(emotion_prediction))
    dic = {}
    for k,v in emotion_dict.items():
        dic[v] = emotion_prediction[0][k]

    result = [{'emotion':dic,'dominant_emotion':emotion_dict[maxindex]}]

    return result