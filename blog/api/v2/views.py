from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from blog.models import *
from .serializer import *
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin , CreateModelMixin , RetrieveModelMixin , DestroyModelMixin , UpdateModelMixin


class CategoryApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = Categoryserializer
    def get_queryset(self):
        return Category.objects.all()
    

class CommentApiViewSet(viewsets.ModelViewSet):
    # lookup_field='id'
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = Commentserializer
    def get_queryset(self):
        return Category.objects.all()
    

class BlogApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = Blogserializer
    def get_queryset(self):
        return Category.objects.all()
    
# class BlogDetailApiViewSet(viewsets.ModelViewSet):
#     permission_classes=[IsAuthenticatedOrReadOnly]
#     lookup_field='id'
#     serializer_class = BlogDetailserializer
#     def get_queryset(self):
#         return Category.objects.filter(id=id)
class BlogDetailView(GenericAPIView , RetrieveModelMixin , DestroyModelMixin , UpdateModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BlogDetailserializer
    def get_queryset(self):
        return Blog.objects.filter(status=True)
    
    def get(self , request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BlogTagApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = BlogTagserializer
    def get_queryset(self):
        return Category.objects.all()
    
