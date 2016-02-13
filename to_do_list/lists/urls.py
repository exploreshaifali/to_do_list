from django.conf.urls import include, url
from rest_framework import routers

# from lists.views import ListView
from lists.views import ListViewSet


router = routers.SimpleRouter()
router.register(r'tasks', ListViewSet)
urlpatterns = [
    # url(r'^$', ListView.as_view(), name='home')
    url(r'^', include(router.urls)),
]
