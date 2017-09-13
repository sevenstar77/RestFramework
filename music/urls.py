from django.conf.urls import url
from music import views


urlpatterns = [
    # url(r'^music/$', views.music_list),
    # url(r'^music/(?P<pk>[0-9]+)/$', views.music_detail),
    url(r'^$', views.JSONResponse.music_list),
    url(r'^(?P<pk>[0-9]+)/$', views.JSONResponse.music_detail),
]