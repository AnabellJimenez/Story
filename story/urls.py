from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'story.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^story/', include('story.urls', namespace="story")),
    url(r'^users/', include('users.urls', namespace = "users")),
    url(r'^post/', include('post.urls', namespace = "post")),
]
