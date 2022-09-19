from .models import Post
from .serializers import MySocialNetworkSerializers
from rest_framework.viewsets import ModelViewSet


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = MySocialNetworkSerializers
