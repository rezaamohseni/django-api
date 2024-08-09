from django.urls import path ,include
from .views import *
app_name = 'api_blog'
urlpatterns = [
    path('category' ,  CategoryApiViewSet.as_view({'get':'list' , 'post':'create'}), name='category'),

    ]