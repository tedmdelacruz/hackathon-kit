from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from app.api import views as api
from app.web import views as web


router = routers.DefaultRouter()
router.register(r'api/users', api.UserViewSet)


urlpatterns = [
    url(r'^$', web.index, name='index'),

    url(r'^register/?$', web.register, name='register'),
    url(r'^login/?$', web.login, name='login'),
    url(r'^logout/?$', web.logout, name='logout'),

    url(r'^admin/', admin.site.urls),
    url('', include('pwa.urls')),
]

urlpatterns += router.urls
