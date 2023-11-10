from rest_framework.urls import path
from rest_framework.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from . import veiws


router = DefaultRouter()
router.register(r'category_admin', veiws.CategoryViewSet, basename='category_admin')



app_name = 'category_admin'
urlpatterns = []
urlpatterns += router.urls