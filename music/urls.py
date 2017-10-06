from django.conf.urls import url
from music import views


urlpatterns = [
    # url(r'^music/$', views.music_list),
    # url(r'^music/(?P<pk>[0-9]+)/$', views.music_detail),
    #url(r'^$', views.JSONResponse.music_list),
    #url(r'^(?P<pk>[0-9]+)/$', views.JSONResponse.music_detail),

    #url(r'^$', views.music_list),
    #url(r'^(?P<pk>[0-9]+)/$', views.music_detail)
    url(r'^music-categories/$', views.MusicCategoryList.as_view(), name=views.MusicCategoryList.name),
    url(r'^music-categories/(?P<pk>[0-9]+)/$', views.MusicCategoryDetail.as_view(), name=views.MusicCategoryDetail.name),
    url(r'^musics/$', views.MusicList.as_view(), name=views.MusicList.name),
    url(r'^musics/(?P<pk>[0-9]+)/$', views.MusicDetail.as_view(), name=views.MusicDetail.name),
    url(r'^players/$', views.PlayerList.as_view(), name=views.PlayerList.name),
    url(r'^players/(?P<pk>[0-9]+)/$', views.PlayerDetail.as_view(), name=views.PlayerDetail.name),
    url(r'^player-scores/$', views.PlayerScoreList.as_view(), name=views.PlayerScoreList.name),
    url(r'^player-scores/(?P<pk>[0-9]+)/$', views.PlayerScoreDetail.as_view(), name=views.PlayerScoreDetail.name),
]