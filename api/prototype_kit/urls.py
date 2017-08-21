from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from app import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
