from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class SpecialService(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=False , blank=False)
    image = models.ImageField(upload_to='root' , default='default.jpg')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='root' , default='default.jpg')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    
class Skill(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.title    
    
class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=False , blank=False)
    image = models.ImageField(upload_to='root' , default='default.jpg')
    Skill = models.ManyToManyField(Skill)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.email    




class Team(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill)
    image = models.ImageField(upload_to='root' , default='default.jpg')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)


    def __str__(self):
        return self.name.email
    

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField() 
    subject = models.CharField(max_length=100)
    message = models.TextField(null=False, blank=False)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

