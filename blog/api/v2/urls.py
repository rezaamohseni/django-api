from django.urls import path ,include
from .views import *

app_name = 'api_blog'
urlpatterns = [
    path('blog' ,  blogApiViewSet.as_view({'get':'list' , 'post':'create'})),
    path('blog/<int:pk>' ,  blogApiViewSet.as_view({'get':'retrieve' , 'patch':'update' , 'delete' : 'destroy'})),
    path('blogtag' ,  blogtagApiViewSet.as_view({'get':'list' , 'post':'create' ,'delete' : 'destroy'})),
    path('comment' ,  CommentApiViewSet.as_view({'get':'list' , 'post':'create' , 'patch':'update' , 'delete' : 'destroy'})),
    path('category' ,  CategoryApiViewSet.as_view({'get':'list','post':'create'})),     
]