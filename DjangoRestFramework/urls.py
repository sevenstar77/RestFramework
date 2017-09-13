from django.conf.urls import url, include
from django.contrib import admin
from blog.views import blog_page
from music import urls
import post_service


urlpatterns = [
    # url(r'^rest-api/', include('rest_framework.urls')),
     #url(r'^rest-swagger/', include('rest_framework_swagger.urls')),

     # url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', blog_page),
    url(r'^board/', include('post_service.urls')),
    url(r'api/v1.0/music/', include('music.urls', namespace='music')),
]
