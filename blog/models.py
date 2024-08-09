from django.db import models
from root.models import Team

class Category(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    image = models.ImageField(upload_to='blog' , default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    website = models.CharField(blank=True , null=True , max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(Team ,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog' , default='default.jpg')
    image_publisher = models.ImageField(upload_to='blog' , default='default.jpg')
    comments = models.ManyToManyField(Comment)
    content = models.TextField()
    descreption = models.TextField()



    def __str__(self):
        return self.title
    


    
class BlogTag(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    