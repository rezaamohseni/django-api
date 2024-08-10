from django.urls import path ,include

urlpatterns = [
    path('api/v2/' ,  include('blog.api.v1.urls'))
    
]
