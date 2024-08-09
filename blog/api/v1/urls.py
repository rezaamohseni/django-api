from django.urls import path ,include
from .views import *
app_name = 'api_blog'
urlpatterns = [
    path('category' ,  CategoryApiViewSet.as_view({'get':'list' , 'post':'create'}), name='category'),
    path('comment' ,  CommentApiViewSet.as_view({'get':'list' , 'post':'create','patch':'update'}), name='comment'),
    path('blog' ,BlogApiViewSet.as_view({'get':'list' , 'post':'create'}), name='blog'),
    path('blogdetail' ,BlogDetailApiViewSet.as_view({'get':'list' , 'post':'create','patch':'update','delete':'destroy'}), name='blog-detail'),
    path('blog-tag' ,  BlogTagApiViewSet.as_view({'get':'list' , 'post':'create'}), name='blog-tag'),


    ]