from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from blog.models import *
from .serializer import *
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import viewsets


class CategoryApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = Categoryserializer
    def get_queryset(self):
        return Category.objects.all()
    

class CommentApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAdminUser]
    serializer_class = Commentserializer
    def get_queryset(self):
        return Category.objects.all()
    

class BlogApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = Blogserializer
    def get_queryset(self):
        return Category.objects.all()
    
class BlogDetailApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = BlogDetailserializer
    def get_queryset(self):
        return Category.objects.all()
    
class BlogTagApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAdminUser]
    serializer_class = BlogTagserializer
    def get_queryset(self):
        return Category.objects.all()
    
