from django.http import Http404
from .models import bill
from .serializers import billSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from PIL import Image
import cv2
import os
from pathlib import Path
import urllib.request 
from ultralytics import YOLO
import easyocr


# Create your views here.

class BillArea(APIView):
    
    parser_classes = [MultiPartParser, FormParser]

    def post(self,request, format = None):
        try:
            serializer = billSerializer(data = request.data)
            if serializer.is_valid():
                 serializer.save()
    
            file_path = list(serializer.data.values())[0]
            print(file_path)
            img =cv2.imread(r'.{}'.format(file_path))
            model = YOLO('./ocr/area.pt')
            class_Name = ["Amount"]
            result = model.predict(img)
            reader = easyocr.Reader(['en'])
            for r in result:
                    boxes=r.boxes
                    for box in boxes.data.tolist():
                         x1, y1, x2, y2, score, class_id = box
                         cropped_img = img[int(y1):int(y2), int(x1): int(x2)]
                         gray_img = cv2.cvtColor(cropped_img, cv2.COLOR_RGB2GRAY)
                         output = reader.readtext(gray_img)

                         text = ""
                         for res in output:
                            if len(output) == 1 or (len(res[1]) > 6 and res[2] > 0.2):
                                text = res[1]
            return Response('Your Prediction is {}'.format(str(text)), status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)

