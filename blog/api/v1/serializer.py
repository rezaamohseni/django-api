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
        fields = [ 'title' , 'publisher' , 'category']


class BlogDetailserializer(serializers.ModelSerializer):

    class Meta:
        model = BlogDetail
        fields = [ 'title' , 'publisher' , 'category' , 'comments' , 'content' , 'description']

class BlogTagserializer(serializers.ModelSerializer):

    class Meta:
        model = BlogTag
        fields = [ 'title']