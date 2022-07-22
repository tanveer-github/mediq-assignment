from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views

router = DefaultRouter()
router.register('', views.UserViewSet, basename='user')

app_name = 'user'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
