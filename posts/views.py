from django.contrib.auth import get_user_model
from django.shortcuts import render
#from rest_framework import generics ///This is a tradeoff where we combine logic
# of multiple views into a single class.
from rest_framework import viewsets  #This is the new line in place of generics

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer 


## These are the new combined classes

class PostViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer





### The old was of creating view classes using generics   

#class PostList(generics.ListCreateAPIView):
#    queryset = Post.objects.all()
#    serializer_class = PostSerializer


#class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#    permission_classes = (IsAuthorOrReadOnly,)
#    queryset = Post.objects.all()
#    serializer_class = PostSerializer

#class UserList(generics.ListCreateAPIView):
#    queryset = get_user_model().objects.all()
#    serializer_class = UserSerializer

#class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = get_user_model().objects.all()
#    serializer_class = UserSerializer