from django.urls import path ,include
from .views import *
app_name = 'api'
urlpatterns = [
    
    path('service' ,  ServiceApiViewSet.as_view({'get':'list' , 'post':'create', 'patch':'update' , 'delete':'destroy'}), name='services'),
    path('specialservice' ,  SpecialServiceApiViewSet.as_view({'get':'list' , 'post':'create', 'patch':'update' , 'delete':'destroy'}) , name='specialservice'),
    path('team' ,  TeamApiViewSet.as_view({'get':'list', 'delete':'destroy','post':'create'}), name='team'),
    path('testimonial' ,  TestimonialsApiViewSet.as_view({'get':'list','delete':'destroy'}), name='testimonial'),
    path('skill' , SkillApiViewSet.as_view({'get':'list','post':'create', 'patch':'update' , 'delete':'destroy'}), name='skill'),
    path('contact' ,  ContactUsApiViewSet.as_view({'post':'create'}), name='contactus'),
]

