from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Profile.models import Image, Likes, Comments
from Profile.serializer import ImageSerializer, CommentsSerializer, LikeSerializer


@api_view(['GET','POST'])
def images(request):
    """
    Retrieve, update or delete a snippet instance.
    """
    if request.method == 'GET':
        snippet = Image.objects.all()
        serializer = ImageSerializer(snippet,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        id = data.get('image_id')
        user_id = data.get('user_id')
        image = Image.objects.get(id = id)
        user = User.objects.get(id=user_id)
        like = Likes.objects.filter(user = user ,image = image)
        if(like.count()==0):
            like = Likes(user = user,image = image)
            like.save()
        else:
            like = Likes.objects.get(user=user, image=image)
            like.delete()
        return Response()


@api_view(['GET','POST'])
def comments(request,pk = None):
    """
    Retrieve, update or delete a snippet instance.
    """
    if request.method == 'GET':
        if(pk == None):
            snippet = Comments.objects.all()
        else:
            snippet = Comments.objects.all().filter(image_id=pk)
        serializer = CommentsSerializer(snippet,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        id = data.get('image_id')
        user_id = data.get('user_id')
        comment = data.get('comment')
        image = Image.objects.get(id=id)
        user = User.objects.get(id=user_id)
        obj = Comments(user = user,image = image,comment = comment)
        obj.save()
        return Response()


@api_view(['POST'])
def addcomments(request):
    """
    Retrieve, update or delete a snippet instance.
    """
    if request.method == 'POST':
        data = request.data
        id = data.get('image_id')
        user_id = data.get('user_id')
        comment = data.get('comment')
        image = Image.objects.get(id=id)
        user = User.objects.get(id=user_id)
        obj = Comments(user = user,image = image,comment = comment)
        obj.save()
        return Response()

@api_view(['GET'])
def getLikeUsers(request,pk=None):
    if request.method == 'GET':
        if (pk == None):
            snippet = Likes.objects.all().values('user')
        else:
            snippet = Likes.objects.all().filter(image_id=pk)
        serializer = LikeSerializer(snippet, many=True)
        return Response(serializer.data)