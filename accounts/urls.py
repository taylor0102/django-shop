from django.urls import include
from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'profile', views.ProfileUserViewSet, basename='profile')

app_name = 'user'
urlpatterns = [
    path('signup/', views.CreateUserApiView.as_view(), name='signup_user'),
    path('', include(router.urls)),
] + router.urls
