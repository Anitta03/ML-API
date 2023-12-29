"""mlapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from titanicapi.views import PredictionList
from cnn.views import PictureList
from objectdetection.views import ObjectList
from ocr.views import BillArea
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('titanic/', PredictionList.as_view(),name ='titanicprediction'),
    path('picture/', PictureList.as_view(), name='pictureprediction'),
    path('object/', ObjectList.as_view(),name = 'objectprediction'),
    path('bill/', BillArea.as_view(), name = 'ocr')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

