"""Instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
from Instagram import views

from Instagram import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('Profile.urls'),name='index'),
    url(r'^api/images/$',views.images),
    url(r'^api/comments/(?P<pk>[0-9]*)/$',views.comments),
    url(r'^api/comments/$',views.addcomments),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        name='login'),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout',
        kwargs={'next_page': '/login/'}
    ),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

urlpatterns += patterns('',
                        url(r'^media/(?P<path>.*)$',
                            'django.views.static.serve',
                            {'document_root': settings.MEDIA_ROOT,}),
                        )