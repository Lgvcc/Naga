from django.conf.urls import url, include
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'blog', BlogAPI)

extra_pattern = [
    url(r'^details/(?P<bid>[0-9]+)$', blog_details, name='details'),
    url(r'^tags$', tags, name='tags'),
    url(r'^categories$', tags, name='categories'),
]


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^b/', include(extra_pattern)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]