from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from api import views as api
from web import views as web


router = routers.DefaultRouter()
router.register(r'api/users', api.UserViewSet)


urlpatterns = [
    url(r'^$', web.index, name='index'),

    url(r'^app/$', web.app, name='app'),
    
    url(r'^login/?$', web.signin, name='login'),
    url(r'^logout/?$', web.signout, name='logout'),

    url(r'^admin/', admin.site.urls),

    # url(r'^', include(router.urls), name='index'),
]
