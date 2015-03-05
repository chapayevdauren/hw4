from django.conf.urls import patterns, include, url
from django.contrib import admin
from bproject.blog.api import PostResource
from bproject.blog.api import CommentResource

post_resource = PostResource()
comment_resource = CommentResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^api/v1/', include(post_resource.urls)),
    (r'^api/v1/', include(comment_resource.urls)),
)
