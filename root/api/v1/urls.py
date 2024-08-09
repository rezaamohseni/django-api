from django.urls import path ,include
from .views import *
app_name = 'api'
urlpatterns = [
    
    path('service' ,  ServiceApiViewSet.as_view({'get':'list' , 'post':'create'}))
]

