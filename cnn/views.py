from django.http import Http404
from .models import tomato
from .serializers import tomatoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
import numpy as np
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img
from PIL import Image
import cv2
import os
from pathlib import Path
import urllib.request 
from ultralytics import YOLO
import easyocr


# Create your views here.

class PictureList(APIView):
    
    parser_classes = [MultiPartParser, FormParser]

    def post(self,request, format = None):
        try:
            serializer = tomatoSerializer(data = request.data)
            if serializer.is_valid():
                 serializer.save()
    
            file_path = list(serializer.data.values())[0]      
            img = load_img(r'.{}'.format(file_path), target_size=(224, 224))

            # Preprocessing the image
            x = img_to_array(img)
                ## Scaling
            x=x/255
            x = np.expand_dims(x, axis=0)
            model = load_model('./cnn/model_mobilenet.h5')
            preds = model.predict(x)
            preds=np.argmax(preds, axis=1)[0]
            if preds==0:
                preds="Bacterial_spot"
            elif preds==1:
                preds="Early_blight"
            elif preds==2:
                preds="Late_blight"
            elif preds==3:
                preds="Leaf_Mold"
            elif preds==4:
                preds="Septoria_leaf_spot"
            elif preds==5:
                preds="Spider_mites Two-spotted_spider_mite"
            elif preds==6:
                preds="Target_Spot"
            elif preds==7:
                preds="Tomato_Yellow_Leaf_Curl_Virus"
            elif preds==8:
                preds="Tomato_mosaic_virus"
            elif preds==9:
                preds="healthy"
            elif preds==10:
                preds="powdery_mildew"
            
            return Response('Your Prediction is {}'.format(str(preds)), status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)

        
