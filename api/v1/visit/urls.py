from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.VisitViewSet, basename='visit')

app_name = 'visit'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
