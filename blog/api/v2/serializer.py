from rest_framework import serializers
from blog.models import *

class Categoryserializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [ 'title','status']

class Commentserializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['name','email','message']


class Blogserializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = [ 'title' , 'content','description', 'status'] 

class BlogDetailserializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = [ 'title', 'content','description' , 'status']

class BlogTagserializer(serializers.ModelSerializer):

    class Meta:
        model = BlogTag
        fields = [ 'title' , 'status']