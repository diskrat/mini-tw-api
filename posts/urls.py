from django.urls import path,include
from posts import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts',views.PostViewSet,basename='post')
router.register(r'users',views.UserViewSet,basename='user')
router.register(r'register',views.UserRegisterViewSet,basename='user-register')
router.register(r'likes',views.LikeViewSet,basename='like')

urlpatterns = [
    path('',include(router.urls)),
]