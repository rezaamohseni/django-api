from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class SpecialService(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='root' , default='default.jpg')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='root' , default='default.jpg')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name = models.ForeignKey(User,  on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='root' , default='default.jpg')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name    


class Skill(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title    


class Team(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill)
    image = models.ImageField(upload_to='root' , default='default.jpg')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    facebook = models.CharField(max_length=100)
    Twitter = models.CharField(max_length=100)
    linkdin = models.CharField(max_length=100)


    def __str__(self):
        return self.name    
    

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField() 
    subject = models.CharField(max_length=100)
    message = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

