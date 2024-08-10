from rest_framework import serializers
from blog.models import *




class Categoryserializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [ 'title' ]


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [ 'name' , 'email' , 'message']



class blogserializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = [ 'title' , 'publisher' , 'category','comment','content','description' ]



class blogdetailserializer(serializers.ModelSerializer):

    class Meta:
        model = BlogDetail
        fields = [ 'title' , 'publisher' , 'category','comment','content','description']



class blogtagserializer(serializers.ModelSerializer):

    class Meta:
        model = BlogTag
        fields = [ 'title' ]



