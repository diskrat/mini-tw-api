from posts.models import Post, Like
from posts.permissions import IsOwnerOrReadOnly, IsOwnerOrReadOnly
from posts.serializers import LikeSerializer, PostSerializer, UserSerializer, UserRegisterSerializer
from rest_framework import permissions
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets, mixins, status


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'message': 'User created'}, status=status.HTTP_201_CREATED)


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the like with the authenticated user
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        try:
            like = Like.objects.get(id=kwargs['pk'], user=self.request.user)
            like.delete()
            return Response({'message': 'Like removed successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            raise ValidationError('post not liked')


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format),
        'register': reverse('user-registration', request, format=format)
    })
