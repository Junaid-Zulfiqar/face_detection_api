from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
# import time
# import cv2
# import mediapipe as mp
# import numpy as np
# import base64

#load fastapi
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Item(BaseModel):
    url: str

#get function
@app.get('/')
def read_root():
    return {"Hello": "World"}

#post function
# @app.post("/person_dectector")
# async def upload_base64(item:Item):
#     mpFaceDetection = mp.solutions.face_detection
#     mpDraw = mp.solutions.drawing_utils
#     faceDetection = mpFaceDetection.FaceDetection(model_selection=2,min_detection_confidence=0.4)
#     encoded_data = item.url.split(',')[1]
#     nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
#     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#     results = faceDetection.process(img)
#     if results.detections:
#         if len(results.detections) == 1:
#           return {   
#             'person':True,
#             'text':"Single person found"
#             }  
#         else:
#           return {   
#             'person':False,
#             'text':"Multiple persons are existed"
#             }      
#     else:
#         return {   
#         'person':False,
#         'text':"no one is found in picture"
#         }      



        