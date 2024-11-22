# from django.contrib import admin
from django.urls import path,include
from LoanDeployment import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('',views.index,name="index"),
    
    path('dataanalysis',views.dataanalysis,name="dataanalysis"),
    # path('result',views.formInfo,name="result"),
    path('about',views.about,name="about"),
    path('', views.formInfo, name="index"), 
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
