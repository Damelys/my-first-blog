from django.conf.url import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
]
