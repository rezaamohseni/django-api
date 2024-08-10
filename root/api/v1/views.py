from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from root.models import Service , SpecialService , ContactUs , Team , Testimonial
from .serializer import *
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import viewsets


class ServiceApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = Serviceserializer
    def get_queryset(self):
        return Service.objects.all()

class SpecialServiceApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = SpecialServiceSerializer
    def get_queryset(self):
        return SpecialService.objects.all()
    
class TeamApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = Teamserializer
    def get_queryset(self):
        return Team.objects.all()
    
class TestimonialApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = Testimonialserializer
    def get_queryset(self):
        return Testimonial.objects.all()
    
class ContactUsApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = ContactUsserializer
    def get_queryset(self):
        return ContactUs.objects.all()
    
class SkillApiViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = Skillserializer
    def get_queryset(self):
        return Skill.objects.all()    