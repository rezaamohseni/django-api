from rest_framework import serializers
from blog.models import *

class Categoryserializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [ 'title' ]

class Commentserializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [ 'name' , 'message' , 'website' , 'email']


class Blogserializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = [ 'title' , 'publisher' ]


class BlogDetailserializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = [ 'title' , 'publisher' , 'category' , 'comments' , 'content' , 'descreption']

class BlogTagserializer(serializers.ModelSerializer):

    class Meta:
        model = BlogTag
        fields = [ 'title']