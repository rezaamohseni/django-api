from django.urls import path ,include
from .views import *

app_name = 'api_blog'

urlpatterns = [
    path('blog', BlogApiViewSet.as_view({'get':'list' , 'post':'create'}), name='blog'),

    path('blog/<int:id>' , BlogDetailView.as_view({'get':'list' ,'put':'update' , 'delete':'destroy'}), name='blog-detail'),

    path('category' ,  CategoryApiViewSet.as_view({'get':'list' , 'post':'create'}), name='category'),

    path('comment' ,  CommentApiViewSet.as_view({'get':'list','post':'create','patch':'update'}), name='comment'),

    path('blog-tag' ,  BlogTagApiViewSet.as_view({'get':'list' , 'post':'create'}), name='blog-tag'),
    ]