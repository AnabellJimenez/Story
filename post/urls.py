from django.conf.urls import url
 
from . import views
 
urlpatterns = [
 url(r'^$', views.post, name='post'),
 url(r'^create', views.create, name='create'),
 url(r'^(?P<post_id>[0-9]+)/$', "post.views.show", name = 'show'),
 url(r'^(?P<post_id>[0-9]+)/comment', "post.views.comment", name = 'comment'),
 url(r'^list', views.list, name='list'),
 url(r'^feed', views.feed, name='feed'),
 url(r'^(?P<comment_id>[0-9]+)/delete_comment', "post.views.delete_comment", name = 'delete_comment'),
 url(r'^(?P<post_id>[0-9]+)/delete_post', "post.views.delete_post", name = 'delete_post'),
 # url(r'^pic', views.pic, name='pic'),
 url(r'^(?P<post_id>[0-9]+)/upload_file', views.upload_file, name='upload_file'),
 url(r'^gallery', views.gallery, name='gallery'),
 url(r'^add_list', views.add_list, name='add_list'),
 url(r'^user_profile', views.user_profile, name='user_profile'),
]