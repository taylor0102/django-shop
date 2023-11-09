from django.urls import include
from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from . import veiws


router = DefaultRouter()
router.register(r'category', veiws.CategoryViewSet, basename='category')

app_name = 'category_client'
urlpatterns = [
    path('', include(router.urls)),
] + router.urls
