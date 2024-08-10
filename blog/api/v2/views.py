from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from blog.models import *
from .serializer import *
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import viewsets


class CategoryApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = Categoryserializer
    def get_queryset(self):
        return Category.objects.all()

class CommentApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    def get_queryset(self):
        return Comment.objects.all()
    
class blogApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = blogserializer
    def get_queryset(self):
        return Blog.objects.all()
    
class blogdetailApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = blogdetailserializer
    def get_queryset(self):
        return BlogDetail.objects.all()
    
class blogtagApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = blogtagserializer
    def get_queryset(self):
        return BlogTag.objects.all()
    
