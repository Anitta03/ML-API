from django.http import Http404
from .models import titanic
from .serializers import titanicSerializer
import tensorflow
from django.core.files.storage import FileSystemStorage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from sklearn.externals import joblib
import pickle
import numpy as np
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img
import PIL.Image as PilImage
import io
# Create your views here.
class PredictionList(APIView):
   
    def post(self, request, format = None):
        try:
            mydata=request.data
            unit = np.array(list(mydata.values()))
            to_predict = unit.reshape(1,-1)
            loaded_model = pickle.load(open('./titanicapi/model.pkl', "rb"))
            result = loaded_model.predict(to_predict)
            if int(result) == 1:
                prediction ='Survived'
            else:
                prediction ='Not Survived'	
       
            return Response('Your Prediction is {}'.format(prediction), status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)
        
   
