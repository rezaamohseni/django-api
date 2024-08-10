from django.urls import path ,include
from .views import *

app_name = 'api'
urlpatterns = [
    path('service' ,  ServiceApiViewSet.as_view({'get':'list' , 'post':'create' ,'patch':'update', 'delete' : 'destroy'})),
    path('SpecialService' ,  SpecialServiceApiViewSet.as_view({'get':'list' ,'patch':'update', 'post':'create' , 'delete' : 'destroy'})),
    path('Team' ,  TeamApiViewSet.as_view({'get':'list' , 'post':'create' , 'patch':'update' , 'delete' : 'destroy'})),
    path('Testimonial' ,  TestimonialApiViewSet.as_view({'get':'list' , 'post':'create' , 'patch':'update' , 'delete' : 'destroy'})),
    path('ContactUs' ,  ContactUsApiViewSet.as_view({'post':'create'})),     
    path('Skill' ,  SkillApiViewSet.as_view({'get':'list' , 'post':'create' , 'patch':'update' , 'delete' : 'destroy'}))            
]

