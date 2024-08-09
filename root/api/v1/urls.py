from django.urls import path ,include
from .views import *
app_name = 'api'
urlpatterns = [
    
    path('service' ,  ServiceApiViewSet.as_view({'get':'list' , 'post':'create'}), name='services'),
    path('specialservice' ,  SpecialServiceApiViewSet.as_view({'get':'list' , 'post':'create'}) , name='specialservice'),
    path('team' ,  TeamApiViewSet.as_view({'get':'list'}), name='team'),
    path('testimonial' ,  TestimonialsApiViewSet.as_view({'get':'list'}), name='testimonial'),
    path('skill' , SkillApiViewSet.as_view({'get':'list'}), name='skill'),
    path('contactus' ,  ContactUsApiViewSet.as_view({'get':'list','post':'create'}), name='contactus'),
]

