from django.contrib.auth.models import User
from posts.models import Like, Post
from rest_framework import serializers
from rest_framework.response import Response


class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Like
        read_only_fields =  ['user']
        fields = ['id','user','post','created']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Post
        fields = ['id','user','content','created']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        password = serializers.CharField(write_only=True)
        fields = ['username','email','password']
    def create(self,validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return Response({'message':'user successfully created'})


        