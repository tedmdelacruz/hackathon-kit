from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from api import views as api
from web import views as web


router = routers.DefaultRouter()
router.register(r'api/users', api.UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^web/', web.index),
    url(r'^admin/', admin.site.urls),
]
