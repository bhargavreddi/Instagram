from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from Profile.models import Comments
from models import Image

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username')

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Image
        fields = ('id','image','date','time','user')

class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    image = ImageSerializer()
    class Meta:
        model = Comments
        fields = ('id','user','image','comment')

